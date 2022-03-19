from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from CV_ables_api.models import ExperienceFrame, Experience, Applicant, Framework, Project
from CV_ables_api.serializers import ExperienceFrameSerializer

class ExperienceFrameView(ViewSet):
    def list(self, request):
            applicant = request.auth.user.applicant
            experience_frame = ExperienceFrame.objects.filter(applicant=applicant)
        
            serializer = ExperienceFrameSerializer(
                experience_frame, many=True, context={'request': request}
                )
            return Response(serializer.data)
        
    def create(self, request):
            experience_frame = ExperienceFrame()
            experience = Experience.objects.get(pk=request.data['experience_id'])
            applicant = request.auth.user.applicant
            framework = Framework.objects.get(pk=request.data['framework_id'])
            project = Project.objects.get(pk=request.data['project_id'])
            
            experience_frame.experience = experience
            experience_frame.framework = framework
            experience_frame.project = project
            experience_frame.applicant = applicant
            
            try:
                experience_frame.save()
                serializer = ExperienceFrameSerializer(experience_frame, context={'request': request})
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as ex:
                return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
            try:
                experience_frame = ExperienceFrame.objects.get(pk=pk)
                serializer = ExperienceFrameSerializer(experience_frame, context={'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as ex:
                return HttpResponseServerError(ex)
            
    def update(self, request, pk=None):
            experience_frame = ExperienceFrame.objects.get(pk=pk)
            experience = Experience.objects.get(pk=request.data['experience_id'])
            applicant = request.auth.user.applicant
            framework = Framework.objects.get(pk=request.data['framework_id'])
            project = Project.objects.get(pk=request.data['project_id'])
            
            experience_frame.experience = experience
            experience_frame.framework = framework
            experience_frame.project = project
            experience_frame.applicant = applicant
            
            experience_frame.save()
            
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
    def destroy(self, request, pk=None):
        try:
            experience_frame = ExperienceFrame.objects.get(pk=pk)
            experience_frame.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except ExperienceFrame.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
