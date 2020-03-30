from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.views.generic import FormView, TemplateView
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from .models import Listing, Post, Profile
from .forms import ListingForm, User, UserForm, ProfileForm, PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django.db.models import F
# Create your views here.
def index(request):
    return render(request,"welcome.html")
    
def create_listing(request):
    print('Should come')
    if request.method == 'POST':
        print('Method is post')
        form = ListingForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            print('Cool')
            form.save()
            #form.save_m2m() commented because it kept crashing and idk what it does
            return redirect('/s/')
    else:
        print('Form is not valid')
        form = ListingForm()
    return render(request, 'create_listing.html', {'form': form})

def save_listing(request):
    form = CreateListingForm(request.POST)
    if form.is_valid():
        title = request.POST['title']
        category = request.POST['category']
        condition = request.POST['category']
        price = request.POST['price']
        description = request.POST['description']
        location = request.POST['location']
        images = request.POST['images']
        acct = request.POST['acct']
        listing_id = request.POST['listing_id']
        print('JAJAJAJA', listing_id)

        new_listing = CreateListing(title=title, category=category, condition=condition, price=price, description=description, images=images, acct=acct, listing_id=listing_id, location=location)
        new_listing.save()
    args = {'title':title, 'category':category, 'condition':condition, 'price':price, 'description':description, 'images':images, 'acct':acct, 'listing_id':listing_id, 'location':location}
    return render(request, 'create_listing.html',{'message': "Success! Your posting has been submitted!"}, args)

def mark_sold(request, user, id):
    if request.method == 'POST':
        Listing.objects.get(listing_id= id).delete()
        return redirect('/s/')

class ItemList(generic.ListView):
    template_name = "itemlist.html"
    context_object_name = "itemlist"

    def get_queryset(self):
        cleared = self.request.GET.get('clear','0')
        if cleared == '1':
            return Listing.objects.all()       
        contains = self.request.GET.get('contains','')
        output = Listing.objects.all().filter(title__icontains=contains)
        minPrice = self.request.GET.get('min-price','0') or 0
        output = output.filter(price__gte=float(minPrice))
        maxPrice = self.request.GET.get('max-price','-1') or '-1'
        if maxPrice != '-1':
            output = output.filter(price__lte=float(maxPrice))
        category = self.request.GET.get('category','ANY')
        if category != 'ANY':
            output = output.filter(category=category)
        condition = self.request.GET.get('condition','ANY')
        if condition != 'ANY':
            output = output.filter(condition=condition)
        location = self.request.GET.get('location','ANY')
        if location != 'ANY':
            output = output.filter(location=location)
        reverse = reversed(list(output))
        return reverse

class ListingView(generic.TemplateView):
    template_name = "listing.html"
    context_object_name = "listingview"

    def get_context_data(self, **kwargs):
        data = {}
        data['listing'] = Listing.objects.get(listing_id=kwargs['id'])
        return data

class LoginView(generic.TemplateView):
    template_name = "login.html"

class LogoutView(generic.TemplateView):
    template_name = "base.html"

class ProfileView(generic.ListView):
    template_name = "profile.html"
    context_object_name = "listings"

    def get_queryset(self):
        user = self.request.path.replace('/', '').replace('profile', '')
        print(user)
        return Listing.objects.filter(acct=user)

class LocationView(generic.TemplateView):
    template_name = "locations.html"

class ForeignProfileView(generic.ListView): # For viewing other users' profile pages
    template_name = "foreign_profile.html"
    context_object_name = "listings"

    def get(self, *args, **kwargs):
        user = self.request.path.replace('/', '').strip()
        good = False
        for u in Profile.objects.all():
            if u.user.username == user:
                good = True
                break
        if not good:
            return redirect("404.html")
        else:
            return super(ForeignProfileView, self).get(*args, **kwargs)
    
    def get_queryset(self):
        user = self.request.path.replace('/', '')
        return Listing.objects.filter(acct=user)

def Logout(request):
    auth_logout(request)
    return redirect("base.html")

def redirect_view(request):
    response = redirect('/redirect-success/')
    return response


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

#    return render(request, 'profile.html', context)
    args = {'user_form': user_form,'profile_form': profile_form}
    return render(request, 'craigslist/profile.html', args)
