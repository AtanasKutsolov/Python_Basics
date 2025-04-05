from First_Steps_In_Coding_Exams.Repainting import totalCost

chikanMAnu = int(input())
fishMAnu = int(input())
veganMAnu = int(input())
delivary = 2.50;

priceForChikan = chikanMAnu * 10.35;
priceForFish = fishMAnu * 12.40;
priceForVegan = veganMAnu * 8.15;

manusCosts = priceForChikan + priceForFish + priceForVegan ;

desertPrice = manusCosts * 0.2 ;

totalCost = manusCosts + desertPrice + delivary ;

print(totalCost)

