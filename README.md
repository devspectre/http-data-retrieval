# HTTP Data Retrieval and Decoding
Simple coding task to demonstrate how to retrieve and decode HTTP data.

# Requirements
- Python 3
- pip
- Virtualenv

## Install
1. Install/Activate Virtualenv for the project
    ```sh
    virtualenv venv
    source venv/bin/activate
    ```
    Here's a reference that can help you setup virtualenv.
    https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
2. Install dependencies
    ```sh
    pip install -r requirements.txt
    ```
    
## Run
To run development server, simply run the following command in your console(terminal).
```sh
flask run
```
Then go to `127.0.0.1:5000` on your browser.

# Screenshots
The first page you see will show you all subway-lines in Boston.

There you can navigate to another page by clicking the `Show stops` link which will show you all stops in that subway-line.
