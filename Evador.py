from PIL import Image, ImageDraw, ImageFont
import time

# Load the image
image_path = 'Evador.jpg'
image = Image.open(image_path)

# Function to convert name to binary
def name_to_binary(name):
    return ''.join(format(ord(char), '08b') for char in name)

# Draw object
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

# Implement a timer
start_time = time.time()
max_time = 120  # 2 minutes

# Get the player's name within the time limit
player_name = ""
while time.time() - start_time < max_time:
    remaining_time = max_time - (time.time() - start_time)
    print(f"Time left: {int(remaining_time)} seconds", end='\r')
    time.sleep(1)
    player_name = input("Enter your name: ")
    if player_name:
        break

if not player_name:
    print("Time's up!")
else:
    # Convert name to binary and embed it in the image
    binary_name = name_to_binary(player_name)
    binary_position = (200, 400)
    draw.text(binary_position, binary_name, fill="red", font=font)

    # Display the final image with the binary name
    image.show()
