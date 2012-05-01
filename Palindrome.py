def palindrome(*num):
    length=len(num)
    num_9=0
    for i in xrange(length):
        if num[i]=="9":
            num_9+=1
    if num_9==length:
        q_num=""
        for i in xrange(length):
            q_num+="0"
        q_num="1"+q_num[1:]+"1"
        return q_num
    
    if length%2==1:
        if num[:length/2]>num[::-1][0:length/2]:
            num=num[:length/2]+num[length/2]+num[:length/2][::-1]
        else:
            if num[length/2]==9:
                num=str(int(num[:length/2-1])+1)+num[length/2:-1]
            else:
                num=str(int(num[:length/2+1])+1)+num[length/2+1:-1]
            num=num[:length/2]+num[length/2]+num[:length/2][::-1]             
    else:
        if num[:length/2]>num[::-1][0:length/2]:
            num=num[:length/2]+num[:length/2][::-1]
        else:
            num=str(int(num[:length/2])+1)+num[length/2+1:-1]
            num=num[:length/2]+num[:length/2][::-1]
            
    return num

count=int(raw_input())
for i in xrange(count):
    num=raw_input()
    print palindrome(num)


    
    
    