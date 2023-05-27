import openai

key=openai.api_key="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"

# here you can make this prompt with speak model  pyttsx3

a=input("krapiya karke apka kam  bataye::-")
# here one things to note chatgpt model treat every words as one token and always provide a unique id to the words chat gpt has 172 billion parameter like this this is only index that is around 800  gb
# now you can imagine the size of data 
# in the chat gpt they charge you according to the token you use 



prompt="say a hindi  poem  lines for me my name is " + a  
#prompt=a
a=openai.Completion.create(prompt=prompt,model="text-davinci-003",max_tokens=1500)

#a=open("dll.c",'w')


print(a["choices"][0]['text'])

# further you can integrate with ci cd toools to 

# chatgpt---->github---->Jenkins---test------>prod


