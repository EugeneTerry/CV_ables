from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from CV_ables_api.models import ExperienceVita, Experience, Vita
from CV_ables_api.serializers import ExperienceVitaSerializer

class ExperienceVitaView(ViewSet):
    def list(self, request):
        experience_vita = ExperienceVita.objects.all()
        
        serializer = ExperienceVitaSerializer(
            experience_vita, many=True, context={'request': request}
            )
        return Response(serializer.data)
    
    def create(self, request):
            experience_vita = ExperienceVita()
            experience = Experience.objects.get(pk=request.data['experience_id'])
            vita = Vita.objects.get(pk=request.data['vita_id'])
            
            experience_vita.experience = experience
            experience_vita.vita = vita
            
            try:
                experience_vita.save()
                serializer = ExperienceVitaSerializer(experience_vita, context={'request': request})
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as ex:
                return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
            try:
                experience_vita = ExperienceVita.objects.get(pk=pk)
                serializer = ExperienceVitaSerializer(experience_vita, context={'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as ex:
                return HttpResponseServerError(ex)
            
    def update(self, request, pk=None):
            experience_vita = ExperienceVita.objects.get(pk=pk)
            experience = Experience.objects.get(pk=request.data['experience_id'])
            vita = Vita.objects.get(pk=request.data['vita_id'])
            
            experience_vita.experience = experience
            experience_vita.vita = vita
            
            experience_vita.save()
            
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
    def destroy(self, request, pk=None):
        try:
            experience_vita = ExperienceVita.objects.get(pk=pk)
            experience_vita.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except ExperienceVita.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
