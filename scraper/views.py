from django.shortcuts import render, get_object_or_404
from .models import CriminalRecord
from django.core.paginator import Paginator
from django.db.models import Q

# ✅ This view seems redundant or unused — you can remove it unless you're actually using it.
# def records_list(request):
#     records = CriminalRecord.objects.all().order_by('-date')
#     return render(request, 'scraper/records_list.html', {'records': records})

# ✅ Main record list with search and pagination
def record_list(request):
    query = request.GET.get('q')
    records = CriminalRecord.objects.all().order_by('-date_filed')

    if query:
        records = records.filter(
            Q(defendant_name__icontains=query) |
            Q(case_number__icontains=query) |
            Q(parish__icontains=query)
        )

    paginator = Paginator(records, 10)  # 10 records per page
    page = request.GET.get('page')
    records = paginator.get_page(page)

    return render(request, 'scraper/record_list.html', {'records': records})
