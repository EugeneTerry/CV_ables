from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from CV_ables_api.models import Mission, Jobtype, Applicant, mission
from CV_ables_api.serializers import MissionSerializer

class MissionView(ViewSet):
    def list(self, request):
        applicant = request.auth.user.applicant
        mission = Mission.objects.filter(applicant=applicant)
        
        serializer = MissionSerializer(
            mission, many=True, context={'request': request}
            )
        return Response(serializer.data)
    
    def create(self, request):
        mission = Mission()
        applicant = request.auth.user.applicant
        job_type = Jobtype.objects.get(pk=request.data['job_type_id'])
        
        mission.mission_text = request.data['mission_text']
        mission.applicant = applicant
        mission.job_type = job_type
        
        try:
            mission.save()
            serializer = MissionSerializer(mission, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        try:
            # The `2` at the end of the route becomes `pk`
            mission = Mission.objects.get(pk=pk)
            serializer = MissionSerializer(mission, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
    def update(self, request, pk=None):
        mission = Mission.objects.get(pk=pk)
        applicant = request.auth.user.applicant
        job_type = Jobtype.objects.get(pk=request.data['job_type_id'])
        
        mission.mission_text = request.data['mission_text']
        mission.applicant = applicant
        mission.job_type = job_type
        mission.save()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, pk=None):
        try:
            mission = Mission.objects.get(pk=pk)
            mission.delete()
            
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Mission.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
