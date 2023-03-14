from django.shortcuts import render

# Create your views here.
def conditional(request):
    d={'a':'30','b':'25','c':'40'}
    return render(request,'conditional.html',context=d)
