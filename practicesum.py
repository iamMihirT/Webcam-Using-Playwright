import requests
import os
import json

def download_file(url, output_dir, output_name):
    """
    Downloads a file using requests and saves it into the specified directory.
    Args:
    - url (str): The URL to download from.
    - output_dir (str): The directory where the file will be saved.
    - output_name (str): The name of the output file.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_name)

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {output_path}")
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")

def extract_video_urls(webcam_data):
    return webcam_data['player']

def extract_preview_images(webcam_data):
    return {
        'current': webcam_data['images']['current']['preview'],
        'daylight': webcam_data['images']['daylight']['preview']
    }

def download_preview_images(webcam_id, preview_images, output_dir):
    for image_type, image_url in preview_images.items():
        file_name = f"{webcam_id}_preview_{image_type}.jpg"
        download_file(image_url, output_dir, file_name)

def download_videos(player_data, webcam_id, output_dir):
    periods = ['day', 'month', 'year', 'lifetime']
    for period in periods:
        file_url = player_data[period]
        file_name = f"{webcam_id}_video_{period}.html"  # Placeholder for HTML embeds
        download_file(file_url, output_dir, file_name)

def download_webcam_content(api_key, webcam_id, output_dir):
    webcam_data = get_webcam_data(api_key, webcam_id)
    if not webcam_data:
        print("Failed to retrieve webcam data.")
        return

    print("Webcam Data Retrieved Successfully:")
    print(json.dumps(webcam_data, indent=4))

    # Extract image and video data
    preview_images = extract_preview_images(webcam_data)
    player_data = extract_video_urls(webcam_data)

    # Download only the preview images (current and daylight)
    download_preview_images(webcam_id, preview_images, output_dir)

    # Download all videos inside the player
    download_videos(player_data, webcam_id, output_dir)

def get_webcam_data(api_key, webcam_id):
    """
    Parameters used for this example:
    - api_key (str): Your Windy API key.
    - webcam_id (str): ID of the webcam to fetch data for.
    
    Returns:
    - dict: Data about the webcam.
    """
    base_url = "https://api.windy.com/webcams/api/v3/webcams"
    params = {
        'include': 'images,location,player,urls',
        'lang': 'en'
    }
    headers = {
        'x-windy-api-key': api_key,
    }
    url = f"{base_url}/{webcam_id}"

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Replace 'YOUR_API_KEY' with your actual Windy API key
# Replace 'WEB_CAM_ID' with the ID of the webcam you are interested in
api_key = 'A50nO6oyDb756hDabW5iPQHTB9j3fcXg'
webcam_id = '1561487172'
output_dir = "C:\\Users\\Mihir Trivedi\\Desktop\\webcams\\downloads"
download_webcam_content(api_key, webcam_id, output_dir)
