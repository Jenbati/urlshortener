from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone
from .models import ShortURL
from .utils import encode_base62

@login_required
def dashboard(request):
    urls = ShortURL.objects.filter(user=request.user)
    return render(request, 'shortener/dashboard.html', {'urls': urls})

@login_required
def create_short_url(request):
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        s_code = encode_base62()
        ShortURL.objects.create(user=request.user, original_url = original_url, short_code = s_code)
        return redirect('dashboard')
    return render(request, 'shortener/create.html')

@login_required
def delete_url(request, id):
    url = get_object_or_404(ShortURL, id=id, user=request.user)
    url.delete()
    return redirect('dashboard')

def redirect_url(request, code):
    url = get_object_or_404(ShortURL, short_code=code)

    if url.is_expired():
        return HttpResponse("This link has expired", status=410)

    url.click_count += 1
    url.save()

    return redirect(url.original_url)