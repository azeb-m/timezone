from django.shortcuts import render
from datetime import datetime
import pytz


def showt(request):
    # Set the timezone for Ethiopia
    ethiopian_timezone = pytz.timezone('Africa/Addis_Ababa')

    # Get the current time in UTC
    utc_now = datetime.utcnow()

    # Convert the UTC time to the Ethiopian timezone
    ethiopian_time = utc_now.replace(tzinfo=pytz.utc).astimezone(ethiopian_timezone)


    context = {
        'TIME_ZONE': ethiopian_time,
    }
     
    return render(request, 'my_template.html',context)
