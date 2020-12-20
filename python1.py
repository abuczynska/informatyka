g = 9.81  # m/s**2, przyspieszenie norm.

v = input ('podaj prędkość w [km/h]: ')
v = float(v)
v = v * 1000 / 60 / 60  # na metry/sekundę

r = input('podaj promień skrętu [m]: ')
r = float(r)

f = input('współczynnik tarcia: ')
f = float(f)
    
a = v**2 / r

print()

if a > f * g:
    print('nie da się uniknąć poślizgu')
else:
    print('da się uniknąć poślizgu')

print('graniczny współczynnik f =' , a / g)