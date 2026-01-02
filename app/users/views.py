
from rest_framework import generics

from utils.utility import SuccessResponseMixin
from .models import User
from .serializers import UserSerializer

class UserListCreateView(SuccessResponseMixin, generics.ListCreateAPIView):
    datakey = "users"
    success_key = "user"
    queryset = User.objects.all()
    serializer_class = UserSerializer