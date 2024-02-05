from django.shortcuts import render


# Create your views here.
def insertapplicationDetails(request):
    return render(request,"'Application_Details'.html")

def insertCertificaterequest(request):
    return render(request,"'Certificate_request'.html")