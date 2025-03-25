import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Step 2: Load the BLIP model and processor
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Step 3: Define the image captioning function
def caption_image(input_image: np.ndarray):
    # Convert numpy array to PIL Image and convert to RGB
    raw_image = Image.fromarray(input_image).convert('RGB')
    
    # Prepare input for the model
    text = "the image of"
    inputs = processor(images=raw_image, text=text, return_tensors="pt")
    
    # Generate caption
    output = model.generate(**inputs, max_new_tokens=50)
    
    # Decode the result
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption

# Step 4: Create the Gradio interface
iface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(type="numpy"),
    outputs="text",
    title="🖼️ Image Captioning App",
    description="Upload an image to generate a caption using BLIP model."
)

# Step 5: Launch the app
iface.launch(share=True)  # Set share=True to get a public link
