from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Quiz, Question, Option
from results.models import Result


@login_required
def quiz_list(request):

    quizzes = Quiz.objects.all()

    return render(
        request,
        'quiz/quiz_list.html',
        {
            'quizzes': quizzes
        }
    )


@login_required
def quiz_detail(request, quiz_id):

    quiz = get_object_or_404(
        Quiz,
        id=quiz_id
    )

    questions = Question.objects.filter(
        quiz=quiz
    )

    if request.method == 'POST':

        score = 0

        for question in questions:

            selected_option = request.POST.get(
                f'question_{question.id}'
            )

            if selected_option:

                option = Option.objects.get(
                    id=selected_option
                )

                if option.is_correct:
                    score += 1

        total_questions = questions.count()

        percentage = (
            score / total_questions
        ) * 100

        Result.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            percentage=percentage
        )

        return render(
            request,
            'quiz/result.html',
            {
                'score': score,
                'total': total_questions,
                'percentage': percentage
            }
        )

    return render(
        request,
        'quiz/quiz_detail.html',
        {
            'quiz': quiz,
            'questions': questions
        }
    )
@login_required
def quiz_instructions(request, quiz_id):

    quiz = get_object_or_404(
        Quiz,
        id=quiz_id
    )

    total_questions = Question.objects.filter(
        quiz=quiz
    ).count()

    return render(
        request,
        'quiz/instructions.html',
        {
            'quiz': quiz,
            'total_questions': total_questions
        }
    )