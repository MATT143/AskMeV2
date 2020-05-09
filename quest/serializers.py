from rest_framework import serializers
# from .models import SolutionCallBack
from django.utils import timezone


# class GetSolutionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=SolutionCallBack
#         fields="__all__"

class GetSolutionSerializer(serializers.Serializer):
    quest_id=serializers.CharField(max_length=100)
    solution=serializers.CharField(max_length=2000)
    creation_date=serializers.DateTimeField(default=timezone.now())


