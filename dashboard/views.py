from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from .models import Product, Order, Book
from .forms import ProductForm, OrderForm, BookForm
from django.contrib.auth.models import User
from django.contrib import messages
import csv
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
import json
import xlwt
from django.core.files.storage import FileSystemStorage
from .filters import ProductFilter


# Create your views here.


@login_required(login_url='user-login')
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form = CreateUserForm()
    return render(request, 'dashboard/home.html', {'form': form})


@login_required(login_url='user-login')
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    orders_count = orders.count()
    products_count = products.count()
    workers_count = User.objects.all().count()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders': orders,
        'form': form,
        'products': products,
        'orders_count': orders_count,
        'products_count': products_count,
        'workers_count': workers_count,
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all()
    product_count = items.count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    myFilter = ProductFilter(request.POST, queryset=items)
    items = myFilter.qs

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items': items,
        'form': form,
        'workers_count': workers_count,
        'product_counts': product_count,
        'orders_count': orders_count,
        'myFilter': myFilter,
    }
    return render(request, 'dashboard/products.html', context)


def home(request):
    return render(request, 'dashboard/index1.html')


@login_required(login_url='user-login')
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')


@login_required(login_url='user-login')
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', context)


@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    orders_count = Order.objects.all().count()
    product_count = Product.objects.all().count()
    context = {
        'workers': workers,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'product_count': product_count,
    }
    return render(request, 'dashboard/staff.html', context)


@login_required(login_url='user-login')
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers': workers,
    }
    return render(request, 'dashboard/staff_detail.html', context)


@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    product_count = Product.objects.all().count()
    workers_count = User.objects.all().count()
    context = {
        'orders': orders,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'product_count': product_count,
    }
    return render(request, 'dashboard/order.html', context)


def export_csv(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['name', 'category', 'quantity'])

    for product in Product.objects.all().values_list('name', 'category', 'quantity'):
        writer.writerow(product)
    response['Content-Disposition'] = 'attachment; filename="product.csv"'

    return response


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['NAME', 'CATEGORY', 'QUANTITY', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Product.objects.all().values_list('name', 'category', 'quantity')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'dashboard/upload.html', context)


def book_list(request):
    books = Book.objects.all()
    return render(request, 'dashboard/book_list.html', {'books': books})


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm()
    return render(request, 'dashboard/upload_book.html', {'form': form})