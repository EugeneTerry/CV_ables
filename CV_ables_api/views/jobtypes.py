from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from CV_ables_api.models import Jobtype
from CV_ables_api.serializers import JobtypeSerializer
class JobtypeView(ViewSet):
    def list(self, request):
        jobtype = Jobtype.objects.all()
        
        serializer = JobtypeSerializer(
            jobtype, many=True, context={'request': request}
            )
        return Response(serializer.data)