from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from uploadfile.models import base_64_file


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        file_url = base_64_file(data=request.data['user_photo']) # Name define dy request end
        print(file_url)
        return Response({"Successfully Uploaded"}, status=status.HTTP_200_OK)
