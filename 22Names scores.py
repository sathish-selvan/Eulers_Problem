# needed names.txt file so its pending 
name = "SATHISH,SOWMYA"
names = list(map(str,name.split(",")))
names.sort()
print(names)
st = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
lis = list(map(str,st.split(",")))
SCORES = []
count = 1
for name in names:
    SCORE = 0
    for i in name:
        SCORE += lis.index(i) +1
    
    SCORES.append(SCORE * count )
    count += 1
print(sum(SCORES))
