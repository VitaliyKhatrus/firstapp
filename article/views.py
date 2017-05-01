# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from forms import CommentForm
from django.core.context_processors import csrf
#from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from django.shortcuts import render
from django.views.generic.list import ListView

#######
##from django.contrib.auth.models import User
'''
class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'article_list.html'
 
    def get_queryset(self):
        articles = Article.objects.all()
        # Отбираем первые 10 статей
        paginator = Paginator(articles, 2)
        page = self.request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            articles = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            articles = paginator.page(paginator.num_pages)
        return articles
'''

# Create your views here.

#######test#######
def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is %s view</html></body>"%view
    return HttpResponse(html) 


def template_two(request):
    view = "template_two"
    t = get_template('myview.html')
    html = t.render(Context({'name': view}))
    return HttpResponse(html)

def template_three(request):
    view = "template_three"
    return render_to_response('myview.html', {'name': view})

#####test######


#######for blog




def articles(request, page_number=1):
###def articles(request, pg=1):
    # current_user = request.user
    # print current_user.id

    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 2)
    context = {
               'articles': current_page.page(page_number),
               'username': auth.get_user(request).username,
               'all_articles': all_articles
               }
    return render_to_response('articles.html', context)




def article(request, article_id=1):
    try:
        all_articles = Article.objects.all()
        comment_form = CommentForm
        args = {}
        args.update(csrf(request)) # defence our form from hack (tocken)
        args['article'] = Article.objects.get(id=article_id)
        args['comments'] = Comments.objects.filter(comments_article_id = article_id)
        args['form'] = comment_form
        args['username'] = auth.get_user(request).username
        args['all_articles'] = all_articles

        return render_to_response('article.html', args)
    except Article.DoesNotExist:
        return render(request, 'error.html')

'''
def addlike(request, article_id):
    
    try:
        if article_id in request.COOKIES:
            redirect('/')
            
        else:            
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            #response = redirect('/') #cookie
            #response = redirect('/page/%s/' % page) # try to stay on the current page
            #response = redirect('/')
            #response.set_cookie(article_id, "test") # add 'max_age = 60' - time to live cookie 
            response = redirect(request.GET.get('next', '/'))
    except ObjectDoesNotExist:
        raise Http404
    return response
'''

def addlike(request, article_id):
    """Like article."""
    back_url = request.META['HTTP_REFERER'] #The referring page, if any 
    try:
        if article_id in request.COOKIES:
            redirect(back_url)
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect(back_url)
            response.set_cookie(article_id, 'value')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect(back_url)

def adddislike(request, article_id):
    """Dislike article."""
    back_url = request.META['HTTP_REFERER'] #The referring page, if any 
    try:
        if article_id in request.COOKIES:
            redirect(back_url)
        else:
            article = Article.objects.get(id=article_id)
            article.article_dislikes += 1
            article.save()
            response = redirect(back_url)
            response.set_cookie(article_id, 'value')
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect(back_url)
  


def addcomment(request, article_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            current_user = request.user
            #u = User.objects.get(request.POST['profile_id'])
            comment.comments_article = Article.objects.get(id=article_id)
            comment.comments_username = current_user.username
            # current_user = request.user
            # print current_user.id
            #############
            ##comment.comments_user = User.objects.get(request.POST['profile_id'])
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/blog/articles/get/%s/' % article_id)

    # if request.user.is_authenticated():
    # # Do something for authenticated users.
    # else:
    # # Do something for anonymous users.
