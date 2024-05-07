print("Quieres Saber cuanto vas a ganar esta semana?")
Hrs = float(input("Enter Hours"))
Rate = float(input("Enter Rate"))
if Hrs <= 50.0 :
    print ("Este este es tu pago semanal :", Hrs * Rate)
    print ("Contactate con tu jefe para que te suban el sueldo")
else :
    print (((Hrs - 40) * 1.5 * Rate) + (40 * Rate))
    print ("Dile a tu jefe que gracias por el overtime")
    print ("Este es tu pago semanal sin deducciones :" ((Hrs - 40) * 1.5 * Rate) + (40 * Rate))
