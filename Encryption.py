import random
import string

#-------------------------------------------------------------------------                                Part of Encryption            -------------------------------------------------------------------------


alpha =string.ascii_letters+string.digits+string.punctuation
user_input= input('enter the message for Encryption: ')

total_enqryption = []
key_enqryption = []
for i in user_input :
    if i == ' ':
        total_enqryption.append(i)
    if i != ' ' :
        rand = random.randrange(1,61)
        inde = (alpha.index(i) + rand) % len(alpha)
        key_enqryption.append(rand)
        enq = alpha[inde]

        total_enqryption.append(enq)

for i in key_enqryption :
    if i >= 61 :

        key_enqryption.remove(i)
        key_enqryption.append(1)
print(''.join(total_enqryption))





#-------------------------------------------------------------------------                                Part of Decryption            -------------------------------------------------------------------------





decryption = []
key= 0
inp = input("Enter the message to decryption : ")
for i in inp :
    if i == ' '  :
        decryption.append(i)
    if i != ' ' :


        cul = alpha.index(i) - key_enqryption[key]

        tot = alpha[cul]
        key+=1

        decryption.append(tot)

print(f'Here is the message: {''.join(decryption)}')