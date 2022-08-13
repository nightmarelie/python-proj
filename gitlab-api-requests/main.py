import requests

user_id = input('type user id for fetching data')

response = requests.get(f"https://gitlab.com/api/v4/users/{user_id}/projects")
my_projects = response.json()

# print the whole objects list
print(my_projects)
print(type(my_projects))

# print just the names and urls
for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['http_url_to_repo']}\n")

