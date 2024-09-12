import qrcode as qr
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        # Use urlparse to parse the URL and check if scheme and netloc are present
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# Loop to handle dynamic input
while True:
    user_input = input("Enter a URL (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break

    # Validate the input URL
    if is_valid_url(user_input):
        img = qr.make(user_input)
        img.save("QRCode.png")
        print("QR code saved as QRCode.png")
    else:
        print("Invalid URL. Please enter a valid URL.")
