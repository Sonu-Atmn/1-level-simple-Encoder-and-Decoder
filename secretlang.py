import random
def ran3word():
    wrd=""
    for i in range(0,3):
        rno=random.randint(65,117)
        wrd=wrd+chr(rno)
    return wrd
def reverse(x):
    return x[::-1]

def encode():
    sentence=input("Enter your message")
    words=sentence.split()
    code_words=[]
    for i in words:
        if len(i)<=3:
            cur_word=reverse(i)
            code_words.append(cur_word)
        else:
            cur_word=ran3word()+reverse(i)+ran3word()
            code_words.append(cur_word)
            
    code_words=" ".join(code_words)
    print(code_words)
            
def decode():
    sentence=input("Enter your message")
    words=sentence.split()
    code_words=[]
    for i in words:
        if len(i)<=3:
            cur_word=reverse(i)
            code_words.append(cur_word)
        else:
            cur_word=i[3:]
            cur_word=cur_word[:-3]
            cur_word=reverse(cur_word)
            code_words.append(cur_word)
            
    code_words=" ".join(code_words)
    print(code_words)           

print("Enter your choice!!!!")
choice=int(input("1.ENCODING(press 1 to conver your message into code)\n2.DECODING(press 2 to convert your secret code into message)"))
if choice==1:
    encode()
    
elif choice==2:
    decode()
else:
    print("Exiting and deleting data.......")
    
