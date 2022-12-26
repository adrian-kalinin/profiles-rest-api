from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from examples import serializers


class HelloApiView(APIView):
    """Simple APIView example"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a hello message and a list of APIView features"""
        apiview_features = [
            "Uses HTTP methods as functions (get, post, patch, put, delete)",
            "Is similar to a traditional Django View",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs",
        ]

        return Response({"message": "Hello!", "apiview_features": apiview_features})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello, {name}!"
            return Response({"message": message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Update an object"""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """Partially update of an object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """Simple ViewSet example"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message and a list of ViewSet features"""
        viewset_features = [
            "Uses actions list, retrieve, create, update, partial_update, delete",
            "Automatically maps to URLs using Routers",
            "Provides more functionality with less code",
        ]

        return Response({"message": "Hello!", "viewset_features": viewset_features})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello, {name}!"
            return Response({"message": message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrieve an object by its ID"""
        return Response({"method": "GET"})

    def put(self, request, pk=None):
        """Update an object by its ID"""
        return Response({"method": "PUT"})

    def partial_update(self, request, pk=None):
        """Partially update an object by its ID"""
        return Response({"method": "PATCH"})

    def destroy(self, request, pk=None):
        """Delete an object by its ID"""
        return Response({"method": "DELETE"})
