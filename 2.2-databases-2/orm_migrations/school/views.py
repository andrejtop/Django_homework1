from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    object_list = Student.objects.prefetch_related('teachers').order_by('group').all()
    context = {'object_list': object_list}

    return render(request, template, context=context)