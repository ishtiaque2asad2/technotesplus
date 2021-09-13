# Create your models here.
import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.encoding import smart_text


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True,
                                   blank=True, related_name='created_by_%(class)ss')
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True,
                                   blank=True, related_name='updated_by_%(class)ss')

    class Meta:
        abstract = True


class Tag(BaseModel):
    name = models.CharField(max_length=255)

    # Meta class that sets the ordering and other stuffs
    class Meta:
        ordering = ['-created']
        verbose_name = 'Tag'
        db_table = 'tag'
        verbose_name_plural = 'Tags'

    # A human friendly name, provide that will give good explanation
    def __str__(self):
        return smart_text(self.name)


class Note(BaseModel):
    title = models.CharField(max_length=255)
    unique_id = models.CharField(default=uuid.uuid4, max_length=255)
    note = models.TextField()
    tags = models.ManyToManyField('Tag')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Note'
        db_table = 'note'
        verbose_name_plural = 'Notes'

    # A human friendly name, provide that will give good explanation
    def __str__(self):
        return smart_text(self.title)


class SharedNote(BaseModel):
    shared_with = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL,
                                    related_name='sharednote_shared_with')
    is_read = models.BooleanField(default=False)
    read_datetime = models.DateTimeField(null=True, blank=True)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']
        verbose_name = 'SharedNote'
        db_table = 'shared_note'
        verbose_name_plural = 'SharedNotes'

    # A human friendly name, provide that will give good explanation
    def __str__(self):
        return smart_text(self.pk)
