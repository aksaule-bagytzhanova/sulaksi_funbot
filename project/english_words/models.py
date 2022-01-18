from django.db import models
# Create your models here.


class Words(models.Model):
    part_speech = [
        ('noun', 'Noun'),
        ('verb', 'Verb'),
        ('adjective', 'Adjective'),
        ('pronoun', 'Pronoun'),
        ('adverb', 'Аdverb'),
        ('numeral', 'Numeral'),
    ]

    word = models.CharField(verbose_name="Word", max_length=100)
    part_of_word = models.CharField(verbose_name="Part_speech", max_length=100, choices=part_speech)

    def __str__(self):
        return self.word + " " + self.part_of_word
