from django.db import models
# Create your models here.


class Words(models.Model):
    PART_SPEECH = [
        ('noun', 'Noun'),
        ('verb', 'Verb'),
        ('adjective', 'Adjective'),
        ('pronoun', 'Pronoun'),
        ('adverb', 'Аdverb'),
        ('numeral', 'Numeral'),
    ]

    word = models.CharField(verbose_name="Word", max_length=100)
    part_of_word = models.CharField(verbose_name="Part_speech", max_length=100, choices=PART_SPEECH)

    def __str__(self):
        return self.part_of_word + " " + self.word
