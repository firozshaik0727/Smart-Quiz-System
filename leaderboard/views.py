from django.shortcuts import render
from results.models import Result


def leaderboard(request):

    results = Result.objects.order_by(
        '-score',
        '-percentage'
    )

    return render(
        request,
        'leaderboard/leaderboard.html',
        {
            'results': results
        }
    )