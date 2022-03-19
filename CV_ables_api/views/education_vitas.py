from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from CV_ables_api.models import EducationVita, Education, Vita
from CV_ables_api.serializers import EducationVitaSerializer

class EducationVitaView(ViewSet):
    def list(self, request):
        education_vita = EducationVita.objects.all()
        
        serializer = EducationVitaSerializer(
            education_vita, many=True, context={'request': request}
            )
        return Response(serializer.data)
    
    def create(self, request):
            education_vita = EducationVita()
            education = Education.objects.get(pk=request.data['education_id'])
            vita = Vita.objects.get(pk=request.data['vita_id'])
            
            education_vita.education = education
            education_vita.vita = vita
            
            try:
                education_vita.save()
                serializer = EducationVitaSerializer(education_vita, context={'request': request})
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as ex:
                return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
            
    def update(self, request, pk=None):
        education_vita = EducationVita.objects.get(pk=pk)
        education = Education.objects.get(pk=request.data['education_id'])
        vita = Vita.objects.get(pk=request.data['vita_id'])
        
        education_vita.education = education
        education_vita.vita = vita
        
        education_vita.save()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)


    def retrieve(self, request, pk=None):
        try:
            # The `2` at the end of the route becomes `pk`
            education_vita = EducationVita.objects.get(pk=pk)
            serializer = EducationVitaSerializer(education_vita, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
    def destroy(self, request, pk=None):
        try:
            education_vita = EducationVita.objects.get(pk=pk)
            education_vita.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except EducationVita.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)