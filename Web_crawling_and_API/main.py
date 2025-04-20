##############################################################################
### We will building a relatively simple API and serving it on our local   ###
### machine (localhost). People have built APIs with Python for some time, ###
### and packages such as flask have been popular for doing so. However, in ###
### the last few years FastAPI has become a very popular solution for this,###
### and will be our chosen package.                                        ###
##############################################################################

# Before you start, you need to install FastAPI and Uvicorn
# Uvicorn is an ASGI (Asynchronous Server Gateway Interface) server implementation for Python. 
# It's designed to be fast, lightweight, and efficient, particularly when working with asynchronous web frameworks like FastAPI.
# That mean, we will build an API with FastAPI and then we will run our FastAPI with uvicorn.

# !pip install fastapi uvicorn

from fastapi import FastAPI

# First, we will make some data that can be served from our API
datastore = {1001: {"name": "Jordan Bruno", "teacher_rank": 7},
			1002: {"name": "Liping Zheng", "teacher_rank": 2}, 
			1003: {"name": "Mark Bonnett", "teacher_rank": 5}
			}

# Initialise the FastAPI application
app = FastAPI()

# Create a root endpoint
# In this case we will trigger this function anytime a user hits the endpoint /all.
@app.get("/all")
async def get_all():
	return datastore

# Create an endpoint with a path parameter
# We would more likely want users to be able to select specific data rather than everything, 
# and we can do this by having them pass information (e.g. ids, names, etc.) in the request (the endpoint).
@app.get("/ids/{id}")
async def get_by_id(id: int):
	try:
		return datastore[id] # subset the dictionary by the ID
	except:
		return "No records found" # return if key does not exist

@app.get("/names/{name}")
async def get_by_name(name):
	output = "No records found" # placeholder if no value matched
	for sid in datastore:
		if datastore[sid]['name'] == name: # match by the name value
			output = datastore[sid] # replace placeholder with record
	return output

# By creating the above two functions, we can call the data by id or by name.
# For example, if we made the API call to /ids/1001, then we will get the data of Jordan Bruno; 
# if we made the API call to /names/Jordan Bruno, then we will get the data of Jordan Bruno again.

# How to run this application? You will need to do it in terminal locally
# save this file as main.py in a folder locally
# Open the terminal and change the directory (cd) to the folder where you have this file
# run with: uvicorn main:app --reload
