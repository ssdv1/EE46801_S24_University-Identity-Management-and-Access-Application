from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Avg, Max, Min, Sum
from .models import Professor, Department, CourseSection, Research


def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def admin_dashboard(request):

    feature = request.GET.get('feature', 'roster') 

    if feature == 'roster':
        sort_by = request.GET.get('sort', 'name')  
        if sort_by == 'name':
            professors = Professor.objects.all().order_by('name')
        elif sort_by == 'dept':
            professors = Professor.objects.all().order_by('department__name')
        elif sort_by == 'salary':
            professors = Professor.objects.all().order_by('-salary')
        
        data = list(professors.values('name', 'department__name', 'salary'))
        return JsonResponse(data, safe=False)

    elif feature == 'salary':
        data = Department.objects.annotate(
            min_salary=Min('professor__salary'),
            max_salary=Max('professor__salary'),
            avg_salary=Avg('professor__salary')
        ).values('name', 'min_salary', 'max_salary', 'avg_salary')
        return JsonResponse(list(data), safe=False)

    elif feature == 'performance':
        professor_id = request.GET.get('professor_id')
        academic_year = request.GET.get('academic_year')
        semester = request.GET.get('semester')
        
        professor = Professor.objects.get(pk=professor_id)
        courses_taught = CourseSection.objects.filter(professor=professor, academic_year=academic_year, semester=semester).count()
        students_taught = CourseSection.objects.filter(professor=professor, academic_year=academic_year, semester=semester).aggregate(total_students=Sum('students'))
        research_details = Research.objects.filter(professor=professor).aggregate(total_funding=Sum('funding'), total_papers=Sum('papers_published'))

        response_data = {
            'courses_taught': courses_taught,
            'students_taught': students_taught.get('total_students', 0),
            'total_funding': research_details.get('total_funding', 0),
            'total_papers': research_details.get('total_papers', 0),
        }
        return JsonResponse(response_data)

    else:
        return JsonResponse({'error': 'Invalid feature requested'}, status=400)