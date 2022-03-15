from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from CV_ables_api.models import Vita, Applicant, Jobtype, Mission, Prospect, vita
from CV_ables_api.serializers import VitaSerializer
class VitaView(ViewSet):
    def list(self, request):
        vita = Vita.objects.all()
        
        serializer = VitaSerializer(
            vita, many=True, context={'request': request}
        )
        return Response(serializer.data)
    
    def create(self, request):
        vita = Vita()
        applicant = Applicant.objects.get(pk=request.data['applicant_id'])
        job_type = Jobtype.objects.get(pk=request.data['job_type_id'])
        mission = Mission.objects.get(pk=request.data['mission_id'])
        prospect = Prospect.objects.get(pk=request.data['prospect_id'])
        
        vita.slug = request.data['slug']
        vita.published = request.data['published']
        
        vita.job_type = job_type
        vita.mission = mission
        vita.applicant = applicant
        vita.prospect = prospect
        
        try:
            vita.save()
            serializer = VitaSerializer(vita, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
  
    def retrieve(self, request, pk=None):
        try:
            vita = Vita.objects.get(pk=pk)
            serializer = VitaSerializer(vita, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)
          
    def update(self, request, pk=None):
            vita = Vita.objects.get(pk=pk)
            applicant = Applicant.objects.get(pk=request.data['applicant_id'])
            job_type = Jobtype.objects.get(pk=request.data['job_type_id'])
            mission = Mission.objects.get(pk=request.data['mission_id'])
            prospect = Prospect.objects.get(pk=request.data['prospect_id'])
            
            vita.slug = request.data['slug']
            vita.published = request.data['published']
            
            vita.job_type = job_type
            vita.mission = mission
            vita.applicant = applicant
            vita.prospect = prospect
            vita.save()
            
            return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, pk=None):
        try:
            vita = Vita.objects.get(pk=pk)
            vita.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Vita.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)