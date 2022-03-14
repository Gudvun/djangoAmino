import names
from hashlib import sha1
import random
import hmac
import base64

def dev():
    hw=(names.get_full_name()+str(random.randint(0,10000000))+names.get_first_name())
    identifier=sha1(hw.encode('utf-8')).digest()
    mac = hmac.new(bytes.fromhex('76b4a156aaccade137b8b1e77b435a81971fbd3e'), b"\x32" + identifier, sha1)
    return (f"32{identifier.hex()}{mac.hexdigest()}").upper()

def get_weather_from_ip(request):
  print(request.GET.get("ip_address"))
  data = {"weather_data": 20}
  return JsonResponse(data)

def sigg(data):
  key=' fbf98eb3a07a9042ee5593b10ce9f3286a69d4e2'
  mac = hmac.new(bytes.fromhex(key), data.encode("utf-8"), sha1)
  digest = bytes.fromhex("32") + mac.digest()
  return base64.b64encode(digest).decode("utf-8")