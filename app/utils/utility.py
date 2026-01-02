from rest_framework.response import Response
from rest_framework import status
from .custom_exceptions import APIError


def success_response(key, data, status_code=status.HTTP_200_OK):
    return Response({
        'error': False,
        'data': {
            key: data
        }
    }, status=status_code)
    
def success_response_msg(msg, status_code=status.HTTP_200_OK):
    return Response({
        'error': False,
        'msg':msg
    }, status=status_code)

class SuccessResponseMixin:
    success_key = None  # override this in child viewsets
    datakey = "item"

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return success_response(self.datakey, response.data)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return success_response(self.datakey, response.data)
    
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return success_response_msg(f'{self.get_success_key().title()} added successfully.',status.HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return success_response_msg(f'{self.get_success_key().title()} deleted successfully.')
    
    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return success_response_msg(f'{self.get_success_key().title()} updated successfully.')

    def get_success_key(self):
        return self.success_key
    
    
class CustomGetObjectMixin:
    success_key = None 
    
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        lookup_value = self.kwargs.get(lookup_url_kwarg)

        try:
            return queryset.get(**{self.lookup_field: lookup_value})
        except queryset.model.DoesNotExist:
            name = self.success_key

            raise APIError(f"{name.title()} not found.",status.HTTP_404_NOT_FOUND)
           
