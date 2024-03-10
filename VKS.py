import json
from vkOsint import vkOsint

username = 'login/number'  # Your VK login
password = 'pass'  # Your VK password
phone_number = input("Enter number: ") 

vk_instance = vkOsint()
vk_instance.login(username=username, password=password)

parsed_data = vk_instance.osint(phoneNumbers=[phone_number])

for phone, user_info in parsed_data.items():
    if user_info.get("found"):
        user = user_info["response"]
        vk_url = f"https://vk.com/id{user['id']}"
        print(f"Information about {phone}:")
        print(f"Full name: {user.get('first_name', 'Nothing')} {user.get('last_name', 'Nothing')}")
        followers = user.get("counters", {}).get("followers", "Nothing")
        print(f"Followers: {followers}")

        print(f"City: {user.get('city', {}).get('title', 'Nothing')}")
        print(f"Country: {user.get('country', {}).get('title', 'Nothing')}")
        print(f"School: {', '.join(school.get('name', '') for school in user.get('schools', [])) or 'Nothing'}")
        print(f"Birth day: {user.get('bdate', 'Nothing')}")
        print(f"Profile link: {vk_url}")
        print("-" * 30)
    else:
        print(f"Information about {phone} not found")
