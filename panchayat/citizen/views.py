from django.shortcuts import render

from citizen.models import ApplicationDetails

from citizen.models import CertificateRequest
from citizen.models import Schemes
from citizen.models import Complaints
from citizen.models import CitizenDetails
from citizen.models import CertificateDetails



# Create your views here.

# create user login page


def insertapplicationDetails(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        ApplicationDetails.objects.create(Application_id=s1, Application_type=s2, Aadhar_no=s3, Name=s4, Details=s5,
                                          Date=s6, Time=s7, Status=s8)

        return render(request, "'Application_Details'.html")
    return render(request, "'Application_Details'.html")


def insertCertificaterequest(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")

        CertificateRequest.objects.create(Request_id=s1, Scheme_id=s2, Aadhar_no=s3, Apply_date=s4, Status=s5)

        return render(request, "'Certificate_request'.html")

    return render(request, "'Certificate_request'.html")


def insertCertificateDetails(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s9 = request.POST.get("t9")
        s8 = request.POST.get("t8")
        s10 = request.POST.get("t10")
        s11 = request.POST.get("t11")
        CertificateDetails.objects.create(Request_id=s1, Certificate_no=s2, Type=s3, Issue_Date=s4, Name=s5,
                                          Father_Name=s6, Mother_Name=s7, Reason=s8,Date=s9, time=s10, status=s11)

        return render(request, "'CertificateDetails'.html")
    return render(request, "'CertificateDetails'.html")


def insertCitizenDetails(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s9 = request.POST.get("t9")
        s10 = request.POST.get("t10")
        CitizenDetails.objects.create(Aadhar_no=s1, First_name=s2, Last_name=s3, Father_name=s4, Mother_name=s5,
                                      DateOfBirth=s6, Gender=s7, Mobile_no=s8, Cast=s9, Sub_Cast=s10)

        return render(request, "'CitizenDetails'.html")
    return render(request, "'CitizenDetails'.html")


def insertComplaints(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")

        Complaints.objects.create(Complaints_id=s1, Givenby=s2, Complaints_On=s3, Date=s4, MTime=s5)

        return render(request, "'Complaints'.html")
    return render(request, "'Complaints'.html")


def insertSchemes(request):
    if (request.method == "POST"):
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        s9 = request.POST.get("t9")
        s10 = request.POST.get("t10")
        Schemes.objects.create(Schemes_id=s1, Schemes_name=s2, Details=s3, Release_Details=s4, Start_Date=s5,
                               Eligibility=s6, Releasedby=s7, Min_age=s8, Max_age=s9, Mobile_no=s10)

        return render(request, "'Schemes'.html")
    return render(request, "'Schemes'.html")
