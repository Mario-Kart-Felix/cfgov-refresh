import traceback

from django.http import HttpRequest
from django.contrib.messages.api import MessageFailure
from django.contrib.auth import authenticate
from django.core.exceptions import PermissionDenied, ValidationError

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.views import pages as pages_views
from wagtail.wagtailsnippets.views import snippets as snippets_views


class DataImporter:
    def __init__(self, *args, **kwargs):
        self.data_type = kwargs.get('data_type')
        self.wagtail_type = kwargs.get('wagtail_type')
        self.parent = kwargs.get('parent')
        self.snippet = kwargs.get('snippet')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.app = kwargs.get('app', 'v1')
        self.overwrite = kwargs.get('overwrite')
        self.verbosity = kwargs.get('verbosity')
        self.results = {
            'migrated': 0,
            'overwritten': 0,
            'existed': 0,
            'errors': 0,
            'migrated_slugs': [],
            'overwritten_slugs': [],
            'existed_slugs': [],
            'errors_slugs': [],
        }

    def migrate(self, imported_data, converter):

        # Create the request object then pass it an authenticated user.
        request = HttpRequest()
        request.user = self.authenticate_user()

        if self.snippet:
            self.migrate_snippet(request, imported_data, converter)
        else:
            self.migrate_page(request, imported_data, converter)

    def authenticate_user(self):
        user = authenticate(username=self.username, password=self.password)
        if user:
            if not user.is_active or not user.is_superuser:
                raise PermissionDenied('This user does not have permissions to'
                                       + 'perform this operation.')
        else:
            raise ValidationError('The username and password were incorrect.')

        return user

    def migrate_snippet(self, request, imported_data, converter):
        existing = converter.get_existing_snippet(imported_data)

        if existing and not self.overwrite:
            self.results['existed'] += 1
            self.results['existed_slugs'].append(imported_data.get('slug'))
            return

        # Convert the imported data into Wagtail readable data then save it.
        request.POST = converter.convert(imported_data)
        request.POST['save'] = u'Save'

        # Create the snippet or overwrite the existing one. Since we aren't
        # hitting the middleware we have to catch the MessageFailure exception.
        try:
            if self.overwrite and existing:
                snippets_views.edit(request, existing.id)
            else:
                snippets_views.create(request, self.app, self.wagtail_type)
        except MessageFailure:
            self.is_valid(existing, imported_data)

    def migrate_page(self, request, imported_data, converter):
        try:
            existing = Page.objects.get(slug=imported_data.get('slug'))
        except Page.DoesNotExist:
            existing = None

        if existing and not self.overwrite:
            self.results['existed'] += 1
            self.results['existed_slugs'].append(imported_data.get('slug'))
            return

        # Get parent. If parent doesn't exist, then raise Page.DoesNotExist
        try:
            parent_page = Page.objects.get(slug=self.parent)
        except:
            raise Page.DoesNotExist('Parent page does not exist')

        # Convert the imported data into Wagtail readable data then publish it.
        request.POST = converter.convert(imported_data)
        request.POST['action-publish'] = u'Publish on WWW'

        # Create the page or overwrite the existing one. Since we aren't
        # hitting the middleware we have to catch the MessageFailure exception.
        try:
            if self.overwrite and existing:
                pages_views.edit(request, existing.id)
            else:
                pages_views.create(request, self.app, self.wagtail_type,
                                   parent_page.id)
        except MessageFailure:
            self.is_valid(existing, imported_data)

    # Because the middleware isn't being used, we have to catch the
    # MessageFailure and analyze the actual traceback to see if it was a
    # success or failure.
    def is_valid(self, existing, imported_data):
        if 'messages.error' in traceback.format_exc():
            self.results['errors'] += 1
            self.results['errors_slugs'].append(imported_data.get('slug'))
        elif existing and self.overwrite:
            self.results['overwritten'] += 1
            self.results['overwritten_slugs'].append(imported_data.get('slug'))
        else:
            self.results['migrated'] += 1
            self.results['migrated_slugs'].append(imported_data.get('slug'))

    def print_results(self):
        for state in ['migrated', 'overwritten', 'existed', 'errors']:
            print '%s %s' % (self.results[state], state)
            if self.verbosity > 1:
                for slug in self.results[state + '_slugs']:
                    print slug


class PageDataConverter:
    def convert(self, imported_data):
        raise NotImplementedError()


class SnippetDataConverter(PageDataConverter):
    def get_existing_snippet(self, imported_data):
        raise NotImplementedError()
