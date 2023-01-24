# IIC_App_Backend

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
---
May cause errors with versions lower than Python 3.10
<br>

To run locally:
1. Clone this repo
2. Open terminal to the repo (can venv to create venv if u want to, definitely suggested) and run `pip install -r requirements.txt`
3. from same repo `uvicorn app.main:app --reload`
4. api will be live at `http://127.0.0.1:8000`
5. go to `http://127.0.0.1:8000/docs for SwaggerUI`
5. for login use Authorize button and not the login route (for some reason the route doesnt work in FastAPI for me...definitely doing something wrong :), but login functionality works)
<br>

There is an existing user in the db: 
- username: user1
- password: string
<br>

Still left to do:
1. OTP authentication
2. Forgot Password
3. Make admin login
4. Profile pic for team members
<br>
PS: Use TablePlus to view the db. Its a great software.
