## DEMO

### Step 1: Create a Virtual Environment

First, create a virtual environment to manage your project dependencies. You can do this using the following command:

python -m venv venv

### Step 2: Activate the Virtual Environment

Activate the virtual environment using the following command:

```
For Windows:
venv\Scripts\activate

For macOS and Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

Install the required dependencies by running:

```
pip install -r requirements.txt
```


### Step 4: Set Up Environment Variables

Copy the `.env-sample` file to a new file named `.env`:

```
cp .env-sample .env

Then, edit the `.env` file and fill in your actual values for:

- CONSUMER_ID
- APP_ID
- API_KEY
```

### Step 5: Run the Script

You can now run the main script using:

```
python main.py
```


This will execute the API calls using the Apideck Accounting API.

### Note

Make sure you have the necessary permissions and valid API credentials before running the script. The API key and other sensitive information should be kept secure and not shared publicly.
