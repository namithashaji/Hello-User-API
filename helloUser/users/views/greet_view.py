from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from dataclasses import asdict
from ..dataclass.response import GreetUserResponse
from ..services import greet_user
from ..exceptions import UserNotFoundError, DatabaseError
from ..utils import error_response


class GreetView(APIView):
    def get(self, request, user_id):
        try:
            # Generate the response object
            response_data = GreetUserResponse(
                greet_name=greet_user(user_id)
            )

            # Convert the dataclass to a dictionary before returning
            return Response(asdict(response_data), status=status.HTTP_200_OK)

        except UserNotFoundError as e:
            return Response(error_response(
                error=str(e),
                message="User not found"
            ), status=status.HTTP_404_NOT_FOUND)

        except DatabaseError as e:
            return Response(error_response(
                error=str(e),
                message="Failed to retrieve user due to a database error"
            ), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
