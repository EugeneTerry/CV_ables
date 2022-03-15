from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from CV_ables_api.models import Project
from CV_ables_api.serializers import ProjectSerializer
class ProjectView(ViewSet):
    def list(self, request):
        project = Project.objects.all()
        
        serializer = ProjectSerializer(
            project, many=True, context={'request': request}
            )
        return Response(serializer.data)