import boto3
import base64
import json
import os

def generate_image(prompt, output_dir="generated_images", image_name="output.png"):
    # Initialize AWS Bedrock client
    client = boto3.client("bedrock-runtime", region_name="us-east-1")  # Change region if needed
    
    # API request payload
    payload = {
        "textToImageParams": {"text": prompt},
        "taskType": "TEXT_IMAGE",
        "imageGenerationConfig": {
            "cfgScale": 8,
            "seed": 42,
            "quality": "standard",
            "width": 1024,
            "height": 1024,
            "numberOfImages": 1
        }
    }
    
    response = client.invoke_model(
        modelId="amazon.titan-image-generator-v1",
        contentType="application/json",
        accept="application/json",
        body=json.dumps(payload)
    )
    
    # Parse response
    response_body = json.loads(response["body"].read())
    image_data = response_body["images"][0]  # Base64 encoded image
    
    # Decode image
    image_bytes = base64.b64decode(image_data)
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, image_name)
    
    # Save image
    with open(output_path, "wb") as img_file:
        img_file.write(image_bytes)
    
    print(f"Image saved at: {output_path}")
    
# Example usage
generate_image("A futuristic city skyline at sunset")