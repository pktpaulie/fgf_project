from auth_app.models import Contributor, User
from business_logic.system_users._user import User as UserFacade
from auth_app.serializers import (CreateContributorSerializer, ContributorSerializer, ContributorLoginSerializer)
from core.mixins import view_mixins
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.views.decorators.http import require_http_methods

# Create your views here.
class CreateContributorViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Contributor.objects.all()
    serializer_class = CreateContributorSerializer
    lookup_field = 'id'

    @require_http_methods(["GET", "POST"])
    def create(self, validated_data):
        # Create and return a new user instance using the validated data
        user = User.objects.create(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])  # Hash and set the password
        #user.save()
       
        _request = self.context['request']
        request = {'request':_request, 'validated_data':validated_data}
        #return user
        return UserFacade().register_contributor(request)

    # def post(self, request):
    #     try:
    #         return self.create(request)
    #     except Exception as exception:
    #         raise exception


class ViewContributorsListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    lookup_field = 'id'
    #filter_backends = [filters.SearchFilter]
    search_fields = ['user']


class RetrieveContributorViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    lookup_field = 'id'


class UpdateContributorViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    # Permission_classes = [HasUsergroup, IsContributor]
    lookup_field = 'id'


class DeleteContributorViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception


class ContributorLoginView(generics.GenericAPIView):
    serializer_class = ContributorLoginSerializer
    permission_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            data = serializer.validated_data
            # print(data)
            return Response(data=data, status=status.HTTP_200_OK)