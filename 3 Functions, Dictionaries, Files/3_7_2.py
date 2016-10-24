plaintext = input()
code = input()
plaintext_to_code = input()
code_to_decode = input()

result_code = ''
result_plaintext = ''

forward = {}
reverse = {}

for i in range(len(plaintext)):
    forward.update({plaintext[i]: code[i]})
for i in range(len(plaintext)):
    reverse.update({code[i]: plaintext[i]})


for i in range(len(plaintext_to_code)):
    result_code += forward[plaintext_to_code[i]]
for i in range(len(code_to_decode)):
    result_plaintext += reverse[code_to_decode[i]]

print(result_code)
print(result_plaintext)