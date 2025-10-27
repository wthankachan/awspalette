import boto3
import base64
import json
from . import summarizeprofile as sp
def customize_background(profile:str)->str:
    # Initialize AWS clients
    s3_client = boto3.client('s3')
    bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1')
    
    # S3 bucket and key
    bucket_name = 'aws-palette-stock-images--use1-az4--x-s3'
    object_key = 'shoes.png'
    
    # Read image from S3
    response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    image_data = response['Body'].read()
    image_base64 = base64.b64encode(image_data).decode('utf-8')
    user_prompt=sp.summarizeprofile(profile)
    print("User Prompt:",user_prompt)
    # Prepare request for Amazon Nova model
    request_body = {
        "taskType": "IMAGE_VARIATION",
        "imageVariationParams": {
            "text": f"Place the image in a background using the provided customer profile. Do not modify the product image in the foreground. Customer Profile: {user_prompt}",
            "images": [
                image_base64,
            ]
        }
    }
    #request_body = {
    #    "taskType": "OUTPAINTING",
    #        "outPaintingParams": {
    #            "text": "change the image background to match the given customer profile" + user_prompt,
    #            "negativeText": "do not change the main subject of the image",
    #            "image": image_base64,
    #            "maskPrompt": "change the image background to match the given customer profile" + user_prompt,
    #            "outPaintingMode": "DEFAULT"
    #        },
    #        "imageGenerationConfig": {
    #            "numberOfImages": 1,
    #            "height": 512,
    #            "width": 512,
    #            "cfgScale": 8.0
    #        }
    #    }


    # Invoke Amazon Nova model
    response = bedrock_client.invoke_model(
        modelId='amazon.nova-canvas-v1:0',
        body=json.dumps(request_body),
        contentType='application/json'
    )
    
    # Parse response
    response_body = json.loads(response['body'].read())
    output_image = response_body['images'][0]
    #output_image = response_body['imageVariations'][0]['images'][0]['bytes']
    #return base64.b64decode(output_image)
    return (output_image)

# Example usage
#if __name__ == "__main__":
#    prompt = input("Enter your background customization prompt: ")
#    customized_image = customize_background(prompt)
#    
#    with open('customized_image.png', 'wb') as f:
#        f.write(customized_image)
#    
#    print("Background customized successfully! Saved as customized_image.png")