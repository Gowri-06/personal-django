# from os import PRIO_PGRP
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import csv
# from backend import student
from . models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.template import loader
from django.urls import reverse
from datetime import date,timedelta, datetime
import pyautogui

def shown(request):
    return render(request, "show.html")


def addpage(request):

    if request.method == "POST":
       name = request.POST.get("name") 
       age = request.POST.get("age")  
       roll_no = request.POST.get("roll_no")  
       place = request.POST.get("place")  
       email_id = request.POST.get("email_id") 
       a = Student(name=name,age=age,roll_no=roll_no,place=place,email_id=email_id).save()
       print((a))
    #    return HttpResponse("save_data")
       return HttpResponseRedirect(reverse('shown'))
    else:
       return render(request, "adddata.html")

def viewpage(request):
    data =Student.objects.all().values().order_by('-created_at')
    print(data)
    template = loader.get_template('viewdata.html')
    context = {
        "data":data,
        "Id":"Id",
        "Name":"Name",
        "Age":"Age",
        "Roll_number":"Roll number",
        "Place":"Place",
        "Email":"Email"

    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("db_data")
def delete(request,id):
    delete_data = Student.objects.get(id=id)
    print(delete_data)
    delete_data.delete()
    return HttpResponseRedirect(reverse('viewpage'))
    
    
def viewpageone(request,id):
    data =Student.objects.get(id=id)
    print(data)
    template = loader.get_template('viewdataone.html')
    context = {
        "data":data,
        "Id":"Id",
        "Name":"Name",
        "Age":"Age",
        "Roll_number":"Roll number",
        "Place":"Place",
        "Email":"Email"

    }
    return HttpResponse(template.render(context, request))

def update(request,id):
    get_data = Student.objects.get(id=id)
    print("get_data",get_data) 
    template = loader.get_template('update.html')
    context = {
        "data":get_data
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request,id):
    update_data = Student.objects.get(id=id)
    print(update_data)
    name =request.POST['name'] 
    age = request.POST['age']  
    roll_no = request.POST['roll_no']  
    place = request.POST['place'] 
    email_id = request.POST['email_id']
    update_student_data = Student.objects.filter(id=id)

    update_student_data(name=name,age=age)
    update_student_data.age = age 
    update_student_data.roll_no = roll_no  
    update_student_data.place = place  
    update_student_data.email_id = email_id 
    update_student_data.save()
    return HttpResponseRedirect(reverse('viewpage'))


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def download_data(request):
    download = Student.objects.all().values()
    filename = "data.csv"
    fields = ["id","name","age","roll_no","place","email_id","created_at","updated_at"]
    csv_file = open(filename, "w", newline='')
    writer = csv.DictWriter(csv_file,fieldnames=fields)
    writer.writeheader()
    writer.writerows(download)
    print(download)
    return HttpResponse("csv file stored successfully")


def download_single_data(request,id):
    check_id = id
    print(">>>>>>>>>>>",check_id)
    download = Student.objects.get(id=id)
    var1 = [{
        "id":download.id,
        "name":download.name,
        "age":download.age,
        "roll_no":download.roll_no,
        "place":download.place,
        "email_id":download.email_id
    }]
    print(type(var1))
    filename = "single_data.csv"
    fields = ["id","name","age","roll_no","place","email_id"]
    csv_file = open(filename, "w", newline='')
    writer = csv.DictWriter(csv_file,fieldnames=fields)
    writer.writeheader()
    writer.writerows(var1)
    return HttpResponse("csv file stored successfully")



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def adminview(request):
  
    choose_date = request.POST.get("date")
    print("form-date",choose_date)
    today = date.today()
    print(type(today))
    d1 = today.strftime("%Y-%m-%d")
    print("d1>>>>>>>",d1)
    print(type(today))
    present_day = datetime.now()
    print(type(present_day))
    thirty_days_ago = present_day - timedelta(days=30)
    print("thirty_days_ago",type(thirty_days_ago))
    yesterday = present_day - timedelta(6)
    class_str = yesterday.strftime("%Y-%m-%d")
    print("class_str",type(class_str))
    tomorrow = present_day + timedelta(1)
    this_year = present_day.strftime("%Y")
    this_month = present_day.strftime("%m")
    print("present_day",present_day.strftime("%Y-%m-%d"))
    print("yesterday",yesterday.strftime("%Y-%m-%d"))
    print("yesterday",type(yesterday))
    print("tomorrow",tomorrow.strftime("%Y-%m-%d"))
    data =Student.objects.all().values().order_by('-created_at')
    # Sample.objects.filter(date__range=["2011-01-01", "2011-01-31"])
    data_1_week = Student.objects.filter(created_at__range=[yesterday,present_day])
    print(data_1_week)
    data_2_month = Student.objects.filter(created_at__year=this_year, created_at__month=this_month)
    print(data_2_month)
    data_3_day = Student.objects.filter(created_at__date=d1)
    print(data_3_day)
    
    template = loader.get_template('adminview.html')
    context = {
        "data_1":data_1_week,
        "data_2":data_2_month,
        "data_3":data_3_day,
        "Id":"Id",
        "Name":"Name",
        "Age":"Age",
        "Roll_number":"Roll number",
        "Place":"Place",
        "Email":"Email",
        "Date":"Date"

    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("output")


def yearview(request):
  if request.method == "POST":
 
    
    choose_month = request.POST.get("month")
    print("month-date",type(choose_month),choose_month)
    list_box_split = choose_month.split("-")
    print("list_box_split",list_box_split)
    present_day = datetime.now()
    print(type(present_day))
     
    datetime_str = '09/19/18 13:55:26'
    datetime_object = datetime.strptime(choose_month, '%Y-%m-%d').date()
    print(type(datetime_object))
    thirty_days_ago = datetime_object - timedelta(days=30)
    print("thirty_days_ago",thirty_days_ago)
    class_str =  thirty_days_ago.strftime("%Y-%m-%d")
    print("class_str",type(class_str),class_str)
    print(datetime_object)  # printed in default format
    # thirty_days_ago_str =  (thirty_days_ago.strftime("%Y-%m-%d"))

    # Sample.objects.filter(date__range=["2011-01-01", "2011-01-31"])
    # data_1_week = Student.objects.filter(created_at__range=[choose_date1_range1, choose_date2_range2])
    # print(data_1_week)
    # data_2_month = Student.objects.filter(created_at__year=list_box_split[0], created_at__month=list_box_split[1])
    # print("data_2_month",data_2_month)
    data_2_month = Student.objects.filter(created_at__range=[class_str,choose_month])
    print("data_2_month",data_2_month)
    count_data_2_month = Student.objects.filter(created_at__range=[class_str,choose_month]).count()
    print("count_data_2_month>>>",count_data_2_month)
    # data_3_day = Student.objects.filter(created_at__date=choose_date1)
    # print(data_3_day)
    
    template = loader.get_template('adminview.html')
    context = {
        "data_1":"",
        "data_2":data_2_month,
        "data_3":"",
        "month_count":count_data_2_month,
        "Id":"Id",
        "Name":"Name",
        "Age":"Age",
        "Roll_number":"Roll number",
        "Place":"Place",
        "Email":"Email",
        "Date":"Date"

    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("oerefefef")
    
def dateview(request):
  if request.method == "POST":
   
    choose_date1 = request.POST.get("today_date")
    print("single-day-date",type(choose_date1),choose_date1)
    
    data =Student.objects.all().values().order_by('-created_at')
    # Sample.objects.filter(date__range=["2011-01-01", "2011-01-31"])
    # data_1_week = Student.objects.filter(created_at__range=[choose_date1_range1, choose_date2_range2])
    # print(data_1_week)
    # data_2_month = Student.objects.filter(created_at__year=list_box_split[0], created_at__month=list_box_split[1])
    # print(data_2_month)
    data_3_day = Student.objects.filter(created_at__date=choose_date1)
    print(data_3_day)
    count_data_3_day = Student.objects.filter(created_at__date=choose_date1).count()
    print("count_data_3_day",type(count_data_3_day))
    
    template = loader.get_template('adminview.html')
    context = {
        "data_1":"",
        "data_2":"",
        "data_3":data_3_day,
        "day_count":str(count_data_3_day),
        "Id":"Id",
        "Name":"Name",
        "Age":"Age",
        "Roll_number":"Roll number",
        "Place":"Place",
        "Email":"Email",
        "Date":"Date"

    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("oerefefef")


def weekview(request):
  if request.method == "POST":
    choose_date1_range1 = request.POST.get("date1")
    print("form-range-date",type(choose_date1_range1),choose_date1_range1)
    choose_date2_range2 = request.POST.get("date2")
    print("form-range-date",choose_date2_range2)
    data_1_week = Student.objects.filter(created_at__range=[choose_date1_range1, choose_date2_range2])
    print(data_1_week)
    count_data_1_week = Student.objects.filter(created_at__range=[choose_date1_range1, choose_date2_range2]).count()
    print("count",count_data_1_week)
    # data_2_month = Student.objects.filter(created_at__year=list_box_split[0], created_at__month=list_box_split[1])
    # print(data_2_month)
    # data_3_day = Student.objects.filter(created_at__date=choose_date1)
    # print(data_3_day)
    
    template = loader.get_template('adminview.html')
    context = {
        "data_1":data_1_week,
        "data_2":"",
        "data_3":"",
        "week_count":str(count_data_1_week),
        "Id":"Id",
        "Name":"Name",
        "Age":"Age",
        "Roll_number":"Roll number",
        "Place":"Place",
        "Email":"Email",
        "Date":"Date"

    }
    return HttpResponse(template.render(context, request))
    

def loginpage(request):

  
    
    template = loader.get_template('loginpage.html')
    context = {
       

    }
    return HttpResponse(template.render(context,request))

def adminanduser(request):
        
    template = loader.get_template('adminanduser.html')
    context = {
       
      
        

    }
    return HttpResponse(template.render(context,request))



