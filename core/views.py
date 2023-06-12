from django.shortcuts import render


def homepage(request):
    """Display the home page"""
    return render(request, "home.html")


def handler400(request, exception):
    """handler exception when error 400 case: bad_request"""
    return render(request, "errors/400.html", status=400)


def handler403(request, exception):
    """handler exception when error 403 case: custom_permission_denied"""
    return render(request, "errors/403.html", status=403)


def handler404(request, exception):
    """handler exception when error 404 case: page_not_found"""
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """handler exception when error 500 case: error_view"""
    return render(request, "errors/500.html", status=500)
