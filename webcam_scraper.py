import requests
import json

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
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()  # Returns the JSON response as a dictionary
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Replace 'YOUR_API_KEY' with your actual Windy API key
# Replace 'WEB_CAM_ID' with the ID of the webcam you are interested in
api_key = 'A50nO6oyDb756hDabW5iPQHTB9j3fcXg'
webcam_id = '1561487172'

webcam_data = get_webcam_data(api_key, webcam_id)

if webcam_data:
    print("Webcam Data Retrieved Successfully:")
    print(json.dumps(webcam_data, indent=4))  #Pretty Print Implementation
else:
    print("Failed to retrieve webcam data.")
