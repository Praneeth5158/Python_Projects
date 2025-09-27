#pip install phonenumbers

import phonenumbers
from phonenumbers import geocoder, carrier, timezone
number=phonenumbers.parse("+91 9963258741")
print(geocoder.description_for_number(number,'en'))
print(carrier.name_for_number(number,'en'))
print("Timezones: ",timezone.time_zones_for_number(number))