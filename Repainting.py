

naylo = int(input())
paint = int(input())
razreditel = int(input())
hours = int(input())

sumForNaylo = (naylo + 2) * 1.50;
sumForPaint = (paint + 1.1) * 14.50 ;
sumForRazreditel = razreditel * 5 ;
sumZaTorbichki = 0.40 ;

obshtaSuma = sumForNaylo + sumForPaint + sumForRazreditel + sumZaTorbichki ;

sumForMaystor = (obshtaSuma * 0.3) * hours ;

totalCost = obshtaSuma + sumForMaystor ;

print(totalCost)
