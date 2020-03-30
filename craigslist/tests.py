
from django.urls import resolve
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from craigslist.forms import ListingForm
from craigslist.models import Listing
from craigslist.views import index, create_listing, LogoutView, ItemList, LocationView, ForeignProfileView
from django.core.files.uploadedfile import SimpleUploadedFile
from craigslist.forms import CONDITIONS 
from craigslist.forms import CATEGORIES
from craigslist.forms import LOCATIONS
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import pytz
import datetime


class ViewTests(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, index) 
    def test_create_listing_url_resolves_to_create_listing_view(self):
        found = resolve('/create_listing/')  
        self.assertEqual(found.func, create_listing) 
    def setUp(self):
        self.user = User.objects.create_superuser(
            'admin',
            'admin@admin.com',
            'password'
        )
    @staticmethod
    def get_image_file(name='test.png', ext='png', size=(50, 50), color=(256, 0, 0)):
        file_obj = StringIO()
        image = Image.new("RGBA", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)
    def test_create_form(self): 
        self.client.login(username='admin', password='password')
        im = Image.new(mode='RGB', size=(200, 200)) # create a new image using PIL
        im_io = BytesIO() # a BytesIO object for saving image
        im.save(im_io, 'JPEG') # save the image to im_io
        im_io.seek(0) # seek to the beginning

        image = InMemoryUploadedFile(
            im_io, None, 'random-name.jpg', 'image/jpeg', len(im_io.getvalue()), None
        )
        file_dict = {'images': image}
        form_data = { 
            'acct': 'admin',
            'listing_id': 100000,
            'title': 'car',
            'price': 42000,
            'description': 'this is a car',
            'category': CATEGORIES[0][0],
            'condition': CONDITIONS[0][0],
            'location': LOCATIONS[0][0]
        } 
        form = ListingForm(files = file_dict, data=form_data)
        self.assertTrue(form.is_valid())
        response = self.client.post('/create_listing/', form_data)

#class ListingModelTests(TestCase):
#    def test_listing_was_posted_recently_with_new_question(self):
#        l1 = Listing()
#        l1.save()
#        self.assertIs(l1.posted_recently(), True)

#    def test_listing_was_posted_recently_with_old_question(self):
#        time = timezone.now() + datetime.timedelta(days=10)
#        l1 = Listing()
#        l1.save()
#        l1.posted = time
#        self.assertIs(l1.posted_recently(), False)

