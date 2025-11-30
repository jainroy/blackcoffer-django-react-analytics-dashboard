from django.db import models


class InsightEntry(models.Model):
    """
    Model representing a single entry from the JSON data.
    Adjust field names/types to match your jsondata.json structure.
    Common fields used in popular public datasets:
    - intensity, relevance, likelihood: numeric
    - start_year, end_year, year: integer-ish
    - country, region, city, topic, sector, pestle, source, swot: text
    - published, added: dates or datetimes
    """
    # Numeric fields
    intensity = models.IntegerField(null=True, blank=True)
    relevance = models.IntegerField(null=True, blank=True)
    likelihood = models.IntegerField(null=True, blank=True)

    # Year fields (start/end range, and maybe overall year)
    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

    # Categorical / text fields
    topic = models.CharField(max_length=255, null=True, blank=True)
    sector = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    pestle = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    swot = models.CharField(max_length=255, null=True, blank=True)

    # Descriptive fields
    title = models.CharField(max_length=500, null=True, blank=True)
    insight = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    # Date / datetime fields
    published = models.DateField(null=True, blank=True)  # store as Date for charts
    added = models.DateTimeField(null=True, blank=True)  # raw timestamp if available

    # Extra raw JSON storage (optional)
    raw_data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.title or f'InsightEntry #{self.pk}'
