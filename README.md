# url-shortener

This is an excercise, created to practice Flask. This app is far from ready and is in development.

#### Done:
The app is currently redirecting links that are hardcoded in a python dictionary.
There is also a simple homepage and a 404 page.

#### How to run the app:
Clone the repository, export the FLASK_APP environment variable:
```
export FLASK_APP=logic.py
$ flask run
```

#### List of features to be added / to do:

*DB*
* configure a db
* use db to search for urls

*FUNCTIONALITY*
* integrate admin page
* see a table of all addresses and shortenings from the admin page
* make possible to add short_url and a redirection page through an admin page
 
*TESTS*
* testing the above
