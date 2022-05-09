
email = input(" Please enter your email : ") # g@g..pk, .com

# ars laN@gmail.com

k = 0
j = 0
d = 0

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i == i.upper():
                            j=1
                    elif i == "_" or i== "." or i=="@":
                        continue
                    else:
                        d = 1
                
                if k==1 or j==1 or d==1:
                    print(" Invalid email : Spaced included, Uppercase letter, any special character ")
                else:
                    print("congratulations : Your email is valid")
            else:
                print(" Invalid email : less or more use of \".\" ")
        else:
            print(" Invalid email : less or more use of @. Limit is only 1")
    else:
        print(" Invalid email : your email is only starts with alphabets")
else:
    print(" Invalid email : your email is too short. valid email minimum length is 6")