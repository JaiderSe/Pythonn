s='*'
cero=[s*3,s+' '+s,s+' '+s,s+' '+s,s*3]
uno=[s,s,s,s,s]
dos=[s*3,' '+' '+s,s*3,s+' '+' ',s*3]
tres=[s*3,' '+' '+s,s*3,' '+' '+s,s*3]
cuatro=[s+' '+s,s+' '+s,s*3,' '+' '+s,' '+' '+s]
cinco=[s*3,s+' '+' ',s*3,' '+' '+s,s*3]
seis=[s*3,s+' '+' ',s*3,s+' '+s,s*3]
siete=[s*3,' '+' '+s,' '+' '+s,' '+' '+s,' '+' '+s]
ocho=[s*3,s+' '+s,s*3,s+' '+s,s*3]
nueve=[s*3,s+' '+s,s*3,' '+' '+s,s*3]
numbers=[cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve]

salida=[]
N=[]


def segmentos(strg):
    
    n0=''
    n1=''
    n2=''
    n3=''
    n4=''
    
    for num in strg:
        
        
        n0+=numbers[int(num)][0]+'  '
        n1+=numbers[int(num)][1]+'  '
        n2+=numbers[int(num)][2]+'  '
        n3+=numbers[int(num)][3]+'  '
        n4+=numbers[int(num)][4]+'  '
        
    print(n0)
    print(n1)
    print(n2)
    print(n3)
    print(n4)
segmentos("9081726354")