from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from CV_ables_api.models.applicant import Applicant
from CV_ables_api.serializers import ApplicantSerializer
from django.http import HttpResponseServerError


@api_view(['GET'])
def get_profile(request):
  applicant = request.auth.user.applicant
  
  serializer = ApplicantSerializer(applicant)
  return Response(serializer.data)
class AppicationView(ViewSet):
  def update(self, request, pk=None):
          applicant = Applicant.objects.get(pk=pk)
          
          applicant.portfolio_url = request.data['portfolio_url']
          applicant.linkedin_url = request.data['linkedin_url']
          applicant.github_url = request.data['github_url']
          applicant.city = request.data['city']
          applicant.state = request.data['state']
          applicant.save()
          
          return Response({}, status=status.HTTP_204_NO_CONTENT)
  
  def list(self, request):
      applicant = request.auth.user.applicant
  
      serializer = ApplicantSerializer(applicant)
      return Response(serializer.data)
    
  def retrieve(self, request, pk=None):
        try:
            # The `2` at the end of the route becomes `pk`
            applicant = Applicant.objects.get(pk=pk)
            serializer = ApplicantSerializer(applicant, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)