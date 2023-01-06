email=input('enter your email:')
phno=int(input('enter your phno:'))

if email.endswith("@gmail.com") and len(phno)==10:
   if phno.startswith(9) or phno.startswith(8) or phno.startswith(7) or phno.startswith(6) or phno.startswith(0):
       print('registration successfull')
else:
            print('check your details')