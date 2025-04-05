depositSum = float(input())
srokNaDeposit = int(input())
gofishenLihvenProcent = float(input())

natrupanaLihva = depositSum * (gofishenLihvenProcent/100) ;
lihvazaMesec = natrupanaLihva/ 12 ;

suma  =  depositSum + srokNaDeposit * lihvazaMesec ;

print(suma)