# 🖼️ Image Captioning AI App with BLIP and Gradio

This is a simple yet powerful image captioning web application built with Python, [BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base), and [Gradio](https://gradio.app/). It automatically generates descriptive captions for uploaded images using a pre-trained vision-language transformer model.

---

## 🚀 Demo

![demo](images/demo-screenshot.png) <!-- Optional: Add a screenshot here -->

Try it locally by uploading an image, and the app will instantly generate a caption!

---

## 🧠 How It Works

This app uses:

- **BLIP (Bootstrapping Language-Image Pretraining)** from Hugging Face for image captioning
- **Gradio** for a lightweight, interactive web UI
- **PIL (Pillow)** to handle image data
- **Transformers** for model access and inference

---

## 📦 Features

- 🧠 Automatically generates human-readable image captions
- ⚡ Easy-to-use Gradio interface
- 🌐 Can be adapted to run in cloud, local, or integrated into web apps
- 📝 Includes a version for scraping images from webpages using BeautifulSoup

---

## 📁 Project Structure

```bash
/home/project/
│
├── image_cap.py                # Simple image captioning with BLIP
├── image_captioning_app.py     # Gradio-powered web app
├── automate_url_captioner.py   # Bonus: Auto-captioning from webpage images
├── image1.jpg                  # Sample image
├── my_env/                     # Virtual environment (not tracked)
├── captions.txt                # Output from URL captioning script
└── README.md
