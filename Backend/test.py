from utils import processing_function, get_chat_response, image_generating_function_quantity, show_image, image_generating_function_object, image_generating_function_action, identify_parts

parts = identify_parts("take 2 pills daily for 14 days")

print(parts)

url = image_generating_function_action(parts[0])
show_image(url)

url = image_generating_function_quantity(parts[1])
show_image(url)

url = image_generating_function_object(parts[2])
show_image(url)