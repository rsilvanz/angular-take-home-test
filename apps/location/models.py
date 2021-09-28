from django.db import models

# Create your models here.


class EquipmentLocationCategory(models.Model):
    """ A Category node from choices for equipment location types. """
    name = models.CharField(max_length=50)


class EquipmentManual(models.Model):
    """ A Document Relating to Equipment. """
    file_name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)


class EquipmentLocation(models.Model):
    """ A location node in a tree of production machinery equipment. """

    parent_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=90, blank=True, null=True)
    type = models.ForeignKey('EquipmentLocationCategory', models.DO_NOTHING, blank=True, null=True)
    order = models.IntegerField()
    site = models.ForeignKey(
        'EquipmentLocation',
        models.DO_NOTHING,
        related_name='location_site',
        help_text="The site is the top most ancestor in the location tree. Eg. Auckland"
    )
    part_number = models.CharField(max_length=80, blank=True, null=True, default=None)
    manual = models.ForeignKey('EquipmentManual', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        unique_together = (('id', 'site'),)

    @property
    def location_path(self): pass  # TODO: replace this stub with your answer.

    @property
    def number_of_machines(self): pass  # TODO: replace this stub with your answer.
