from django.shortcuts import render

# Create your views here.


from .models import Post
def showPost(request):
    postList = Post.objects.all()
    context = {
        'Post' : postList
    }
    return render(request, 'PostManagement/PostList.html', context)