from flask import Flask, render_template, request
import requests

app = Flask(__name__)
OPENTRIPMAP_API_KEY = "5ae2e3f221c38a28845f05b674e8e9fbb58d2f82cbacb8004ddf08c9"
PIXABAY_API_KEY = "47011732-d44aa39b2300e4adeb1302b29"

def search_places(city):
    # OpenTripMap request to get location data and nearby places
    base_url = "https://api.opentripmap.com/0.1/en/places/geoname"
    search_url = f"{base_url}?name={city}&apikey={OPENTRIPMAP_API_KEY}"
    
    response = requests.get(search_url)
    if response.status_code != 200:
        print("Error fetching city data:", response.status_code, response.text)
        return []

    city_data = response.json()
    lon = city_data.get('lon')
    lat = city_data.get('lat')
    
    if not lon or not lat:
        print("City data is missing longitude/latitude.")
        return []

    # Get places near the city location
    places_url = f"https://api.opentripmap.com/0.1/en/places/radius?radius=5000&lon={lon}&lat={lat}&apikey={OPENTRIPMAP_API_KEY}"
    places_response = requests.get(places_url)
    
    if places_response.status_code != 200:
        print("Error fetching places data:", places_response.status_code, places_response.text)
        return []

    places = places_response.json().get('features', [])
    for place in places:
        place_name = place['properties'].get('name')
        place['image_url'] = get_image_url(place_name)
    
    return places

def get_image_url(query):
    # Pixabay API request to get images related to the place name
    image_url = f"https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={query}&image_type=photo&per_page=3"
    response = requests.get(image_url)
    if response.status_code == 200:
        data = response.json()
        if data['hits']:
            return data['hits'][0]['webformatURL']
    return "https://via.placeholder.com/150"  # Placeholder if no image found

@app.route('/', methods=['GET', 'POST'])
def index():
    places = []
    if request.method == 'POST':
        city = request.form['city']
        places = search_places(city)
    return render_template('index.html', places=places)

if __name__ == '__main__':
    app.run(debug=True)
