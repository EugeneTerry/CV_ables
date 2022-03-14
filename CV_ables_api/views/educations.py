from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from CV_ables_api.models import Education, Applicant
from CV_ables_api.serializers import EducationSerializer

class EducationView(ViewSet):
    def list(self, request):
        education = Education.objects.all()
        
        serializer = EducationSerializer(
            education, many=True, context={'request': request}
            )
        return Response(serializer.data)
    
    def create(self, request):
        education = Education()
        applicant = Applicant.objects.get(pk=request.data['applicant_id'])
        
        education.school_name = request.data['school_name']
        education.city = request.data['city']
        education.state = request.data['state']
        education.diploma = request.data['diploma']
        education.grad_year = request.data['grad_year']
        education.applicant = applicant
        
        try:
            education.save()
            serializer = EducationSerializer(education, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk=None):
        education = Education.objects.get(pk=pk)
        applicant = Applicant.objects.get(pk=request.data['applicant_id'])
        
        education.school_name = request.data['school_name']
        education.city = request.data['city']
        education.state = request.data['state']
        education.diploma = request.data['diploma']
        education.grad_year = request.data['grad_year']
        education.applicant = applicant
        education.save()
        
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    
    def retrieve(self, request, pk=None):
        try:
            # The `2` at the end of the route becomes `pk`
            education = Education.objects.get(pk=pk)
            serializer = EducationSerializer(education, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
    def destroy(self, request, pk=None):
        try:
            education = Education.objects.get(pk=pk)
            education.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Education.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
