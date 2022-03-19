from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from CV_ables_api.models import Project, Applicant
from CV_ables_api.serializers import ProjectSerializer
class ProjectView(ViewSet):
    def list(self, request):
        applicant = request.auth.user.applicant
        project = Project.objects.filter(applicant=applicant)
    
        serializer = ProjectSerializer(
            project, many=True, context={'request': request}
            )
        return Response(serializer.data)
        
    def create(self, request):
        project = Project()
        applicant = request.auth.user.applicant
        
        project.title = request.data['title']
        project.github_url = request.data['github_url']
        project.deploy_url = request.data['deploy_url']
        project.image_url = request.data['image_url']
        project.applicant = applicant
        
        try:
            project.save()
            serializer = ProjectSerializer(project, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        try:
            # The `2` at the end of the route becomes `pk`
            project = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(project, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
    def update(self, request, pk=None):
        project = Project.objects.get(pk=pk)
        applicant = request.auth.user.applicant

        project.title = request.data['title']
        project.github_url = request.data['github_url']
        project.deploy_url = request.data['deploy_url']
        project.image_url = request.data['image_url']
        project.applicant = applicant
        project.save()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)
        
    def destroy(self, request, pk=None):
        try:
            project = Project.objects.get(pk=pk)
            project.delete()
            
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Project.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
