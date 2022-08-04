from django.shortcuts import render


def handler404(request, exception):
    """Error handler for 404 responses"""
    return render(request, 'errors/404.html', status=404)
