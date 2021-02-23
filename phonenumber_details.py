import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

phone_number = phonenumbers.parse('Enter Number')
#Brazilian phone number example +55

print(geocoder.description_for_number(phone_number,'en'))
print(carrier.name_for_number,'en')
print(timezone.time_zones_for_number(phone_number))
