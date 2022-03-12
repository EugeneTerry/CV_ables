from rest_framework.decorators import api_view
from rest_framework.response import Response
from CV_ables_api.serializers import ApplicantSerializer

@api_view(['GET'])
def get_profile(request):
  applicant = request.auth.user.applicant
  
  serializer = ApplicantSerializer(applicant)
  return Response(serializer.data)
