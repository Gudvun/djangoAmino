from django.shortcuts import render
from django.http import JsonResponse
from mysite.device import dev, sigg

# Create your views here.
def home(request):
    return render(request, 'index.html')

def get_device_id(request):
  # print(request.GET.get("ip_address"))
  data = {"deviceID": dev()}
  return JsonResponse(data)

def get_msg_sig(request):
  data = {"msg_sig": sigg(request.GET.get("data"))}
  return JsonResponse(data)

def get_weather_from_ip(request):
  print(request.GET.get("ip_address"))
  data = {"weather_data": 20}
  return JsonResponse(data)