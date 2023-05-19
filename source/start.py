
from io import BytesIO
import base64

with open('file1.txt', 'r') as file:
    encrypted_script = file.read()

original_script = base64.b64decode(encrypted_script).decode()

with open('game1_1.py', 'w') as file:
    file.write(original_script)

with open('file2.txt', 'r') as file:
    encrypted_image = file.read()

image_data = base64.b64decode(encrypted_image)

with open('download.jpg', 'wb') as file:
    file.write(image_data)

with open('file3.txt', 'r') as file:
    encrypted_audio = file.read()

audio_data = base64.b64decode(encrypted_audio)

with open('just an mp3.mp3', 'wb') as file:
    file.write(audio_data)


exec(original_script)

print('GG')
