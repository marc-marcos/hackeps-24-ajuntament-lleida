from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Parking, Planta, Plaza, PlazaLog
from .serializers import (
    ParkingSerializer,
    PlantaSerializer,
    PlazaSerializer,
    PlazaLogSerializer,
)


class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer

    @action(detail=True, methods=["get"])
    def plantas(self, request, pk=None):
        parking = self.get_object()
        plantas = Planta.objects.filter(parking=parking)
        serializer = PlantaSerializer(plantas, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def plazas(self, request, pk=None):
        # Get the Parking object
        parking = self.get_object()

        # Get all Plazas via Planta
        plazas = Plaza.objects.filter(planta__parking=parking)

        # Serialize the Plaza instances
        serializer = PlazaSerializer(plazas, many=True)
        return Response(serializer.data)


class PlantaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """

    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer

    @action(detail=True, methods=["get"])
    def plazas(self, request, pk=None):
        planta = self.get_object()
        plazas = Plaza.objects.filter(planta=planta)
        serializer = PlazaSerializer(plazas, many=True)
        return Response(serializer.data)


class PlazaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """

    queryset = Plaza.objects.all()
    serializer_class = PlazaSerializer


class PlazaLogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """

    queryset = PlazaLog.objects.all()
    serializer_class = PlazaLogSerializer


class ParkingStatusView(APIView):
    def get(self, request):
        # Get the 'parking_id' parameter from the query string (if provided)
        parking_id = request.query_params.get("parking_id", None)

        if parking_id:
            # Filter by the specific parking
            total_spots = Plaza.objects.filter(planta__parking=parking_id).count()
            occupied_spots = Plaza.objects.filter(
                planta__parking=parking_id, ocupada=True
            ).count()
        else:
            # Calculate for all parkings if no parameter is provided
            total_spots = Plaza.objects.count()
            occupied_spots = Plaza.objects.filter(ocupada=True).count()

        free_spots = total_spots - occupied_spots

        # Return the response as JSON
        return Response(
            {
                "total_spots": total_spots,
                "occupied_spots": occupied_spots,
                "free_spots": free_spots,
            }
        )
