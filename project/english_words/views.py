import random
from django.shortcuts import render
from .serializers import WordSerializations
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class RandomWord(APIView):
    def get(self, *args, **kwargs):
        all_words = models.Words.objects.all()
        random_word = random.choice(all_words)
        serialized_random_word = WordSerializations(random_word, many=False)
        return Response(serialized_random_word.data)

