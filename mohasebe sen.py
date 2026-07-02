#enter your personality information
sale_tavalod =int(input('sale tavalod:'))
mahe_tavalod =int(input('mahe tavalod:'))
roze_tavalod =int(input('roze tavalod:'))
#enough from today
sale_separi = 512460-(sale_tavalod*365)
mahe_separi = (mahe_tavalod- 1)
roze_separi = (roze_tavalod- 2)
sal = sale_separi // 365
mah = (12-mahe_separi)
rooz = (30-roze_separi)
#show for users
print('shoma',sal,'sal va',mah,'mah va',rooz,
      'rooz az omr khod ra gozarandid') 