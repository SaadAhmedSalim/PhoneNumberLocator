import phonenumbers

from phonenumbers import geocoder

from phonenumbers import carrier



user_inp = input('Enter a Phone Number with Country Code: ')



# TO know From which country the Number Belongs!!

ch_nmber = phonenumbers.parse(user_inp,'CH')

print(geocoder.description_for_number(ch_nmber,"en"))



# TO know From which Service Provider the Number is being Linked to!!

service_numb = phonenumbers.parse(user_inp,"RO")

print(carrier.name_for_number(service_numb,"en"))