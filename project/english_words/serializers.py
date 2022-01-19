from rest_framework.serializers import *
from . import models


class WordSerializations(ModelSerializer):
    class Meta:
        model = models.Words
        fields = ['pk', 'word', 'part_of_word']

