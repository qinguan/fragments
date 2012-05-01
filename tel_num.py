import string
import os 
chartonum = {"a":"2",
             "b":"2",
             "c":"2",
             "d":"3",
             "e":"3",
             "f":"3",
             "g":"4",
             "h":"4",
             "i":"4",
             "j":"5",
             "k":"5",
             "l":"5",
             "m":"6",
             "n":"6",
             "o":"6",
             "p":"7",
             "q":"7",
             "r":"7",
             "s":"7",
             "t":"8",
             "u":"8",
             "v":"8",
             "w":"9",
             "x":"9",
             "y":"9",
             "z":"9"
             }
def lettertonum(str):
    num=""
    for letter in str:
        num += chartonum[letter]
    return num

def input_table(input):
    new_input = {}
    for item in input:
        new_input[item]=lettertonum(item)
    return new_input 

#input1 = ["aaa","ddd"]
#input2 = ["666"]
print "please input letters :"
a = raw_input()
input1 = a.split(",")
print "please input numbers :"
b = raw_input()
input2 = b.split(",")
print "waiting..."
#print input_table(input1)

#myfile = file("test.txt","w")

flag = 0
for item in input2:
    for key,val in input_table(input1).items():
        if item == val:
            flag = 1
            print key + ":" + val
           # print >> myfile , key + ":" + val
    if flag == 0:
        print item + " : there is no result!" 
        #print >> myfile , "there is no result!" 
    flag = 0
os.system('pause')

        
        
table = {"1":"",
         "2":["a","b","c"],
         "3":["d","e","f"],
         "4":["g","h","i"],
         "5":["j","k","l"],
         "6":["m","n","o"],
         "7":["p","q","r","s"],
         "8":["t","u","v"],
         "9":["w","x","y","z"]
         }

