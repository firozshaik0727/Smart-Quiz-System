from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import date
from results.models import Result


def generate_certificate(request):

    latest_result = Result.objects.filter(
        user=request.user
    ).order_by('-id').first()

    if not latest_result or latest_result.percentage < 70:
        return HttpResponse(
            """
            <h2 style='color:red;text-align:center;margin-top:50px;'>
            Certificate is available only for scores 70% and above.
            </h2>
            """
        )

    response = HttpResponse(
        content_type='application/pdf'
    )

    response[
        'Content-Disposition'
    ] = 'attachment; filename="certificate.pdf"'

    p = canvas.Canvas(response)

    width = 595
    height = 842

    p.setFillColorRGB(0.93, 0.96, 1)

    p.rect(
        0,
        0,
        width,
        height,
        fill=1
    )

    p.setStrokeColor(colors.darkblue)
    p.setLineWidth(6)

    p.rect(
        25,
        25,
        width - 50,
        height - 50
    )

    p.setLineWidth(2)

    p.rect(
        40,
        40,
        width - 80,
        height - 80
    )

    p.setFillColor(colors.darkgoldenrod)

    p.setFont(
        "Helvetica-Bold",
        28
    )

    p.drawCentredString(
        width / 2,
        740,
        "CERTIFICATE OF ACHIEVEMENT"
    )

    p.setFillColor(colors.black)

    p.setFont(
        "Helvetica",
        16
    )

    p.drawCentredString(
        width / 2,
        680,
        "This Certificate is Proudly Presented To"
    )

    p.setFont(
        "Helvetica-Bold",
        26
    )

    p.setFillColor(colors.darkblue)

    p.drawCentredString(
        width / 2,
        620,
        request.user.username.upper()
    )

    p.setFillColor(colors.black)

    p.setFont(
        "Helvetica",
        16
    )

    p.drawCentredString(
        width / 2,
        570,
        "For Successfully Completing"
    )

    p.setFont(
        "Helvetica-Bold",
        22
    )

    p.drawCentredString(
        width / 2,
        530,
        latest_result.quiz.title
    )

    p.setFont(
        "Helvetica",
        14
    )

    p.drawCentredString(
        width / 2,
        490,
        f"Score: {latest_result.score}"
    )

    p.drawCentredString(
        width / 2,
        470,
        f"Percentage: {latest_result.percentage:.2f}%"
    )

    p.drawCentredString(
        width / 2,
        430,
        f"Date: {date.today()}"
    )

    p.setFont(
        "Helvetica",
        12
    )

    p.drawCentredString(
        width / 2,
        180,
        "Signature"
    )

    p.setFillColor(colors.darkblue)

    p.setFont(
        "Helvetica-Oblique",
        30
    )

    p.drawCentredString(
        width / 2,
        140,
        "Firoz"
    )

    p.setFillColor(colors.black)

    p.setFont(
        "Helvetica-Bold",
        12
    )

    p.drawCentredString(
        width / 2,
        100,
        "Firoz Shaik"
    )

    p.setFont(
        "Helvetica",
        11
    )

    p.drawCentredString(
        width / 2,
        80,
        "Project Administrator"
    )

    p.save()

    return response