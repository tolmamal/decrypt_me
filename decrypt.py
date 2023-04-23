import base64

encrypted = '=AEShtGbDBnacFHZgdnQ'

def decrypt(text, key):
    output = ''
    for i in range(len(text)):
        character = ord(text[i])
        output += chr(character ^ key)
    return str(output)

for i in range(10):
    print('key:', i, 'result = ', decrypt(base64.b64decode(encrypted[::-1]).decode('utf-8'),i), '\n\n')
