from django.urls import path
from .views import (
    quiz_list,
    quiz_detail,
    quiz_instructions
)

urlpatterns = [

    path(
        '',
        quiz_list,
        name='quiz_list'
    ),

    path(
        '<int:quiz_id>/instructions/',
        quiz_instructions,
        name='quiz_instructions'
    ),

    path(
        '<int:quiz_id>/',
        quiz_detail,
        name='quiz_detail'
    ),

]