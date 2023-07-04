from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from polls.forms import LoginForm, CustomerLogin, CourseForm
from polls.models import Course
from django.contrib.auth.decorators import login_required


def customer_registration(request):
    form1 = LoginForm()
    form2 = CustomerLogin()

    if request.method == 'POST':
        form1 = LoginForm(request.POST)
        form2 = CustomerLogin(request.POST)

        if form1.is_valid() and form2.is_valid():
            obj = form1.save(commit=False)
            obj.is_customer = True
            obj.save()
            data = form2.save(commit=False)
            data.user = obj
            data.save()
            return redirect('login_view')

    return render(request, 'customer_registration.html', {'form1': form1, 'form2': form2})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:

            if user.is_staff:
                login(request, user)
                return redirect('admindashboard')

            elif user.is_customer:
                login(request, user)
                return redirect('customer_dashboard')

        else:
            messages.info(request, 'invalid Credentials')
    return render(request, 'login.html')


@login_required(login_url='login_view')
def admindashboard(request):
    return render(request, 'adminbase.html')


@login_required(login_url='login_view')
def add_course(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_course')
    return render(request, 'Addcourse.html', {'form': form})


@login_required(login_url='login_view')
def view_course(request):
    data = Course.objects.all()
    p = Paginator(data, 3)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
        # context = {'page_obj': page_obj}
    return render(request, 'Viewcourse.html', {'page_obj': page_obj})


@login_required(login_url='login_view')
def delete(request, id):
    data = Course.objects.get(id=id)
    data.delete()
    return redirect(view_course)


@login_required(login_url='login_view')
def update(request, id):
    data = Course.objects.get(id=id)
    form = CourseForm(instance=data)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_course')
    return render(request, 'updatecourse.html', {'form': form})


@login_required(login_url='login_view')
def customer_dashboard(request):
    return render(request, 'customerbase.html')


def logout_view(request):
    logout(request)
    return redirect('login_view')


@login_required(login_url='login_view')
def cust_view_course(request):
    data = Course.objects.all()
    p = Paginator(data, 3)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    return render(request, 'cust_view_course.html', {'page_obj': page_obj})
