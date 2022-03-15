from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from CV_ables_api.models import Description, Experience
from CV_ables_api.serializers import DescriptionSerializer

class DescriptionView(ViewSet):
    def list(self, request):
        description = Description.objects.all()
        
        serializer = DescriptionSerializer(
            description, many=True, context={'request': request}
            )
        return Response(serializer.data)
    
    def create(self, request):
        description = Description()
        experience = Experience.objects.get(pk=request.data['experience_id'])
        
        description.description_text = request.data['description_text']
        description.experience = experience
        
        try:
            description.save()
            serializer = DescriptionSerializer(description, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        try:
            # The `2` at the end of the route becomes `pk`
            description = Description.objects.get(pk=pk)
            serializer = DescriptionSerializer(description, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
    def update(self, request, pk=None):
        description = Description.objects.get(pk=pk)
        experience = Experience.objects.get(pk=request.data['experience_id'])
        
        description.description_text = request.data['description_text']
        description.experience = experience
        description.save()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, pk=None):
        try:
            description = Description.objects.get(pk=pk)
            description.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Description.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
