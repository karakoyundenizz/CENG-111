# hangisinin olduğunu bulma
def pattern_search(P, I):
 n=0
 while n< len(P)-1 :
    if len(P[0])!=len(P[n+1]): return False
    n+=1
#0 derece
 p0=P
#90 derece
 def dok(n):
    z=len(P)-1
    return doksan(z,n)
 def doksan(z,n) :

    if z==1 : return P[1][n]+ P[0][n]
    return P[z][n] + doksan(z-1,n)
 p90=list(map(dok,range(len(P[0]))))
#180 deneme map

 p2=P[::-1]
 def cevir(l):
    return l[::-1]
 p180= list(map(cevir,p2))
#270 derece
 def yetmıs(n):
    z = 0
    return ıkıyuz_yetmıs(z, n)
 def ıkıyuz_yetmıs(z,n) :
    if z == len(P)-2: return P[len(P)-2][n]+ P[len(P)-1][n]
    return P[z][n] + ıkıyuz_yetmıs(z+1,n)
 p270=list(map(yetmıs,range(len(P[0]))[::-1]))
#checking in or not 0 degree
 starty=0
 start=0
 start1=0
 B = len(I[0])
 def checking0(p0,I,x):
  k = I[:]
  a = 0
  b = 0
  global start
  global starty
  globals()
  while a < len(p0) and b< len(k):
    if len(p0) > len(k): return False
    if len(p0)==0:
        return False
    if len(k[0])==0 : return False
    if a == 0 and len(p0) == 1 and p0[a] in k[b]:
        start= start1 + k[b].index(p0[a])
        starty=b
        return (starty,start,x)
    if a == 0 and len(p0) == 1 and b != len(k) - 1 and p0[a] not in k[b]:
        a=a
        b+=1
    if a == 0 and len(p0) != 1 and b == len(k) - 1 and p0[a] not in k[b]:
        return False
    if a == 0 and len(p0)!=1 and b != len(k) - 1 and p0[a] in k[b]:
        start=start1 + k[b].index(p0[a])
        starty=b
        a+=1
        b+=1
    if a == 0 and len(p0)!=1 and b != len(k)-1 and p0[a] not in k[b]:
       b+=1
       a=a
    if a == 0 and len(p0)!=1 and b == len(k)-1 and p0[a] not in k[b]:
        return False
    if 0<a<len(p0)-1  and b< len(k) and p0[a] in k[b]:
        def eleman_kaldır(t):
            global start1
            global start
            if p0[0] not in k[starty]: return []
            x = k[starty].index(p0[0])
            return k[t][x:]

        U = list(map(eleman_kaldır, range(len(k))))
        def eleman_cek(t):
            global start1
            global start
            if p0[0] not in k[starty]: return []
            x = k[starty].index(p0[0])
            return k[t][x + 1:]
        Z = list(map(eleman_cek, range(len(k))))
        r = k[starty].index(p0[0])
        c = k[b].index(p0[a])
        if c == r :
            a+=1
            b+=1
        elif c != r and I != U and checking0(p0, U, x) == False:
            if checking0(p0, Z, x) == False:
                b = b - a + 1
                a = 0
            elif checking0(p0, Z, x) != False:
                return checking0(p0, Z, x)
        elif c != r and I != U and checking0(p0, U, x) != False:
            return checking0(p0, U, x)
        elif c != r and I == U and start == 0 and checking0(p0, Z, x) != False:
            return checking0(p0, Z, x)
        elif c != r and I == U and start == 0 and checking0(p0, Z, x) == False:
            b = b - a + 1
            a = 0
        elif c != r and I == U and start > 0:
            return False
        else:
            return False
    if a == len(p0) - 1 and b < len(k) - 1 and p0[a] not in k[b]:
        b = b - a + 1
        a = 0
    if a < len(p0) - 1 and b == len(k) - 1:
        return False

    if 0<a<len(p0)-1  and b< len(k) and p0[a] not in k[b]:
        b=b-a +1
        a = 0
    if a==len(p0) -1  and b == len(k) -1 and p0[a] in k[b]:
        def eleman_kaldır(t):
            global start1
            global start
            if p0[0] not in k[starty]: return []
            x = k[starty].index(p0[0])
            return k[t][x:]
        U = list(map(eleman_kaldır, range(len(k))))
        def eleman_cek(t):
            global start1
            global start
            if p0[0] not in k[starty]: return []
            x = k[starty].index(p0[0])
            return k[t][x + 1:]
        Z = list(map(eleman_cek, range(len(k))))
        r = k[starty].index(p0[0])
        c = k[b].index(p0[a])
        if c == r and B == len(k[0]):
            return (starty, start, x)
        if c == r and B != len(k[0]):
            return (starty, start + B - len(k[0]), x)
        elif c != r and I != U and checking0(p0, U, x) == False:
            if checking0(p0, Z, x) == False:
                b = b - a + 1
                a = 0
            elif checking0(p0, Z, x) != False:
                return checking0(p0, Z, x)
        elif c != r and I != U and checking0(p0, U, x) != False:
            return checking0(p0, U, x)
        elif c != r and I == U and start == 0 and checking0(p0, Z, x) != False:
            return checking0(p0, Z, x)
        elif c != r and I == U and start == 0 and checking0(p0, Z, x) == False:
            b = b - a + 1
            a = 0
        elif c != r and I == U and start > 0:
            return False
        else:
            return False
    if a == len(p0) - 1 and b < len(k) - 1 and p0[a] not in k[b]:
        b = b - a + 1
        a = 0
    if a < len(p0) - 1 and b == len(k) - 1:
        return False
    if a == len(p0) - 1 and b == len(k) - 1 and p0[a] not in k[b]:
        return False
    if a == len(p0) - 1 and b  < len(k) - 1 and p0[a] in k[b]:
        def eleman_kaldır(t):
            global start1
            global start
            if p0[0] not in k[starty]: return []
            x = k[starty].index(p0[0])
            return k[t][x:]
        U = list(map(eleman_kaldır, range(len(k))))
        def eleman_cek(t):
            global start1
            global start
            if p0[0] not in k[starty]: return []
            x = k[starty].index(p0[0])
            return k[t][x + 1:]
        Z = list(map(eleman_cek, range(len(k))))
        r=k[starty].index(p0[0])
        c = k[b].index(p0[a])
        if c == r and B== len(k[0]):
            return (starty,start,x)
        if c == r and B!= len(k[0]):
            return (starty,start+B-len(k[0]),x)
        elif c != r and I != U and checking0(p0, U, x) == False :
            if checking0(p0, Z, x) == False:
                b = b - a + 1
                a = 0
            elif checking0(p0, Z, x) != False:
                return checking0(p0, Z, x)
        elif c != r and I != U and checking0(p0, U, x) != False  :
            return checking0(p0,U, x)
        elif c != r and I == U and start==0 and checking0(p0, Z, x) != False  :
            return checking0(p0, Z, x)
        elif c != r and I == U and start==0 and checking0(p0, Z, x) == False:
            b = b - a + 1
            a = 0
        elif c != r and I == U and start>0 :
            return False
        else:
            return False
    if a == len(p0) - 1 and b < len(k) - 1 and p0[a] not in k[b]:
        b = b-a+1
        a = 0
    if  a < len(p0) - 1 and b == len(k) -1 :
        return False
        #en son
 if checking0(p0,I,0)==False and checking0(p90,I,90)==False and checking0(p180,I,180)==False and checking0(p270,I,270)==False :
     return False
 if checking0(p0,I,0)!=False and checking0(p90,I,90)==False and checking0(p180,I,180)==False and checking0(p270,I,270)==False :
     return checking0(p0,I,0)
 if checking0(p0,I,0)==False and checking0(p90,I,90)!=False and checking0(p180,I,180)==False and checking0(p270,I,270)==False :
     return checking0(p90,I,90)
 if checking0(p0,I,0)==False and checking0(p90,I,90)==False and checking0(p180,I,180)!=False and checking0(p270,I,270)==False :
     return checking0(p180,I,180)
 if checking0(p0,I,0)==False and checking0(p90,I,90)==False and checking0(p180,I,180)==False and checking0(p270,I,270)!=False :
     return  checking0(p270,I,270)
