from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Facteon Django Take Home Test",
        default_version=f'1.0.0',
        description="Simple Web Development Exercise",
        contact=openapi.Contact(email=settings.ADMIN),
    ),
)
