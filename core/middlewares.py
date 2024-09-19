
from django.shortcuts import render


class SiteUnderConstruction:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        print("Before View")
        reponse = render(request, 'core/siteunserconstruction.html')
        print("After View")
        return reponse
        