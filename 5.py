weight = float(input())
height = float(input())
weight_kg = weight / 2.205
height_meter = 2.54 * height / 100
imt = weight_kg / height_meter ** 2
if imt < 16:
    print('выраженный дефицит массы тела')
elif imt < 18.49:
    print('недостаточная масса тела')
elif imt < 24.99:
    print('норма')
elif imt < 29.99:
    print('избыточная масса тела')
elif imt < 34.99:
    print('ожирение первой степени')
elif imt < 39.99:
    print('ожирение второй степени')
else:
    print('ожирение третьей степени')