from django.shortcuts import render


def handler400(request, exception):
    """handler exception when error 400 case"""
    return render(request, "errors/400.html")


def handler403(request, exception):
    """handler exception when error 403 case"""
    return render(request, "errors/403.html")


def handler404(request, exception):
    """handler exception when error 404 case"""
    return render(request, "errors/404.html")


def handler500(request):
    """handler exception when error 500 case"""
    return render(request, "errors/500.html")