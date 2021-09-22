from django.shortcuts import render
from .forms import Cstudent_dbf, Cmark_dbf
from .models import Marks, Students
from student import models
from django.contrib import messages




################################################################################################
def student(request):
    form = Cstudent_dbf(request.POST or None)
    if form.is_valid():
        form.save()

        form = Cstudent_dbf()
    
    context = {
        'form': form,
        'std': Students.objects.all()
    }

    return render(request,'student.html',context)
##############################################################################################################
def search(request):
    context = {'f': ''}
    if request.method == "POST":
        ss = request.POST['ss']
        if len(ss)>0:
            dt = Students.objects.filter(name__contains=ss)
            context={
                'na':ss,
                'dt':dt,
                'f':"Not present...."
            }
            return render(request,'search.html',context)
        else:
            context = {
                'dt': '',
                'na': "Nothing..!!"
            }
            return render(request, 'search.html', context)
    else:
        context={
            'dt':'',
            'na': "Nothing..!!"
        }
        return render(request, 'search.html', context)


################################################################################################


def mark(request, ass):
    messages.error(request,'markkkkkkk...!')
    context = {}
    obj = Students.objects.get(id=ass)
    na = obj.name
    try:  
        obj = Marks.objects.get(idd=ass) 
        m = obj.mark
        if m == None:
            m = 'No Recodes'
        
    except:
        Mar = Marks.objects.create(idd=int(ass),mark=None)
        Mar.save()
        obj = Marks.objects.get(idd=ass)
        m = obj.mark
        if m == None:
            m = 'No Recodes'
    context = {
        'm': m,
        'id':ass,
        'na':na
    }

    return render(request,'mark.html', context)
######################################################################################################################

def add(request, ass):
    context = {}
    form = Cmark_dbf(request.POST or None)
    
    obj = Students.objects.get(id=ass)
    na = obj.name
    obj = Marks.objects.get(idd=ass)
    m = obj.mark
        
    if m== None:
        m = 'No Recodes'
    context = {
        'm': m,
        'form': form,
        'id': ass,
        'na':na
    }    
    instanc =Marks.objects.get(idd=ass)
    print(type(instanc),"iiii",type(ass))
    form = Cmark_dbf(request.POST or None, instance=instanc)
    if form.is_valid():
        form.save()
        m=request.POST.get('mark')
        temp={'m':m}
        context.update(temp)
        return render(request, 'mark.html', context)

    return render(request, 'add.html', context)




##############################################################################################################

def delete(request,ass):
    d = Students.objects.get(id=ass)
    d.delete()
    dd = Marks.objects.get(idd=ass)
    dd.delete()
    messages.success(request,'student details has been deleted...!')

    return render(request, 'student.html', {})
###############################################################################

def result(request):
    tns=neg_a=neg_b=neg_c=neg_d=neg_e=neg_f=d=fc=p=0
    c = Students.objects.all().count()
    for j in range (c):
        try:
            obj = Marks.objects.get(idd=j+1)
            neg_a = neg_a+(1 if obj.mark >= 91 else 0)
            neg_b = neg_b+(1 if obj.mark >= 81 and obj.mark < 91  else 0)
            neg_c= neg_c+(1 if obj.mark >= 71 and obj.mark < 81 else 0)
            neg_d= neg_d+(1 if obj.mark >= 61 and obj.mark < 71 else 0)
            neg_e= neg_e+(1 if obj.mark >= 55 and obj.mark < 61 else 0)
            neg_f= neg_f+(1 if obj.mark < 55 else 0)
        except:
            pass
    d = round((neg_a/c)*100,2)
    fc = round(((neg_b+neg_c)/c)*100,2)
    p= round(((tns-neg_f)/c)*100,2)

        
    context = {
        's': c,
        'a': neg_a,
        'b': neg_b,
        'c': neg_c,
        'd': neg_d,
        'e': neg_e,
        'f': neg_f,
        'dc': d,
        'fc': fc,
        'p' : p

    }
    return render(request, 'results.html', context)
