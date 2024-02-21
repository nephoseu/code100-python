import requests

email = "EMAIL-OR-USERNAME-HERE" # Replace with email or username given to you
password = "PASSWORD-HERE" # Replace with password given to you

# Step 1: Login
login_data = { "email": email, "password": password }
login_response = requests.post("https://challenger.code100.dev/login", json=login_data)
token = login_response.json()["token"]

# Step 2: Call Authenticated Endpoint to just check if the token is working
headers = {"Authorization": f"Bearer {token}"}
auth_response = requests.get("http://challenger.code100.dev/testauthroute", headers=headers)
print(auth_response.json(), "\n")

# Step 3: Call the API to GET the puzzle
puzzle = requests.get("https://challenger.code100.dev/getpuzzle", headers=headers)
print(puzzle.json(), "\n")

# Step 4: Solve the puzzle

########## Your code goes here ##########

answer = "some solution in the requested format"

# Step 5: Submit the solution
solution = { "answer": answer }
submit_response = requests.post("https://challenger.code100.dev/postanswer", json=solution, headers=headers)
print(submit_response.json().get("message"))