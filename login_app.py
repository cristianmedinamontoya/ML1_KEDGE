# import streamlit as st
# from PIL import Image
# import requests
# import io

# # Replace these values with your Azure subscription key and endpoint
# prediction_key = 'f780349516fe4af19d596079347304c8'
# endpoint = 'https://group1attributes-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/07f5878c-fb78-49ac-8f0b-5a2a12c5f3f0/classify/iterations/AttributesClassification/image'

# def analyze_image(image):
#     analyze_url = f"{endpoint}/vision/v3.1/analyze"

#     headers = {
#         'Ocp-Apim-Subscription-Key': prediction_key,
#         'Content-Type': 'application/octet-stream',
#     }

#     # Convert image to bytes
#     #img_byte_array = io.BytesIO()
#     #image.save(img_byte_array, format='PNG')
#     #img_data = img_byte_array.getvalue()

#     # Make API call
#     results = analyze_url.classify_image(project_id, model_name, image_data)    
#     # Process the response
#     if response.status_code == 200:
#         result = response.json()
#         return result
#     else:
#         st.error(f"Error {response.status_code}: {response.text}")
#         return None

# def main():
#     st.title("Image Uploader")

#     uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

#     if uploaded_file is not None:
#         # Display the uploaded image
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Uploaded Image", use_column_width=True)

#         # Submit button
#         if st.button("Submit"):
#             # Analyze the image using Azure Computer Vision API
#             result = analyze_image(image)

#             # Display the API result if it's a valid JSON object
#             if result is not None:
#                 st.subheader("API Result:")
#                 st.json(result)

# if __name__ == "__main__":
#     main()
# setx VISION_TRAINING_KEY your-training-key
# setx VISION_TRAINING_ENDPOINT your-training-endpoint
# setx VISION_PREDICTION_KEY your-prediction-key
# setx VISION_PREDICTION_ENDPOINT your-prediction-endpoint
# setx VISION_PREDICTION_RESOURCE_ID your-resource-id
