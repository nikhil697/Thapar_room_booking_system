import mysql.connector
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Credentials
from .models import Booking
import logging
from django.db.utils import IntegrityError
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
from decimal import Decimal
from django.db import connection


# Create your views here.
def loginpage(request):
    return render(request, 'book1/index.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('mail')
        password = request.POST.get('pass1')
        
        conne = mysql.connector.connect(user='root', password='nikhil2002', host='localhost', database='bookroom')
        cursor = conne.cursor()
        query = "SELECT * FROM User WHERE Email = %s AND Password = %s"
        values = (email, password)
        cursor.execute(query, values)
        # escaped_email = mysql.connector.escape_string(email)
        # query = f"SELECT * FROM User WHERE Email = {escaped_email} AND Password = '{password}'"
        # cursor.execute(query)
        user = cursor.fetchone()
        if user:
            request.session['Email'] = user[0] # assuming user_id is the first column in the table
            query = F"SELECT * FROM user WHERE Email = {email}"
            # cursor.execute(query)
            # results = cursor.fetchall()
            # items = goods.objects.filter(Possessed_by__isnull=True)
            # # close the database connection
            # conne.close()
        
            # return render(request, 'sports_goods/particular.html', {'results': results,'items': items})
            return render(request, 'book1/booking.html', {})
        else:
        # close the database connection
            conne.close()

        # if user does not exist, show an error message
            # error_message = 'Invalid login credentials. Please try again.'
            return render(request, 'book1/index.html', {})
    else:
        # if request method is GET, show the login page
        return render(request, 'book1/index.html')

    # if request.method=='POST':
    #     mail=request.POST.get['mail']
    #     pass1=request.POST.get['pass1']
    #     conne = mysql.connector.connect(user='root', password='nikhil2002', host='localhost', database='bookroom')
    #     cursor = conne.cursor()
    #     cursor.execute("SELECT * FROM User WHERE Email = '{}' AND Password = '{}'".format(connection.escape_string(mail),pass1))
    #     result=cursor.fetchone()
    #     if result is not None:
    #         # user is authenticated, redirect to home page
    #         return redirect('home_view')
    #     else:
    #         # authentication failed, show error message
    #         return render(request,'login.html',{'error':"Invalid credentials"})
    # else:
    #     return render(request,'login.html')


def booked(request):
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     sn = request.POST.get('society-name')
    #     email1 = request.POST.get('email')
    #     date = request.POST.get('date')
    #     room = request.POST.get('room')
    #     time_slot = request.POST.get('time')
    #     reason = request.POST.get('message')
    #     # if item1 == item2:
    #     #     message = 'Cannot book the same item twice'
    #     #     return render(request, 'sports_goods/booksuccess.html', {'message': message})
    #     email = request.session.get('Email')
    #     conne = mysql.connector.connect(user='root', password='nikhil2002', host='localhost', database='bookroom')
    #     cursor = conne.cursor()

    #     query = f"UPDATE book1 SET Name='{name}' WHERE id='{}'"
    #     cursor.execute(query)
    #     cursor.execute(query2)
    #     cursor.execute(query3)
    #     conne.commit()
    #     conne.close()
    #     return render(request,'book1/thanks.html',{})
    # else:
    #     return render(request, 'book1/booking.html', {})
    


#     if request.method == 'POST':
#         name = request.POST.get('name')
#         sn = request.POST.get('society-name')
#         email1 = request.POST.get('email')
#         date = request.POST.get('date')
#         room = request.POST.get('room')
#         time_slot = request.POST.get('time')
#         reason = request.POST.get('message')
        
#         email = request.session.get('Email')
#         conne = mysql.connector.connect(user='root', password='nikhil2002', host='localhost', database='bookroom')
#         cursor = conne.cursor()

#         # Get the user ID from the database
#         query_user = f"SELECT id FROM user WHERE email='{email}'"
#         cursor.execute(query_user)
#         user_id = cursor.fetchone()[0]

#         # Insert the form data into the database
#         query_insert = f"INSERT INTO book1 (user_id, name, society_name, email, date, room, time_slot, reason) VALUES ('{user_id}', '{name}', '{sn}', '{email1}', '{date}', '{room}', '{time_slot}', '{reason}')"
#         cursor.execute(query_insert)
        
#         conne.commit()
#         conne.close()
#         return render(request,'book1/thanks.html',{})
#     else:
#         return render(request, 'book1/booking.html', {})


# def thanks(request):
#     return render(request, 'book1/thanks.html')
 
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     sn = request.POST.get('society-name')
    #     email1 = request.POST.get('email')
    #     date = request.POST.get('date')
    #     room = request.POST.get('room')
    #     time_slot = request.POST.get('time')
    #     reason = request.POST.get('message')
        
    #     email = request.session.get('Email')
    #     conne = mysql.connector.connect(user='root', password='nikhil2002', host='localhost', database='bookroom')
    #     cursor = conne.cursor()

    #     # Get the user ID from the database
    #     query_user = f"SELECT id FROM user WHERE email='{email}'"
    #     cursor.execute(query_user)
    #     user_id = cursor.fetchone()[0]

    #     # Insert the form data into the database
    #     query_insert = f"INSERT INTO book1 (user_id, name, society_name, email, date, room, time_slot, reason) VALUES ('{user_id}', '{name}', '{sn}', '{email1}', '{date}', '{room}', '{time_slot}', '{reason}')"
    #     cursor.execute(query_insert)
        
    #     conne.commit()
    #     conne.close()
    #     return render(request,'book1/thanks.html',{})
    # else:
    #     return render(request, 'book1/booking.html', {})


    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     sn = request.POST.get('society-name')
    #     email1 = request.POST.get('email')
    #     date = request.POST.get('date')
    #     room = request.POST.get('room')
    #     time_slot = request.POST.get('time')
    #     reason = request.POST.get('message')
        
    #     # Insert the form data into the database
    #     booking = Booking(Name=name, Sn_Sc=sn, Email=email1, date=date, room=room, time_slot=time_slot, reason=reason)
    #     booking.save()
        
    #     return render(request,'book1/thanks.html',{})
    # else:
    #     return render(request, 'book1/booking.html', {})
    

    if request.method == 'POST':
        name = request.POST.get('name')
        sn = request.POST.get('society-name')
        email_address = request.POST.get('email')
        date = request.POST.get('date')
        room = request.POST.get('room')
        time_slot = request.POST.get('time')
        reason = request.POST.get('message')
        
        try:
            # Get the Credentials instance for the given email address
            email = Credentials.objects.get(Email=email_address)
        except Credentials.DoesNotExist:
            # Handle case where no matching Credentials instance is found
            return HttpResponse('Invalid email address')
        
        # Insert the form data into the database
        booking = Booking(Name=name, Sn_Sc=sn, Email=email, date=date, room=room, time_slot=time_slot, reason=reason)
        booking.save()
        
        return render(request,'book1/thanks.html',{})
    else:
        return render(request, 'book1/booking.html', {})


