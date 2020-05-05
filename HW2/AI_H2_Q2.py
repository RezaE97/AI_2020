tp=0
fp=0
fn=0
i=0
while i<10:
    try:
        inputLine=input("Set N."+str(i+1).zfill(2)+":-->")
        if inputLine[0] not in ['0','1'] or inputLine[2] not in ['0','1'] or inputLine[1]!=' ':
            raise Exception
        if inputLine[0]=='1':
            if inputLine[2]=='1':
                tp+=1
            else:
                fn+=1
        else:
            if inputLine[2]=='0':
                pass
            else:
                fp+=1
        i+=1
    except:
        print("Please enter in correct format: i.e.[1 0]")
p=tp/(tp+fp)
r=tp/(tp+fn)
F1=2*p*r/(p+r)
print("\nP  value:-->"+str(p))
print("R  value:-->"+str(r))
print("F1 value:-->"+str(F1)+'\n')