from rest_framework.decorators import api_view
from rest_framework.response import Response
from CV_ables_api.models import Jobtype
from CV_ables_api.serializers import JobtypeSerializer

@api_view(['GET'])
def get_jobtypes_list(self):
    jobtype = Jobtype.objects.all()
    
    serializer = JobtypeSerializer(jobtype, many=True)
    return Response(serializer.data)