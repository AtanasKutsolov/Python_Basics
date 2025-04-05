

broiPaketHimikali = int(input())
broiPaketMarkeri = int(input())
litriPreparat = int(input())
discount = int(input())


cenaNaHimikali = broiPaketHimikali * 5.80 ;
cenaNaMarkeri = broiPaketMarkeri * 7.20 ;
cenaNaPreparat = litriPreparat * 1.20 ;

costs = cenaNaHimikali + cenaNaMarkeri + cenaNaPreparat ;

disocunt2 = costs * (discount/100);

totalCost = costs - disocunt2 ;

print(totalCost)

