from django.shortcuts import render, get_object_or_404
from .models import Scheme, Branch, Semester, Subject, Notes, YTLink, KTUUpdates, Newsletter
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if Newsletter.objects.filter(email=email).exists():
            return JsonResponse({'error': 'This email is already subscribed'}, status=400)
        
        newsletter = Newsletter(email=email)
        newsletter.save()

        return JsonResponse({'message':'Thank You for subscribing'})
    else:
        return JsonResponse({'error':'Invalid Request'}, status=400)

def scheme2019(request):
    branch = request.GET.get('branch')
    print(branch)
    scheme_2019 = Scheme.objects.get(scheme_name='2019')
    branches = Branch.objects.filter(scheme_id=scheme_2019)
    return render(request, 'scheme2019.html', {'branches':branches})

def scheme2024(request):
    scheme_2024 = Scheme.objects.get(scheme_name='2024')
    branches = Branch.objects.filter(scheme_id=scheme_2024)
    return render(request, 'scheme2024.html', {'branches':branches})

def linkpage(request, semester_id):
    semester = get_object_or_404(Semester, sem_id=semester_id)
    notes = Notes.objects.filter(semester_id=semester)
    yt_links = YTLink.objects.filter(semester_id=semester)

    return render(request, 'linkpage.html', {
        'semester':semester,
        'notes':notes,
        'yt_links':yt_links,
    })

def sempage(request, branch_id):
    branch = get_object_or_404(Branch, branch_id=branch_id)
    sem = Semester.objects.filter(branch_id=branch).all()
    sem_details = []
    for sem_instance in sem:
        sem_details.append({
            'semester_id': sem_instance.sem_id,
            'semester_number': sem_instance.sem_number,
            'branch_name': sem_instance.branch_id.branch_name,
        })
    return render(request, 'sempage.html', {'semesters':sem_details, 'branch':branch})

def results(request):
    search_query = request.GET.get('search_query', '')
    unique_videos = {}

    if search_query:
        yt_links = YTLink.objects.filter(subject_name__icontains=search_query)

        for video in yt_links:
            if video.subject_name not in unique_videos:
                unique_videos[video.subject_name] = [video.links]
            else:
                if video.links not in unique_videos[video.subject_name]: 
                    unique_videos[video.subject_name].append(video.links)

    unique_videos_list = [(subject, links) for subject, links in unique_videos.items()]

    return render(request, 'results.html', {
        'unique_videos': unique_videos_list,
        'search_query': search_query,
    })

def updates(request):
    updates = KTUUpdates.objects.all()
    updates = updates[::-1]
    return render(request, 'updates.html', {'updates':updates})
