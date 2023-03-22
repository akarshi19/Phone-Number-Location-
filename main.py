import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

x = int(input())
ch_number = phonenumbers.parse(x, "CH")
print("Location:")
print(geocoder.description_for_number(ch_number, "en"))
service_number = phonenumbers.parse(x, "RO")
print("SIM:")
print(carrier.name_for_number(service_number, "en"))

