from django.shortcuts import render,render,HttpResponse
from blog.models import blogpost
import random
from django.views.generic import ListView,DetailView,DeleteView,UpdateView
from django.urls import reverse_lazy
from blog.forms import Myblogform


# Create your views here.

def index(request):
    count=len(blogpost.objects.all())
    postdata=list(blogpost.objects.all()[:30])
    
    #This is for showing topic names in index page
    topic_names=blogpost.objects.values_list('topic',flat=True).distinct() 
    
     
    random.shuffle(postdata)
    blog_data=postdata[:3]
    random.shuffle(blog_data)
    return render(request,'index.html',{'data':postdata,'blog_data':blog_data,'topics':topic_names,'count':count})


def search_result(request):
    search_element=request.GET.get('search_me')
    if search_element=="":
        return HttpResponse('No data for search!')
    else:
        search_data=blogpost.objects.all().filter(title__icontains=search_element)
        count=len(search_data)
        print(search_result)
    
    return render(request,'search_result.html',{'searched':search_element,'result':search_data,'count':count})



#Listing the blogs when we click on all blogs from index page

class ListData(ListView):
    model=blogpost
    template_name='blogpost_list.html'
    def get_queryset(self):
        return blogpost.objects.all().order_by('topic')

        

#detail of every blog when we click on any blog title

class DetailData(DetailView):
    model=blogpost
    template_name='blogpost_detail.html'
    context_object_name='data'


#This code is for update blog post
class UpdateBlog(UpdateView):
    model=blogpost
    template_name='edit_blog.html'
   
class EditBlog(UpdateView):
    model=blogpost
    template_name='edit_blog.html'
    fields=['topic','title','post']
    success_url=reverse_lazy('profile')

#Delete the blog post with this view class

class DeleteBlog(DeleteView):
    model=blogpost
    template_name='delete_blog.html'
    success_url=reverse_lazy('profile') #This shows- When delete is successfull then where to go!