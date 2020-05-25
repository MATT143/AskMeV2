from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post
from .forms import PostQuestionForm
import json,requests
from .serializers import GetSolutionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from uuid import UUID
from django.utils import timezone
from django.views.generic import DetailView,DeleteView


# Create your views here.

def home(request):
    return render(request,'quest/home.html')

class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)


class CreatePostView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostQuestionForm

    def CreatePostRequestPayload(self,form):
        request={"cust_id":form.instance.author_id,
                 "quest_id":form.instance.id,
                 "title":form.instance.title,
                 "category":form.instance.category,
                 "question":form.instance.content}
        return request

    def PostDataToConsultantApp(self,postrequest):
        url='http://localhost:9000/quest/post/master/tasks/v1'
        reqs = json.dumps(postrequest,cls=UUIDEncoder)
        response = requests.post(url=url, data=reqs, headers={'Content-type': 'application/json'})
        return response


    def form_valid(self, form):
        form.instance.author=self.request.user
        self.object=form.save()
        postrequest=self.CreatePostRequestPayload(form)
        self.PostDataToConsultantApp(postrequest)
        return super(CreatePostView,self).form_valid(form)



class GetSolutionView(APIView):
    def post(self,request):
        ser = GetSolutionSerializer(data=request.data)
        if ser.is_valid():
            query1=Post.objects.get(pk=ser.data['quest_id'])
            query1.solution=ser.data['solution']
            query1.status="SOLVED"
            query1.last_modified=timezone.now()
            query1.save()
            return Response({"syncStatus":"success"},status=200)
        return Response(ser.errors,status=400)

class PostDetailsView(DetailView):
    model = Post


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = "/profile/"



















