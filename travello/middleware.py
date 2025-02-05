from django.core.cache import cache
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.deprecation import MiddlewareMixin
from .views import get_client_ip

class TrackUnauthenticatedViewsMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if view_func.__name__ == 'details':
            if not request.user.is_authenticated:
                ip = get_client_ip(request)
                viewed_destinations = cache.get(ip, [])
                destination_id = view_kwargs.get('id')
                
                if destination_id and destination_id not in viewed_destinations:
                    viewed_destinations.append(destination_id)
                    cache.set(ip, viewed_destinations, timeout=3600)
                
                if len(viewed_destinations) > 2:
                    messages.info(request, 'Please register to view more destination details.')
                    return redirect('register')

        return None
