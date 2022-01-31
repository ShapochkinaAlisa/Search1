from Samples.mapapi_PG import show_map
from Samples.geocoder import get_coordinates, get_ll_span
import sys
adress = ' '.join(sys.argv[1:])
longitude, lattitude = get_coordinates(adress)
param1 = f"ll={longitude},{lattitude}"
param2 = f"&spn=30,30"
show_map(param1 + param2)
res = get_ll_span(adress)
show_map(f"ll={res[0]}&spn={res[1]}", add_params=f'pt={longitude},{lattitude},pm2ywl1')