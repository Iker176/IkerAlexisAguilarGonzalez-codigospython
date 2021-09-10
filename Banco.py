#!/usr/bin/env python
# coding: utf-8

# In[1]:


def _cuentas(prestamo,meses):
    cuota=prestamo/meses
    return cuota

def _Prestamo():
    prestamo= input("Monto de tu prestamo? ")
    meses= input("En cuantos meses deseas pagar? ")
    print ("Monto de pago por mes es: ",_cuentas(prestamo,meses))

edad= int (input ("Dame tu edad: "))
if edad >= 18:
    ingresos=int(input("Dame tus ingresos: "))
    egresos=int(input("Dame tus egresos: "))
    if ingresos >= egresos:
        _Prestamo()
    else:
        print("Sus ingresos deben ser mayores.")

else:
    print ("No eres mayor de edad.")


# In[ ]:




