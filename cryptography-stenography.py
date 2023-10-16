from PIL import Image

def hide_text(image_path, secret_text, output_path):
  # Open the image
  image = Image.open(image_path)

  # Convert the secret text to binary
  binary_secret_text = ''.join(format(ord(char), '08b') for char in secret_text)

  # Check if the image can accommodate the secret text
  image_capacity = image.width * image.height * 3
  if len(binary_secret_text) > image_capacity:
    raise ValueError("Image does not have sufficient capacity to hide the secret text.")
  
  # Hide the secret text in the image
  pixels = image.load()
  index = 0
  for i in range(image.width):
    for j in range(image.height):
      r, g, b = pixels[i, j]

      # Modify the least significant bit of each color channel
      if index < len(binary_secret_text):
        r = (r & 0xFE) | int(binary_secret_text[index])
        index += 1
      if index < len(binary_secret_text):
        g = (g & 0xFE) | int(binary_secret_text[index])
        index += 1
      if index < len(binary_secret_text):
        b = (b & 0xFE) | int(binary_secret_text[index])
        index += 1

      pixels[i, j] = (r, g, b)

  # Save the image with the hidden secret text
  image.save(output_path)

def extract_text(image_path):
  # Open the image
  image = Image.open(image_path)

  # Extract the secret text from the image
  pixels = image.load()
  binary_secret_text = ""
  for i in range(image.width):
    for j in range(image.height):
      r, g, b = pixels[i, j]

      # Extract the least significant bit of each color channel
      binary_secret_text += str(r & 1)
      binary_secret_text += str(g & 1)
      binary_secret_text += str(b & 1)

  # Convert the binary text to ASCII
  secret_text = ""
  for i in range(0, len(binary_secret_text), 8):
      char = chr(int(binary_secret_text[i:i+8], 2))
      secret_text += char

  return secret_text

image_path = 'geranimo-bKhETeDV1WM-unsplash.jpg'
secret_text = 'This is a super secret message.'
output_path = 'output_geranimo-bKhETeDV1WM-unsplash.jpg'
hide_text(image_path, secret_text, output_path)

# Extract the secret text from the image
extracted_text = extract_text(output_path)
print("Extracted text:", extracted_text)