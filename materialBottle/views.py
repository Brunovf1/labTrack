from material.frontend.views import ModelViewSet

from . import models


class SampleViewSet(ModelViewSet):
   model = models.Sample


class BatchViewSet(ModelViewSet):
    model = models.Batch
