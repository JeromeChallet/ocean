from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.shortcuts import render

from management.models import School2
from management.models import Addaschool

from .forms import AddaschoolForm

def oec(request):
    return render(request,'oec/oec.html')

def morning(request):
    school = Addaschool.objects.all().order_by('-id').values()
    # school = Addaschool.objects.all()
    # .objects.all().order_by('-id').values()
    # print("agagaggagagaggaga")
    # for x in school:
    #     print(x.schoolname)
    return render(request,'oec/morning.html', {'school': school})

def afternoon(request):
    return render(request,'oec/index2.html')

def addaschool(request):
    if request.method == 'POST':

        schoolphone = request.POST.get('schoolphone')
        schoolfax = request.POST.get('schoolfax')
        schoolname = request.POST.get('schoolname')
        companyname  = request.POST.get('companyname')
        postelcode = request.POST.get('postelcode')
        addressone = request.POST.get('addressone')
        addresstwo = request.POST.get('addresstwo')
        googlemaplink = request.POST.get('googlemaplink')
        trainstation = request.POST.get('trainstation')
        busstation = request.POST.get('busstation')
        ownername = request.POST.get('ownername')
        ownerphone = request.POST.get('ownerphone')
        personincharge = request.POST.get('personincharge')
        picphone = request.POST.get('picphone')
        print("phoneoooooooooooooooo")
        # print(picphone)
        branchStudentObject = Addaschool(companyname=companyname, postelcode=postelcode, addressone=addressone, addresstwo=addresstwo, schoolname=schoolname, schoolphone=schoolphone, schoolfax=schoolfax, googlemaplink=googlemaplink, trainstation=trainstation, busstation=busstation, ownername=ownername, ownerphone=ownerphone, personincharge=personincharge, picphone=picphone)
        branchStudentObject.save()
    return render(request,'oec/add-a-school.html')

# if request.method == "POST":
#         product = get_object_or_404(Product, id=product_id)
#         product.model_name = request.POST['model_name']
#         product.image = request.FILES['image']
#         product.save()
#         return redirect('listing')

def addaschoolupdate(request, pk):
    school = Addaschool.objects.filter(id=pk)
            # Entry.objects.values_list('id', 'headline')
    print(school)
    if request.method == 'POST':
        product = get_object_or_404(Addaschool, id=pk)
        # branch = Branch.objects.get(id=pk)
        schoolname  = request.POST.get('schoolname')
        # branchStudentObject = Addaschool(companyname=schoolname)
        # branchStudentObject.save()
        # branch = request.POST.get('branch')
        # saveschoolname = addaschool(companyname='schoolname')
        # saveschoolname.save()
        # obj = AddTeacher(TeacherID=ID)
        # obj.save()
        # schoolname.save()
        print("amammamammamammamama")
        print(schoolname)
    # school = School2.objects.all()
    print("hwhwhwwhhwhhwhwhhwhwhhwhhwhwhhwhw")
    for i in school:
        print(i.schoolname)
    return render(request,'oec/add-a-school-edit.html', {'school': school})

def editschool(request, pk):
    if request.method == 'POST':
        # editcolumn = Addaschool.objects.get(id=pk)
        # print(editcolumn)
        # form = Addaschool(request.POST, instance=editcolumn)

        editedcolumn = get_object_or_404(Addaschool, id=pk)
        # form = AddaschoolForm(request.POST or NONE, instance=editedcolumn)
        # if form.valid():
        #     form.save()
        # form = AddaschoolForm(request.POST or None, instance=editedcolumn)
        editedcolumn.schoolphone = request.POST.get('schoolphone')
        editedcolumn.schoolfax = request.POST.get('schoolfax')
        editedcolumn.schoolname = request.POST.get('schoolname')
        editedcolumn.companyname = request.POST.get('companyname')
        editedcolumn.postelcode = request.POST.get('postelcode')
        editedcolumn.addressone = request.POST.get('addressone')
        editedcolumn.addresstwo = request.POST.get('addresstwo')
        editedcolumn.googlemaplink = request.POST.get('googlemaplink')
        editedcolumn.trainstation = request.POST.get('trainstation')
        editedcolumn.busstation = request.POST.get('busstation')
        editedcolumn.ownerphone = request.POST.get('ownerphone')
        editedcolumn.ownername = request.POST.get('ownername')
        editedcolumn.personincharge = request.POST.get('personincharge')
        editedcolumn.picphone = request.POST.get('picphone')

        print("produuuuuuccccct")
        print(editedcolumn.trainstation)
        editedcolumn.save()
        # school = Addaschool.objects.all()
        school = Addaschool.objects.all().order_by('-id').values()
    return render(request, 'oec/morning.html', {'school': school})


# if request.method == "POST":
#         product = get_object_or_404(Product, id=product_id)
#         product.model_name = request.POST['model_name']
#         product.image = request.FILES['image']
#         product.save()
#         return redirect('listing')


def schoollist(request):
    school = School2.objects.all()
    return render(request,'oec/schoollist.html')

def deleteschool(request, pk):
    school = Addaschool.objects.get(id=pk)
    print(school)
    if request.method == "POST":
        # branchDelete.delete()
        school.delete()
        return redirect('morning')
    context = {'id': school}

    return render(request, 'oec/delete-school-confirm.html', context)

