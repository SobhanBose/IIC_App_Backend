# IIC_App_Backend

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
---
May cause errors with versions lower than Python 3.10
<br>

To run locally:
1. Clone this repo
2. Open terminal to the repo (can use venv to create venv if u want to, definitely suggested) and run `pip install -r requirements.txt`
3. from same repo `uvicorn app.main:app --reload`
4. api will be live at `http://127.0.0.1:8000`
5. go to `http://127.0.0.1:8000/docs` for SwaggerUI
5. for login use Authorize button and not the login route(thats just there to generate JWT and will be hidden in the production version)
<br>

I don't remember the username and password of the user in db so please make a new one🙂


Still left to do:
1. OTP authentication
2. Make admin login
3. Profile pic for team members

<br>
PS: Use TablePlus to view the db. Its a great software.
<br>
PS: Didn't use a remote db cause Heroku now makes you add a payment method to start a project😒
