from django.db import models
from .models import DataSource


class VerticaDataSource(DataSource):
    data_source = models.OneToOneField(DataSource)
    host = models.CharField('Host', max_length=255)
    port = models.CharField('Port', max_length=255)
    username = models.CharField('Username', max_length=255)
    password = models.CharField('Password', max_length=255)
    database = models.CharField('Database', max_length=255)
    schema_name = models.CharField('Schema name', max_length=255)

    class Meta:
        verbose_name = 'Vertica Data source'
        verbose_name_plural = 'Vertica Data sources'

    def create_config_file(self):
        pass

    def update_config_file(self):
        pass

