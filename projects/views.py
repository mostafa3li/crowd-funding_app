from django.shortcuts import render
from  comments.views import AddComment
from comments.models import Comment
from comments.forms.addcomment import AddCommentForm
# Create your views here.

def index(request):
  
  form = AddCommentForm()
  comments = Comment.objects.all()
  print(comments[0].title)
  # return render(request, 'comments/index.html',{'form': form,'project_id':project_id,'comments':comments})
  return render(request, 'projects/index.html', {'form': form,'comments':comments})