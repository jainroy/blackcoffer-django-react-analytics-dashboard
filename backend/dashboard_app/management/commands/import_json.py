import json
from datetime import datetime
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from dashboard_app.models import InsightEntry


class Command(BaseCommand):
    """
    Usage:
      python manage.py import_json --file path/to/jsondata.json

    This command reads the JSON file and creates InsightEntry records.
    It is idempotent only if you clear the table first or ensure unique constraints.
    """
    help = 'Import entries from a JSON file into InsightEntry model.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            required=True,
            help='Path to jsondata.json',
        )

    def handle(self, *args, **options):
        file_path = options['file']
        path = Path(file_path)

        if not path.exists():
            raise CommandError(f'File not found: {file_path}')

        self.stdout.write(self.style.NOTICE(f'Reading JSON file: {file_path}'))

        with path.open('r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                raise CommandError(f'Invalid JSON: {e}')

        if not isinstance(data, list):
            raise CommandError('Expected a list of objects at the root of JSON')

        created = 0
        for item in data:
            # Defensive access: use dict.get with defaults
            intensity = parse_int(item.get('intensity'))
            relevance = parse_int(item.get('relevance'))
            likelihood = parse_int(item.get('likelihood'))

            start_year = parse_int(item.get('start_year'))
            end_year = parse_int(item.get('end_year'))
            year = parse_int(item.get('year'))

            # Strings (empty string becomes None)
            topic = normalize_str(item.get('topic'))
            sector = normalize_str(item.get('sector'))
            region = normalize_str(item.get('region'))
            country = normalize_str(item.get('country'))
            city = normalize_str(item.get('city'))
            pestle = normalize_str(item.get('pestle'))
            source = normalize_str(item.get('source'))
            swot = normalize_str(item.get('swot'))

            title = normalize_str(item.get('title'))
            insight = normalize_str(item.get('insight'))
            url = normalize_str(item.get('url'))

            published = parse_date(item.get('published'))
            added = parse_datetime(item.get('added'))

            entry = InsightEntry(
                intensity=intensity,
                relevance=relevance,
                likelihood=likelihood,
                start_year=start_year,
                end_year=end_year,
                year=year,
                topic=topic,
                sector=sector,
                region=region,
                country=country,
                city=city,
                pestle=pestle,
                source=source,
                swot=swot,
                title=title,
                insight=insight,
                url=url,
                published=published,
                added=added,
                raw_data=item,
            )
            entry.save()
            created += 1

        self.stdout.write(self.style.SUCCESS(f'Imported {created} entries.'))


def normalize_str(value):
    """
    Convert empty strings or whitespace-only strings to None.
    """
    if value is None:
        return None
    if isinstance(value, str):
        val = value.strip()
        return val or None
    return str(value)


def parse_int(value):
    """
    Safely parse integers; return None if invalid or empty.
    """
    if value in (None, '', 'null'):
        return None
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def parse_date(value):
    """
    Try to parse dates as YYYY-MM-DD or similar formats.
    Returns a date object or None if parsing fails.
    """
    if not value:
        return None

    # Try a few common formats
    for fmt in ('%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d', '%Y-%m-%dT%H:%M:%S'):
        try:
            dt = datetime.strptime(str(value), fmt)
            return dt.date()
        except ValueError:
            continue
    return None


def parse_datetime(value):
    """
    Try to parse datetime strings.
    Returns a datetime object or None.
    """
    if not value:
        return None

    for fmt in (
        '%Y-%m-%dT%H:%M:%S',
        '%Y-%m-%d %H:%M:%S',
        '%Y-%m-%dT%H:%M:%S.%fZ',
    ):
        try:
            return datetime.strptime(str(value), fmt)
        except ValueError:
            continue
    return None
