import ollama
from pydantic import BaseModel



file_path = "./list_of_produts"


# List models
models = ollama.list()

 #print(models)

chat = ollama.chat(
    model="gemma3:1b", 
                   messages=[{
                       "role" : "user", "content" : """
                       Write me in this file a list of products I should buy 
                       based on my goal of maintain high energy every day with budget"""
                       #"system" : "Lawyer James", "" 
                       }])


print(type(chat))

"""test = chat["message"]["content"]
print(type(test))"""
#chat(["message"]["content"])
#print(chat["message"]["content"])
#print(chat)
"""
with open(file=file_path, mode="w") as file:
    try: 
        file.write(resposne)
        file.close()
    except Exception as Error:
        print(Error)
        file.close()

"""