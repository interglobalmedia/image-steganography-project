from PIL import Image
from hide_text import output_path

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

# Extract the secret text from the image
extracted_text = extract_text(output_path)
print("Extracted text:", extracted_text)