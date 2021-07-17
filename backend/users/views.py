from rest_framework import generics
from users.models import UserAccount
from users.permissions import IsUser, IsSuperuser
from users.serializers import UserSerializer

# Create your views here.
class UserDetailsView(generics.RetrieveAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperuser | IsUser]