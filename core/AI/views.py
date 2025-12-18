"""
Views for AI app.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AISerializer


class Studyplan(APIView):
    """
    A mock AI model that generates a study plan.
    """
    def post(self, request):
        serializer = AISerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        free_hours = serializer.validated_data['free_hours']
        lessons = serializer.validated_data['lessons']

        total_credits = sum(lessons.values())
        hour_per_credit= free_hours / total_credits

        study_plan = {
            name: round(credit * hour_per_credit, 2)
            for name, credit in lessons.items()
        }

        return Response(
            {
                'total_credits': total_credits,
                'hour_per_credit': round(hour_per_credit, 2),
                'study_plan': study_plan
            },
            status=status.HTTP_200_OK
        )