from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

import datetime
import platform
from ..utils import check_database


class HealthCheckView(APIView):
    renderer_classes = [JSONRenderer]  # Force JSON rendering for this view

    start_time = datetime.datetime.now()

    def get(self, request):
        uptime = datetime.datetime.now() - self.start_time
        db_status = check_database()

        health_status = {
            "server_status": "Server is running",
            "uptime": str(uptime),
            "server_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "architecture": platform.architecture()[0],
            "python_version": platform.python_version(),
            "database": db_status,
        }

        return Response(data=health_status, status=status.HTTP_200_OK)
