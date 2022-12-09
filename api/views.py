from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Link
from api.serializers import LinkSerializer


class LinkApiView(APIView):
    def get(self, request, *args, **kwargs):
        links = Link.objects
        serializer = LinkSerializer(links, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'url': request.data.get('url'),
        }
        serializer = LinkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LinkDetailApiView(APIView):
    def get(self, request, pk):
        link = Link.objects.get(pk=pk)
        if link:
            serializer = LinkSerializer(link)
            return Response(status=200, data=serializer.data)
        return Response(status=400, data={'Destination Not Found'})


@api_view(['POST'])
def upvote(request, pk):
    link = Link.objects.get(pk=pk)
    if link:
        link.upvote()
        serializer = LinkSerializer(link)
        return Response(status=200, data=serializer.data)
    return Response(status=400, data={'Destination Not Found'})


@api_view(['POST'])
def downvote(request, pk):
    link = Link.objects.get(pk=pk)
    if link:
        link.downvote()
        serializer = LinkSerializer(link)
        return Response(status=200, data=serializer.data)
    return Response(status=400, data={'Destination Not Found'})
