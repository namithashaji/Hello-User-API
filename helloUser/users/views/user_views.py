from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers.requests import CreateUserSerializer, UpdateUserSerializer
from ..serializers.response import UserDetailsSerializer
from ..dataclass.request import CreateUserRequest, UpdateUserRequest
from ..dataclass.response import UserDetailsResponse

from ..services import create_user, update_user, delete_user, get_user_by_id
from ..utils import success_response, error_response
from ..exceptions import UserNotFoundError, DuplicateUserError, DatabaseError


class UserViews(APIView):
    # POST: Create a user
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Use dataclass for structured data
                user_data = CreateUserRequest(**serializer.validated_data)

                # Call the service layer to create a user
                user = create_user(user_data)

                # Prepare response using dataclass
                user_response = UserDetailsResponse(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    age=user.age
                )

                return Response(success_response(
                    data=UserDetailsSerializer(user_response).data,
                    message="User created successfully"
                ), status=status.HTTP_201_CREATED)

            except DuplicateUserError as e:
                return Response(error_response(
                    error=str(e),
                    message="Duplicate user detected"
                ), status=status.HTTP_400_BAD_REQUEST)

            except DatabaseError as e:
                return Response(error_response(
                    error=str(e),
                    message="Failed to create user due to a database error"
                ), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(error_response(
            error=serializer.errors,
            message="Validation failed"
        ), status=status.HTTP_400_BAD_REQUEST)

    # GET: Retrieve a user by ID
    def get(self, request, user_id):
        try:
            # Call the service layer to get the user by ID
            user = get_user_by_id(user_id)

            # Prepare response using dataclass
            user_response = UserDetailsResponse(
                id=user.id,
                name=user.name,
                email=user.email,
                age=user.age
            )

            return Response(success_response(
                data=UserDetailsSerializer(user_response).data,
                message="User retrieved successfully"
            ), status=status.HTTP_200_OK)

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

    # PUT: Update a user by ID
    def put(self, request, user_id):
        serializer = UpdateUserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Use dataclass for structured data
                user_data = UpdateUserRequest(**serializer.validated_data)

                # Call the service layer to update the user
                user = update_user(user_id, user_data)

                # Prepare response using dataclass
                user_response = UserDetailsResponse(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    age=user.age
                )

                return Response(success_response(
                    data=UserDetailsSerializer(user_response).data,
                    message="User updated successfully"
                ), status=status.HTTP_200_OK)

            except UserNotFoundError as e:
                return Response(error_response(
                    error=str(e),
                    message="User not found"
                ), status=status.HTTP_404_NOT_FOUND)

            except DatabaseError as e:
                return Response(error_response(
                    error=str(e),
                    message="Failed to update user due to a database error"
                ), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(error_response(
            error=serializer.errors,
            message="Validation failed"
        ), status=status.HTTP_400_BAD_REQUEST)

    # DELETE: Delete a user by ID
    def delete(self, request, user_id):
        try:
            # Call the service layer to delete the user
            delete_user(user_id)

            return Response(success_response(
                message="User deleted successfully"
            ), status=status.HTTP_200_OK)

        except UserNotFoundError as e:
            return Response(error_response(
                error=str(e),
                message="User not found"
            ), status=status.HTTP_404_NOT_FOUND)

        except DatabaseError as e:
            return Response(error_response(
                error=str(e),
                message="Failed to delete user due to a database error"
            ), status=status.HTTP_500_INTERNAL_SERVER_ERROR)




