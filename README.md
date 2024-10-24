# Flask-React Web App Instructions

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup Python Virtual Environment](#setup-python-virtual-environment)
3. [Install Backend Dependencies](#install-backend-dependencies)
4. [Setup Frontend (Node & NPM)](#setup-frontend-node--npm)
5. [Running the Flask App](#running-the-flask-app)
6. [Testing the Setup](#testing-the-setup)
7. [Troubleshooting](#troubleshooting)
8. [Summary](#summary)

## Prerequisites

- Python 3.x
- Node.js and npm
- (Optional) Virtual Environment setup tools

## Setup Python Virtual Environment

1. Navigate to the `backend` directory:
   ```sh
   cd backend
   ```

2. Set up a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate    # For Windows
   ```

## Install Backend Dependencies

1. With the virtual environment activated, install the required Python dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Setup Frontend (Node & NPM)

1. Navigate to the `frontend` directory:
   ```sh
   cd frontend
   ```

2. Install dependencies using npm (ensure Node.js and npm are installed on your system):
   ```sh
   npm install
   ```

3. Run the React development server:
   ```sh
   npm start
   ```
   This will run the React frontend at [http://localhost:3000](http://localhost:3000). Make sure to keep this terminal window open while running the app.

## Running the Flask App

1. Navigate to the `backend` directory (if not already there):
   ```sh
   cd backend
   ```

2. Run the Flask development server:
   ```sh
   flask run
   ```
   The Flask backend should now be running at [http://localhost:5000](http://localhost:5000).

## Testing the Setup

1. Open your web browser and navigate to [http://localhost:3000](http://localhost:3000).
   - The frontend React application should be loaded.

2. Interact with the web application to confirm that data can be successfully retrieved from the Flask backend.
   - You may want to open the browser's developer console to check for any network errors.

3. Verify that both servers are running without errors (React on port 3000 and Flask on port 5000).

## Troubleshooting

- **CORS Issues**: If there are CORS errors in the console, ensure that Flask is configured to handle CORS by installing and using the `flask-cors` library:
  ```sh
  pip install flask-cors
  ```
  Add the following to `backend/app.py`:
  ```python
  from flask_cors import CORS
  CORS(app)
  ```

- **React Server Not Running**: Ensure the frontend dependencies were installed properly using `npm install`. Check for any errors in the terminal when running `npm start`.

- **Virtual Environment Issues**: If you have trouble activating the virtual environment, ensure that the virtual environment was created successfully. On Windows, you may need to adjust execution policy settings to run scripts.

## Summary

- Set up the frontend by installing dependencies and running the development server.
- Set up the backend by creating a virtual environment, installing dependencies, and running the Flask server.
- Test the integration between the frontend and backend by navigating to [http://localhost:3000](http://localhost:3000) and interacting with the app.
- Refer to the troubleshooting section if you run into any issues.

### Next Steps
If you need further instructions or face any additional challenges, feel free to reach out or consult relevant documentation for Flask or React. Enjoy building your web application!
