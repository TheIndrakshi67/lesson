fp=open("data.txt",'a')
t=("John", "Bixy", "Alexa")
print("Here are the elements inside tuple", t)
l=["Google", "Groq","Chatgpt"]
print("Here are the elements inside list", l)
fp.write("Here are the elements inside tuple\n")
fp.write(str(t)+"\n")
fp.write("Here are the elements inside list\n")
fp.write(str(1)+"\n")

fp.close()