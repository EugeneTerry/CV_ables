from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from CV_ables_api.models import Experience, Jobtype, Applicant
from CV_ables_api.serializers import ExperienceSerializer
class ExerienceView(ViewSet):
  def list(self, request):
        applicant = request.auth.user.applicant
        experience = Experience.objects.filter(applicant=applicant)
    
        serializer = ExperienceSerializer(
        experience, many=True, context={'request': request})
        return Response(serializer.data)
  
  def create(self, request):
        experience = Experience()
        applicant = request.auth.user.applicant
        jobtype = Jobtype.objects.get(pk=request.data['jobtype_id'])
        
        experience.job_title = request.data['job_title']
        experience.company = request.data['company']
        experience.start_yr = request.data['start_yr']
        experience.end_yr = request.data['end_yr']
        experience.duties = request.data['duties']
        
        experience.applicant = applicant
        experience.job_type = jobtype
        
        try:
            experience.save()
            serializer = ExperienceSerializer(experience, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
  
  def retrieve(self, request, pk=None):
        try:
            experience = Experience.objects.get(pk=pk)
            serializer = ExperienceSerializer(experience, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)
          
  def update(self, request, pk=None):
        experience = Experience.objects.get(pk=pk)
        applicant = request.auth.user.applicant
        jobtype = Jobtype.objects.get(pk=request.data['jobtype_id'])
        
        experience.job_title = request.data['job_title']
        experience.company = request.data['company']
        experience.start_yr = request.data['start_yr']
        experience.end_yr = request.data['end_yr']
        experience.duties = request.data['duties']
        
        experience.applicant = applicant
        experience.job_type = jobtype
        experience.save()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
  def destroy(self, request, pk=None):
      try:
          experience = Experience.objects.get(pk=pk)
          experience.delete()

          return Response({}, status=status.HTTP_204_NO_CONTENT)

      except Experience.DoesNotExist as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

      except Exception as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
