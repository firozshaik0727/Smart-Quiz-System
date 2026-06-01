from django.shortcuts import render
from results.models import Result
from django.db.models import Avg, Max


def dashboard(request):

    results = Result.objects.filter(
        user=request.user
    )

    total_quizzes = results.count()

    highest_score = results.aggregate(
        Max('score')
    )['score__max']

    average_percentage = results.aggregate(
        Avg('percentage')
    )['percentage__avg']

    return render(
        request,
        'dashboard/dashboard.html',
        {
            'results': results,
            'total_quizzes': total_quizzes,
            'highest_score': highest_score,
            'average_percentage': average_percentage
        }
    )