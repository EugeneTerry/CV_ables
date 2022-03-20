from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from CV_ables_api.models import Prospect, ProspectStatus, prospectstatus
from CV_ables_api.serializers import ProspectSerializer
class ProspectView(ViewSet):
    def list(self, request):
        applicant = request.auth.user.applicant
        prospect = Prospect.objects.filter(applicant=applicant)
        
        serializer = ProspectSerializer(
            prospect, many=True, context={'request': request}
        )
        return Response(serializer.data)
    
    def create(self, request):
        prospect = Prospect()
        applicant = request.auth.user.applicant
        prospectstatus = ProspectStatus.objects.get(pk=request.data['prospectstatus_id'])
        
        
        prospect.prospect_name = request.data['prospect_name']
        prospect.listing_url = request.data['listing_url']
        prospect.markedvita = request.data['markedvita']
        prospect.notes = request.data['notes']
        
        prospect.applicant = applicant
        prospect.prospectstatus = prospectstatus
        
        try:
            prospect.save()
            serializer = ProspectSerializer(prospect, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        try:
            prospect = Prospect.objects.get(pk=pk)
            serializer = ProspectSerializer(prospect, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
    def update(self, request, pk=None):
        prospect = Prospect.objects.get(pk=pk)
        prospectstatus = ProspectStatus.objects.get(pk=request.data['prospectstatus_id'])

        applicant = request.auth.user.applicant
        
        prospect.prospect_name = request.data['prospect_name']
        prospect.listing_url = request.data['listing_url']
        prospect.markedvita = request.data['markedvita']
        prospect.notes = request.data['notes']
        prospect.prospectstatus = prospectstatus
        prospect.applicant = applicant
        prospect.save()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):
        try:
            prospect = Prospect.objects.get(pk=pk)
            prospect.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Prospect.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
