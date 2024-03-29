# """Model MixIns
# """

from django.db import models
from django.utils import timezone
from django.conf import settings


class Registrable(models.Model):
    """
    Base class for all Models with no direct attachment with any of the system users.
    """

    registered_at = models.DateTimeField(default=timezone.now)
    registered_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Created by',
        blank=True, null=True,
        related_name="%(app_label)s_%(class)s_created",
        on_delete=models.SET_NULL
    )
    lastupdated_at = models.DateTimeField(default=timezone.now)
    lastupdated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Last modified by',
        blank=True, null=True,
        related_name="%(app_label)s_%(class)s_lastmodified",
        on_delete=models.SET_NULL
    )

    class Meta:
        abstract = True
        ordering = ['-lastupdated_at']
    # End class Meta


class BaseModel(models.Model):
    """
    Base class for all Models with no direct attachment with any of the system users.
    """

    # created_by = models.ForeignKey(
    #     User, verbose_name="Created by", null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Created by',
        blank=True, null=True,
        related_name="%(app_label)s_%(class)s_created",
        on_delete=models.SET_NULL
    )
    lastupdated_at = models.DateTimeField(default=timezone.now)
    lastupdated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Last modified by',
        blank=True, null=True,
        related_name="%(app_label)s_%(class)s_lastmodified",
        on_delete=models.SET_NULL
    )

    class Meta:
        abstract = True
        ordering = ['-lastupdated_at']
    # End class Meta



# import uuid
# from django.db import models
# from django.utils import timezone
# from django.conf import settings


# class BaseModel(models.Model):
#     class Meta:
#         abstract = True

#     pass

# class UserRegistrarModelMixin(BaseModel):

#     registered_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         verbose_name='Created by',
#         blank=True, null=True,
#         related_name="%(class)s_created",
#         on_delete=models.SET_NULL
#     )


# class UserRegistrationDateAndTimeModelMixin(BaseModel):

#     registered_at = models.DateTimeField(default=timezone.now)


# class ResourceCreatorMixin(BaseModel):

#     created_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         verbose_name='Created by',
#         blank=True, null=True,
#         related_name="%(class)s_created",
#         on_delete=models.SET_NULL
#     )


# class ResourceCreationDateAndTimeMixin(BaseModel):

#     created_at = models.DateTimeField(default=timezone.now)


# class ResourceUpdaterMixin(BaseModel):

#     lastupdated_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         verbose_name='Last modified by',
#         blank=True, null=True,
#         related_name="%(class)s_lastmodified",
#         on_delete=models.SET_NULL
#     )


# class ResourceUpdateDateAndTimeMixin(BaseModel):

#     lastupdated_at = models.DateTimeField(default=timezone.now)


# class Model(ResourceCreatorMixin, ResourceCreationDateAndTimeMixin, ResourceUpdaterMixin, ResourceUpdateDateAndTimeMixin):
#     """
#     Base class for all Models with no direct attachment with any of the system users.
#     """
#     # created_at = models.DateTimeField(default=timezone.now)
#     # created_by = models.ForeignKey(
#     #     settings.AUTH_USER_MODEL,
#     #     verbose_name='Created by',
#     #     blank=True, null=True,
#     #     related_name="%(app_label)s_%(class)s_created",
#     #     on_delete=models.SET_NULL
#     # )
#     # lastupdated_at = models.DateTimeField(default=timezone.now)
#     # lastupdated_by = models.ForeignKey(
#     #     settings.AUTH_USER_MODEL,
#     #     verbose_name='Last modified by',
#     #     blank=True, null=True,
#     #     related_name="%(app_label)s_%(class)s_lastmodified",
#     #     on_delete=models.SET_NULL
#     # )

#     class Meta:
#         abstract = True
#         ordering = ['-lastupdated_at']
#     # End class Meta
