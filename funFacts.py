import requests
from pywebio import start_server
from pywebio.output import put_text, put_button, put_html
from pywebio.session import run_js

# Function to fetch a random fact from the API
def get_random_fact():
    url = 'https://uselessfacts.jsph.pl/random.json?language=en'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if request failed
        data = response.json()
        return data['text']
    except requests.RequestException as e:
        return f"Error: Unable to retrieve fact. {e}"

# Function to display the fact and provide a button to get a new one
def fact_generator_app():
    put_html("<h1>Fun Fact Generator</h1>")
    
    # Display a fact initially
    fact = get_random_fact()
    put_text(f"Here's a fun fact: {fact}")
    
    # Button to get a new fact
    def refresh_fact():
        run_js("window.location.reload()")

    put_button("Get another fact", onclick=refresh_fact)

if __name__ == "__main__":
    # Start the PyWebIO server
    start_server(fact_generator_app, port=8080)
