from django.shortcuts import render,redirect
from .models import UsersAll
from .forms import Reviewform
from django.core.paginator import Paginator,EmptyPage
# Create your views here.

def home_pg(request):
    userall = UsersAll.objects.all()
#     userall = UsersAll.objects.get_queryset().order_by('id')
    p = Paginator(userall,8)

    page_num = request.GET.get('page',1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)


    return render(request,'index.html',{'users':page,'totalpages':p.num_pages})

def photo_detl(request,pkimg):
    userimg = UsersAll.objects.get(id=pkimg)

    form = Reviewform(instance=userimg)
    if request.method == 'POST':
        conv = request.POST.get('but')
        count_num = int(conv)
        count_num = count_num + 1
        form = Reviewform({'review':f'{count_num}'},instance=userimg)
        if form.is_valid():
            form.save()
            print('form saved to database')
        else:
            print('not saved data to database')
    context = {'uname':userimg.uname,'uwork':userimg.work,'uimg':userimg.image,'umaterial':userimg.material_used,'ucost':userimg.cost,'uestimated_date':userimg.estimated_date,'review':userimg.review,'FORM':form}

    return render(request,'photodetl.html',context)
    
def searching(request):
    if request.method == 'GET':
        ser_field = request.GET.get('serbut')
        print(f'printing name that is in input tag {ser_field}')
        resulting = UsersAll.objects.all().filter(uname=ser_field)

    return render(request,'search.html',{'result':resulting})

def contactadmin(request):
    return render(request,'contact.html')
