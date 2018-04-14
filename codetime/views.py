from django.shortcuts import render, redirect, HttpResponse
from django.http import StreamingHttpResponse
from codetime.Extens import PageList
from codetime.models import Person, Product
from .forms import LoginForm, ProductForm
from . import models

from openpyxl import load_workbook

import os



# Create your views here.
def auth(func):
    def inner(reqeust, *args, **kwargs):
        v = reqeust.COOKIES.get('username111')
        if not v:
            return redirect('/codetime/login')
        return func(reqeust, *args, **kwargs)

    return inner


# 用户登录函数
def loginForm(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            name = request.POST.get('name', 'NAME')
            password = request.POST.get('password', 'PASSWORD')
            person = Person()
            person.name = "lifushuai"
            person.password = "123456"
            # person = models.Person.objects.get(pk=1)
            if name == person.name and password == person.password:
                res = redirect('/codetime/product/0')
                res.set_cookie('username111', person)
                return res
            return render(request, 'codetime/login.html')
        else:
            print(login_form.errors.as_json())
            return render(request, 'codetime/login.html', {"person": login_form.cleaned_data})
    return render(request, 'codetime/login.html')

@auth
def product(request, item_id):
    if str(item_id) == '0':
        return render(request, 'codetime/product.html')
    product = models.Product.objects.filter(id=item_id).first()
    # product_form = ProductForm(instance=product)
    return render(request, 'codetime/product.html', {"product": product})


@auth
def productForm(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_id = request.POST.get('product_id')
            if product_id != "0":
                models.Product.objects.filter(id=product_id).delete()
            product_form.save()
            return render(request, 'codetime/product.html')
        else:
            print(product_form.errors)
            return render(request, 'codetime/product.html', {"product": product_form.cleaned_data})


@auth
def changeShipments(request):
    if request.method == 'POST':
        item_id = int(request.POST.get('item_id'))
        shipments = request.POST.get('item_shipments')
        if shipments == 'True':
            models.Product.objects.filter(id=item_id).update(shipments=False)
        else:
            models.Product.objects.filter(id=item_id).update(shipments=True)
    return HttpResponse('OK')


@auth
def changeStatus(request):
    if request.method == 'POST':
        item_id = int(request.POST.get('item_id'))
        status = request.POST.get('item_status')
        if status == 'True':
            models.Product.objects.filter(id=item_id).update(status=False)
        else:
            models.Product.objects.filter(id=item_id).update(status=True)
    return HttpResponse('OK')


@auth
def changeKnot(request):
    if request.method == 'POST':
        item_id = int(request.POST.get('item_id'))
        knot = request.POST.get('item_knot')
        if knot == 'True':
            models.Product.objects.filter(id=item_id).update(knot=False)
        else:
            models.Product.objects.filter(id=item_id).update(knot=True)
    return HttpResponse('OK')


@auth
def orderSearch(request):
    condition = {}
    text1 = request.GET.get('text1', "")
    text2 = request.GET.get('text2', "")
    text23 = request.GET.get('text23', "")
    shipments = request.GET.get('shipments', "全部")
    status = request.GET.get('status', "全部")
    knot = request.GET.get('knot', "全部")
    if len(text1) != 0:
        condition["text1"] = text1
    if len(text2) != 0:
        condition["text2"] = text2
    if len(text23) != 0:
        condition["text24"] = text23
    if shipments != "全部":
        condition["shipments"] = int(shipments)
    if status != "全部":
        condition["status"] = int(status)
    if knot != "全部":
        condition["knot"] = int(knot)
    dataSource = models.Product.objects.all()
    if len(dataSource) == 0:
        return render(request, 'codetime/orderSearch.html')
    dataSource = models.Product.objects.filter(**condition).order_by('-text23')
    if len(dataSource) == 0:
        return render(request, 'codetime/orderSearch.html')
    current_page = request.GET.get('p', 1)
    current_page = int(current_page)
    val = 10
    page_obj = PageList.Page(current_page, len(dataSource), val)
    data = dataSource[page_obj.start:page_obj.end]

    page_str = page_obj.page_str("")
    return render(request, 'codetime/orderSearch.html',
                  {"dataSource": data, 'page_str': page_str, "condition": condition, "nonReceiveAmount":1000, "receiveAmount":1000, "fullAmount":2000})


def writeOrderToExcel(request):
    item_id = int(request.GET.get('item_id'))
    product_obj = models.Product.objects.filter(id=item_id).first()

    # 默认可读写，若有需要可以指定write_only和read_only为True
    wb = load_workbook('productModel.xlsx')
    sheet = wb.active
    sheet['B3'] = product_obj.text1
    sheet['B4'] = product_obj.text2
    sheet['G3'] = product_obj.text3
    sheet['G4'] = product_obj.text4
    sheet['B7'] = product_obj.text5
    sheet['B8'] = product_obj.text6
    sheet['B9'] = product_obj.text7
    sheet['B10'] = product_obj.text8
    sheet['B11'] = product_obj.text9
    sheet['B12'] = product_obj.text10
    sheet['B13'] = product_obj.text25
    sheet['B14'] = product_obj.text26
    sheet['B15'] = product_obj.text27
    sheet['B16'] = product_obj.text28
    sheet['B17'] = product_obj.text29
    sheet['B18'] = product_obj.text30
    sheet['B20'] = product_obj.text11
    sheet['B21'] = product_obj.text12
    sheet['B22'] = product_obj.text13
    sheet['B23'] = product_obj.text14
    sheet['B24'] = product_obj.text15
    sheet['B25'] = product_obj.text16
    sheet['B26'] = product_obj.text17
    sheet['B27'] = product_obj.text18
    sheet['B28'] = product_obj.text19
    sheet['B29'] = product_obj.text20
    sheet['B30'] = product_obj.text21
    sheet['B31'] = product_obj.text22
    sheet['E3'] = product_obj.text23
    # sheet['E4'] = product_obj.text24
    the_file_name = "tmp.xlsx"
    exist_file = os.path.exists(the_file_name)
    if exist_file:
        os.remove(r"tmp.xlsx")
    wb.save(the_file_name)

    def file_iterator(file_name, chunk_size=512):
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/vnd.ms-excel'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response

    # timestr = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # system, node, release, version, machine, processor = platform.uname()
    # if system == 'Darwin':
    # print()
    # wb.save(os.getcwd() + timestr + '.xlsx')
    # else:
    #     path = timestr + '.xlsx'
    # wb.save(r'D:\\' + path)
    # print(system)
    # wb.save(r'D:\example.xlsx')
    # return HttpResponse('OK')



