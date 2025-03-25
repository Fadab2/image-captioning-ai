import requests
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load your image (replace with your image filename)
img_path = "image1.jpg"  # Example: "cat.jpg"
image = Image.open(img_path).convert('RGB')

# You do not need a question for image captioning
text = "the image of"
inputs = processor(images=image, text=text, return_tensors="pt")

# Generate caption (max 50 tokens)
outputs = model.generate(**inputs, max_length=50)

# Decode and print the caption
caption = processor.decode(outputs[0], skip_special_tokens=True)
print("Generated Caption:", caption)