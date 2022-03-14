from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from CV_ables_api.models import Language
from CV_ables_api.serializers import LanguageSerializer

class LanguageView(ViewSet):
    def list(self,request):
        language = Language.objects.all()
        
        serializer = LanguageSerializer(
            language, many=True, context={'request': request}
            )
        return Response(serializer.data)