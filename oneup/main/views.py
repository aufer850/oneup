from http.cookiejar import request_path
from idlelib.history import History

from django.shortcuts import render
from news.models import Articles
from django.shortcuts import get_object_or_404, redirect
from main.forms import commentform
# Create your views here.
from django.shortcuts import render

def index(request):
    news = Articles.objects.order_by('date')
    return render(request, 'main/main.html', {'news':news})

def about(request):
    return render(request,'main/about.html')

def review(request):
    news = Articles.objects.filter(articletype='огляд').order_by('date')
    return render(request,'main/review.html', {'news': news})

def selection(request):
    news = Articles.objects.filter(articletype='підбірка').order_by('date')
    return render(request,'main/selection.html', {'news': news})

def article(request):
    news = Articles.objects.filter(articletype = 'стаття').order_by('date')
    return render(request,'main/article.html', {'news':news})

def articlewindow(request, article_id):
    newcomm = commentform
    newcomm.articlekey = article_id
    user_ip = get_client_ip(request)
    if request == 'POST':
        newcomm = commentform(request.POST)
        newcomm.id_articlekey = article_id
    news = Articles.objects.order_by('date')
    new = Articles.objects.get(pk = article_id)
    if user_ip:
        new.view(user_ip)
    comments = new.comments.all()
    return render(request,'main/articlewindow.html', {'id':article_id,'news':news,'new': new,'commentform':newcomm,'comments':comments })

def comment(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(Articles, id=article_id)
        newcomm = commentform(request.POST)
        print(newcomm)
        if newcomm.is_valid():
            print("CHTO BLYAT NAHUI")
            new_comment = newcomm.save(commit=False)
            new_comment.articlekey = article
            new_comment.save()
    return redirect('/' + str(article_id))

def like_article(request, article_id):
    article = get_object_or_404(Articles, id=article_id)
    user_ip = get_client_ip(request)
    article.addlike(user_ip)
    frommain = request.POST.get('redirectto')
    if frommain:
        return redirect(frommain)
    else:
        return redirect('/' + str(article_id))

def dislike_article(request, article_id):
    article = get_object_or_404(Articles, id=article_id)
    user_ip = get_client_ip(request)
    article.adddislike(user_ip)
    frommain = request.POST.get('redirectto')
    if frommain:
        return redirect(frommain)
    else:
        return redirect('/' + str(article_id))

def search(request):
    query = request.GET.get('query', '').strip()  # Получаем запрос из формы
    results = Articles.objects.filter(title__icontains=query) if query else []  # Фильтруем статьи
    return render(request, 'main/searchresults.html', {'news': results, 'query': query})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip