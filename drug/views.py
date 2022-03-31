from django.shortcuts import render
from .models import Csv, Drug
from .forms import CsvForm
import csv
from django.contrib.auth.decorators import login_required
UTZ = True

# Create your views here.
@login_required
def upload_file_view(request):
    error_message = None
    success_message = None
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvForm()
        try:
            obj = Csv.objects.get(activated=False)
            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)

                for row in reader:                                                 
                    # row = " ".join(row)                                      
                    # row = row.split()                           
                    Drug.objects.create(
                        location = row[0],
                        time = int(row[1]),
                        PC_healthxp = float(row[2]),
                        PC_GDP = float(row[3]),
                        USD_CAP = float(row[4]),
                        Flag_codes = row[5],
                        Total_spend = float(row[6])
                    ) 

            obj.activated = True
            obj.save()
            success_message = "Uploaded successfully"
        except:
            error_message = "Oops. Something went wrong...."

    context = {
        'form': form,
        'success_message': success_message,
        'error_message': error_message
    }
    return render(request, 'drug/upload.html', context)