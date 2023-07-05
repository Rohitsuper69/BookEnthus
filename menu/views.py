from django.shortcuts import render, redirect
from .forms import *
from .models import *
import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    print(request.user)
    return render(request,'menu/home.html',{})
@login_required
def bookReview_view(request):
    bookReviews = bookReviews_model.objects.filter(user=request.user)
    context={
        "bookReviews":bookReviews
    }
    return render(request,"menu/bookreview.html",context)
@login_required
def review(request):
    if request.method == "POST":
        form = bookReview_form(request.POST)
        if form.is_valid():
            review=bookReviews_model(
                user=request.user,
                title=request.POST['title'], 
                author=request.POST['author'], 
                review=request.POST['review']
            )
            review.save()
            return redirect('bookreview')
    form = bookReview_form()
    context={
        "form":form
    }
    return render(request,"menu/review.html",context)
@login_required
def deletereview(request,pk=None):
    bookReviews_model.objects.get(id=pk).delete()
    return redirect("bookreview")
@login_required
def todo_view(request):
    todos = todo_model.objects.filter(user=request.user)
    context={
        "todos":todos
    }
    return render(request,"menu/todo.html",context)
@login_required
def toread(request):
    if request.method=="POST":
        form = todo_form(request.POST)
        if form.is_valid():
            todo = todo_model(
                user=request.user,
                title=request.POST['title']
            )
            todo.save()
            return redirect('todo')
    form=todo_form()
    context={
        "form":form
    }
    return render(request,"menu/toread.html",context)
@login_required
def to_delete(request, pk = None):
    todo_model.objects.get(id=pk).delete()
    return redirect('todo')

def books(request):
    if request.method=="POST":
        form = DashboardForm(request.POST)
        text = request.POST['text']
        url="https://www.googleapis.com/books/v1/volumes?q="+text
        r=requests.get(url)
        answer=r.json()
        try:
            result_list=[]
            for i in range(10):
                result_dict={
                'title':answer['items'][i]['volumeInfo']['title'],
                'subtitle':answer['items'][i]['volumeInfo'].get('subtitle'),
                'desc':answer['items'][i]['volumeInfo'].get('description'),
                'count':answer['items'][i]['volumeInfo'].get('pageCount'),
                'categories':answer['items'][i]['volumeInfo'].get('categories'),
                'rating':answer['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail':answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview':answer['items'][i]['volumeInfo'].get('previewLink')
                }
                result_list.append(result_dict)
                context={
                    "form":form,
                    "results":result_list
                }
        except:
             context={
                    "form":form
                }
        return render(request,"menu/books.html",context)
    else:
        form = DashboardForm()
    context={
        "form":form
    }
    return render(request,"menu/books.html",context)

def dict(request):
    if request.method=="POST":
        form = DashboardForm(request.POST)
        text=request.POST['text']
        url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
        r = requests.get(url)
        answer=r.json()
        try:
            phonetics = answer[0]['phonetics'][1]['text']
            audio = answer[0]['phonetics'][0]['audio']
            definition = answer[0]['meanings'][0]['definitions'][0]['definition']
            examples=[]
            for i in range(len(answer[0]['meanings'])):
                try:
                    examples.append(answer[0]['meanings'][i]['definitions'][0]['example'])
                except:
                    pass
            synonyms = answer[0]['meanings'][0]['definitions'][0]['synonyms']
            context={
                "form":form,
                "input":text,
                "phonetics":phonetics,
                "audio":audio,
                "definition":definition,
                "examples":examples,
                "synonyms":synonyms
            }
        except:
            context={
                "form":form,
                "input":""
            }
        return render(request,"menu/dict.html",context)
    
    form = DashboardForm()
    context={
        "form":form
    }
    return render(request,"menu/dict.html",context)
@login_required

def update_user_data(user):
    Profile.objects.update_or_create(user=user, defaults={'mob': user.profile.mob},)

def register(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,f"Account created for {username}!")
            return redirect('login')
    else:
        form=UserRegistrationForm()
    context={
        "form":form
    }
    return render(request,"menu/register.html",context)
@login_required
def profile(request):
    UserProfile = Profile.objects.filter(user=request.user)
    pk=request.user.id
    if UserProfile:
        print(UserProfile)
        context={
            "UserProfile":UserProfile
        }
        return render(request,"menu/profile.html",context)
    else:
        return redirect('create-profile')
    
@login_required
def cprofile(request):
    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            profile=Profile(
                user=request.user,
                first_name=request.POST['first_name'], 
                last_name=request.POST['last_name'], 
                email=request.POST['email'],
                bio=request.POST['bio'],
                Interest=request.POST['Interest']
            )
            profile.save()
            return redirect('profile')
    form = CreateProfileForm()
    context={
        "form":form
    }
    return render(request,'menu/cprofile.html',context)

@login_required
def online_reviews(request):
    reviews=bookReviews_model.objects.filter(isPublic=True).exclude(user=request.user)
    context={
        "reviews":reviews,
        "user":request.user
    }

    return render(request,"menu/onlinereviews.html",context)