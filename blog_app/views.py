from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import blog
from .forms import blog_form


# Create your views here.
class HomePage(ListView):
    model = blog
    template_name = 'home.html'



def displayform(request):
    form_obj = blog_form()
    return render(request,'second.html',{'form':form_obj})


def save_fun(request):
    if request.method=="POST":
        data=blog_form(request.POST)
        if data.is_valid():
            data.save()
            return redirect('/')
    else:
        form_obj=blog_form
        return render(request, 'home.html', {'form': form_obj})


def display_data(request):
    records=blog.objects.all()
    return render(request,'show.html',{'rec':records})

def edit_blog(request,id):
    records = blog.objects.get(id=id)
    return render(request,'edit.html',{'record':records})
#
def update_fun(request,id):
    student=blog.objects.get(id=id)
    if request.method=="POST":
        data=blog_form(request.POST,instance=student)
        if data.is_valid():
            data.save()
            return redirect('/displaydata')
    else:
        form_obj=blog_form
        return render(request, 'home.html', {'form': form_obj})

def delete_blog(request,id):
    task = blog.objects.get(id=id)
    task.delete()
    return redirect('/displaydata')

def search_blog(request):
    if request.method == "GET":
        searched = request.GET.get('searched')

        data=blog.objects.all().filter(title=searched)

        return render(request, 'search.html', {'searched': searched, 'data': data})
    else:
        return render(request, 'search.html', {})