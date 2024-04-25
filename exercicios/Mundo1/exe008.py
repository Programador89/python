# Ao receber o valor em metros, converta o mesmo para KM, HM, DAM, DM, CM, MM

metros = float(input('Informe um valo em metro: '))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print('A media de {:.2f} metros corresponde a: \n{:.3f}km \n{:.3f}hm \n{:.3f}dam \n{}dm \n{:.3f}cm \n{:.3f}mm'.format(metros, km, hm, dam, dm, cm, mm))

