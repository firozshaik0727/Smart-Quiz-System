from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    title = models.CharField(max_length=200)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    timer = models.IntegerField(
        help_text="Timer in Minutes"
    )

    def __str__(self):
        return self.title


class Question(models.Model):

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE
    )

    question_text = models.TextField()

    def __str__(self):
        return self.question_text


class Option(models.Model):

    question = models.ForeignKey(
    Question,
    on_delete=models.CASCADE,
    related_name='options'
)

    option_text = models.CharField(
        max_length=255
    )

    is_correct = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.option_text