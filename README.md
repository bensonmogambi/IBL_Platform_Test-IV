# IBL-OpenEDX

# Open edX - Exercise
Another platform that IBL is built on is Open edX. Here’s the test:

Stand up an instance of Open edX using either the Dockerized Tutor release or our https://gallery.ecr.aws/ibleducation/ibl-edx-ce (architected using Tutor).
Develop an extension that exposes a REST API endpoint and saves a greeting from the user (secure this endpoint with OAuth2 in the same way that Open edX secures its other API endpoints). This endpoint should do the following things with the user-submitted greeting:
Log it (it should be visible in the platform’s LMS logs).
Save it in the database (the greeting should be visible from the Django Admin).
If the greeting is “hello”, then the view of this API endpoint should call the original greeting endpoint again with “goodbye” as the parameter. This is to make sure that you can write an Open edX view that can make an OAuth2-secured API call with a client ID, a client secret and an access token. Of course, if your code calls this endpoint with “hello” again then it’ll be recursive and things will crash.

Important as well to be excellent with Python as well. As a sample course, see: https://github.com/dabeaz-course/python-mastery

# Usage
#### Api Secured with OAuth2, Logs are visible in the Admin Panel.
-After forking, make sure to use the drf_api_logger 
```bash
pip install -r requirements.txt
```
-Then:
```bash
python client2.py
```
