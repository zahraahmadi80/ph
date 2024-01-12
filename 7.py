import math
x=input().split(";")

b1=eval(x[0])
b2=eval(x[1])
def bordat(dic):
    ss=""
    if dic['i']!=0:
        ss=str(dic['i'])+'i'
    if dic['j']>0:
        ss=ss+'+'+str(dic['j'])+'j'
    elif dic['j']!=0:
        ss=ss+str(dic['j'])+'j'
    if dic['k']>0:
        ss=ss+'+'+str(dic['k'])+'k'
    elif dic['k']!=0:
        ss=ss+str(dic['k'])+'k'

    return ss
makhraj=math.sqrt(b1['i']**2+b1['j']**2+b1['k']**2)+math.sqrt(b2['i']**2+b2['j']**2+b2['k']**2)
sorat=b1['i']*b2['i']+b1['j']*b2['j']+b1['k']*b2['k'];

jame={"i":b1['i']+b2['i'],"j":b1['j']+b2['j'],"k":b1['k']+b2['k']}
tafriq={"i":b1['i']-b2['i'],"j":b1['j']-b2['j'],"k":b1['k']-b2['k']}

zarb_dakheli=(sorat/makhraj)*makhraj
ci=b1['j']*b2['k']-b1['k']*b2['j']
cj=b1['k']*b2['i']-b1['i']*b2['k']
ck=b1['i']*b2['j']-b1['j']*b2['i']

zarb_khareji={"i":ci,"j":cj,"k":ck}
print(bordat(jame))
print(bordat(tafriq))
print(zarb_dakheli)
print(bordat(zarb_khareji))

