import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number = input("Enter Mobile Number with +__:")

mobile = phonenumbers.parse(number)
time = timezone.time_zones_for_number(mobile)
cr = carrier.name_for_number(mobile,"en")
reg = geocoder.description_for_number(mobile,"en")

