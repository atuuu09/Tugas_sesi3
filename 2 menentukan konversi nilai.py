nilai = int (input("masukan nilai anda:"))
if nilai <50:
    hasil = "nilai anda E"
elif nilai >=50 and nilai <60:
    hasil = "nilai anda D"
elif nilai >=60 and nilai <70:
    hasil = "nilai anda C"
elif nilai >=70 and nilai <80:
    hasil = "nilai anda B"
elif nilai >=80:
    hasil = "nilai anda A"
    
print(hasil)