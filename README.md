# SMS Sending System with Django and Celery

This project implements a view and form in Django for accepting phone numbers and sending SMS messages to those numbers. All sensitive data required for sending SMS messages should be obtained via environment variables.

## Integration with Celery

SMS messages are sent asynchronously using Celery tasks.

## Using Twilio.com for SMS Sending

This project utilizes Twilio.com as the SMS provider. You'll need to set up an account on Twilio and obtain the required credentials.

## Environment Variables

Ensure you have the following environment variables set:

- TWILIO_ACCOUNT_SID: Your Twilio account SID.
- TWILIO_AUTH_TOKEN: Your Twilio authentication token.
- TWILIO_PHONE_NUMBER: Your Twilio phone number.

## How to Run
1. After downloading all Python files, execute the following commands:

* `python manage.py makemigrations`

* `python manage.py migrate`

2. Install the required packages by running:

* `pip install -r requirements.txt`

3. Set the environment variables in the terminal:

* `set TWILIO_TOKEN={your token}`, where `{your token}` is your Twilio token.

4. Start the server by running:

* `python manage.py runserver`

