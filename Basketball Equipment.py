from First_Steps_In_Coding_Exams.Repainting import totalCost

yearsTax = int(input())

priceForKecove = yearsTax - (yearsTax * 0.4 ) ;
priceForSuits = priceForKecove - (priceForKecove * 0.2 ) ;
priceForBall =  priceForSuits * 0.25 ;
priceForAccsesuar = priceForBall * 0.20;

totalCost = yearsTax + priceForKecove + priceForSuits + priceForBall + priceForAccsesuar ;

print(totalCost)