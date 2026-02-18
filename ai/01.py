import tiktoken

eco = tiktoken.encoding_for_model("gpt-4o")

text = "Gaurav"
token = eco.encode(text)
print("Token", token)

decodedToken = eco.decode([2225, 330, 407])

print("Decoded token:", decodedToken)