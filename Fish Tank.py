duljinasm = int(input())
shirinaSm = int(input())
visochinaSm = int(input())
procent = float(input())

obemNaAkvarium = duljinasm * shirinaSm * visochinaSm ;
obemVlitri = obemNaAkvarium / 1000 ;
zaetoProstranstvo = 0.17 ;

nujnilitri = obemVlitri * (1 - 0.17 ) ;

print(nujnilitri)