from usosapi import *
from os.path import exists
import webbrowser
import json
import credentials

apihandler = USOSAPIConnection('https://apps.usos.pw.edu.pl/', credentials.customer_key,
                               credentials.secret_c_key)


def auth():
    try:
        with open("ldata.usos", "r", encoding='utf-8') as f:
            data = f.readline().split(';')


        apihandler.set_access_data(data[0], data[1])
        assert apihandler.is_authorized()
    except:
        auth_url=apihandler.get_authorization_url()
        print(auth_url)
        webbrowser.open(auth_url)
        apihandler.authorize_with_pin(input('Pin autoryzacyjny: '))
        with open("ldata.usos", "w", encoding='utf-8') as f:
            f.write(';'.join(apihandler.get_access_data()))

    if apihandler.is_authorized():
        identity =apihandler.current_identity()
        print('Autoryzacja poprawna, zalogowano jako {} {} ({})'.format(identity['first_name'], identity['last_name'], identity['id']))


auth()

#do jakich rejestracji mamy dostęp
print('Dostępne rejestracje: ')
print(json.dumps(apihandler.get('services/registrations/user_registrations', active_only='false', fields='id|description'), indent=2))



print("\n-- Szczegóły rejestracji --")
print(json.dumps(apihandler.get('services/registrations/registration',id="6430-WFS-2022L", fields="id|description|status"),indent=2))

print("\n-- Rundy rejestracji --")
print(json.dumps(apihandler.get('services/registrations/course_registration_rounds', registration_id="6430-WFS-2022L"), indent=2))

#20709 - jezyki inne
#id rundy rejestracji: 20498
#registration course żeglarstwo

print("\n-- Wybrany kurs w danej rejestracji")
req=apihandler.get('services/registrations/registration_course',registration_id="6430-WFS-2022L", course_id="6430-00000-000-0025", term_id="2022L")
print(json.dumps(req,indent=2))

req=apihandler.get('services/courses/course', course_id="6430-00000-000-0025")
print(json.dumps(req,indent=2))

print("\n-- Rejestracja --")
req=apihandler.get('services/registrations/register', round_id="20498", course_id="6430-00000-000-0025", term_id="2022L", group_id="1")
print(json.dumps(req,indent=2))


print()
