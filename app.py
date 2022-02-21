import requests

from flask import (
    Flask,
    request,
    render_template,
)

app = Flask(__name__)
MBTA_ROUTES_ENDPOINT = 'https://api-v3.mbta.com/routes'
MBTA_STOPS_ENDPOINT = 'https://api-v3.mbta.com/stops'


@app.route("/ht")
def health_check():
    return 'Healthy!'


@app.route("/", methods=["GET"])
def list_all_subway_lines_in_boston():
    """ Endpoint to show all routes in Boston. """
    if request.method == 'GET':
        response = requests.get(MBTA_ROUTES_ENDPOINT)
        if response.status_code == 200:
            json_data = response.json()
            data = json_data.get('data', [])

            routes = [
                {
                    'id': entry['id'],
                    'name': entry['attributes']['long_name']
                }
                for entry in data
            ]
            return render_template(
                'routes.html',
                description=f"All subway-lines in Boston ({len(routes)})",
                routes=routes
            )
        else:
            return render_template(
                'error.html',
                description=f"Failed to retrieve data: {response.status_code}: {response.reason}"
            )
    else:
        return render_template(
            'error.html',
            description=f"Only GET HTTP method is allowed for this endpoint!"
        )


@app.route("/stops/by_route/<string:line_id>", methods=["GET"])
def list_all_stops_in_subway_line(line_id):
    """
    Endpoint to list all stops on a particular subway-line
    """
    if request.method == 'GET':
        url = f"{MBTA_STOPS_ENDPOINT}?filter[route]={line_id}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json().get('data', None)
            return render_template(
                'stops.html',
                description=f"All stops in subway-line({line_id})",
                stops=data
            )
        else:
            return f"Failed to retrieve data: {response.status_code}: {response.reason}"
    else:
        return render_template(
            'error.html',
            description=f"Only GET HTTP method is allowed for this endpoint!"
        )