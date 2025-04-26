word="kiwi" #case sensitive

guess=""
guess_count=1
guess_limit=3


while guess != word:
    if guess_limit >=1:
        guess=input("Try with one word")
        print(guess_limit-1," tries left")
        guess_count +=1
        guess_limit-=1
    if guess_limit<=0:
        print("You lost")
        break
if(guess==word):
    print("You won! ",guess_count-1," tries")
