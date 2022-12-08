import requests
import json

user_name = input('Please enter your name:')

def response(message):
    my_message = { "message": message, "from": "DVads" }
    new_json = json.dumps(my_message)
    response = requests.post('https://sigma-micro-blogging.herokuapp.com/DVads', data = new_json)
    return response

def get_blogs():
    url = f'https://sigma-micro-blogging.herokuapp.com/{user_name}'
    microBlogs = requests.get(url)
    return microBlogs.json()

def post_blogs():
    while 1:
        message = input('Give me your message. Enter "exit" to quit')
        if message == 'exit':
            break
        else:
            url = f'https://sigma-micro-blogging.herokuapp.com/{user_name}'
            data = {"message": message, "from": user_name}
            post = requests.post(url, data)
    return post

# def delete_blogs():

# def patch_blogs():
 
# print(post_blogs()) #:)


    
# In pairs, the trainees should add functionality that will let the user
# Ask the user for their name and set it
# Get the microblogs only for that username
# Post a message as that username{}
# If the trainees finish this task they should then
# Add a loop so they can keep on posting new messages
# Implement the DELETE endpoint so they can delete messages
# Implement the PATCH endpoint so they can update messages that have already been posted
