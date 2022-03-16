from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from CV_ables_api.models import ExperienceLang, Experience, Applicant, Language, Project, experience_lang
from CV_ables_api.models.vita import Vita
from CV_ables_api.serializers import ExperienceLangSerializer

class ExperienceLangView(ViewSet):
    def list(self, request):
        experience_lang = ExperienceLang.objects.all()
        
        serializer = ExperienceLangSerializer(
            experience_lang, many=True, context={'request': request}
            )
        return Response(serializer.data)
    
    def create(self, request):
            experience_lang = ExperienceLang()
            experience = Experience.objects.get(pk=request.data['experience_id'])
            applicant = Applicant.objects.get(pk=request.data['applicant_id'])
            language = Language.objects.get(pk=request.data['language_id'])
            project = Project.objects.get(pk=request.data['project_id'])
            
            experience_lang.experience = experience
            experience_lang.language = language
            experience_lang.project = project
            experience_lang.applicant = applicant
            
            try:
                experience_lang.save()
                serializer = ExperienceLangSerializer(experience_lang, context={'request': request})
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as ex:
                return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
            try:
                experience_lang = ExperienceLang.objects.get(pk=pk)
                serializer = ExperienceLangSerializer(experience_lang, context={'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as ex:
                return HttpResponseServerError(ex)
            
    def update(self, request, pk=None):
            experience_vita = ExperienceLang.objects.get(pk=pk)
            experience = Experience.objects.get(pk=request.data['experience_id'])
            applicant = Applicant.objects.get(pk=request.data['applicant_id'])
            language = Language.objects.get(pk=request.data['language_id'])
            project = Project.objects.get(pk=request.data['project_id'])
            
            experience_lang.experience = experience
            experience_lang.language = language
            experience_lang.project = project
            experience_lang.applicant = applicant
            
            experience_lang.save()
            
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        
    def destroy(self, pk=None):
        try:
            experience_lang = ExperienceLang.objects.get(pk=pk)
            experience_lang.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except ExperienceLang.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
