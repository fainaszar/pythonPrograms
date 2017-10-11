
places ={
    'SR' : 'Nishat',
    'AN' : 'Pahalgam',
    'BG' : 'Yousmarg',
    'TM' : 'Gulmarg',
    'GB' : 'Sonmarg'
}


districts={
    'Srinagar' : 'SR',
    'Anantnag' : 'AN',
    'Budgam'   : 'BG',
    'Tangmarg' : 'TM',
    'Ganderbal': 'GB'
}


for district,code in districts.items():
    print code



print "*" * 15
print "Srinagar has : " + places['SR'] + "\nBudgam has: " + places['BG']


print "Ganderbal has : " + places[districts['Ganderbal']]

place = places.get('AN','No places yet')
print "Anantnag has " + place


print "Comparison Result : %r" % cmp(places,districts)

print str(places)

print type(places['SR'])

print districts
district_copy = districts
print district_copy

copy2 = districts.copy()

print copy2


keys = ('Fname','Lname','Address')
contacts = dict.fromkeys(keys)

print contacts.has_key('Phone')
info ={'Phno':None}
contacts.update(info)

print contacts

