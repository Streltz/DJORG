from django.db import models

class Bookmark(models.Model):
    id = models.UUIDField(primary_key = TRUE, default = uuid4, editable = FALSE)
    url = models.URLField('URL', unique = TRUE)
    name = models.CharField(max_length = 200)
    notes = models.TextField(blank = TRUE)
