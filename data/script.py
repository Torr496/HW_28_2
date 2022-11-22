import pandas as pandas

from ads.models import Ad, Category
from users.models import Location, User

data_ads = pandas.read_csv('ads.csv', sep=",").to_dict()
print(data_ads)

i = 0

while max(data_ads['id'].keys()) > i:
    ad = Ad.objects.create(
        name=data_ads["name"][i],
        author=data_ads["author"][i],
        price=data_ads["price"][i],
        description=data_ads["description"][i],
        address=data_ads["address"][i],
        is_published=data_ads["is_published"][i],
    )

    print(data_ads['Id'][i])
    i += 1

data_categories = pandas.read_csv('categories.csv', sep=",").to_dict()
print(data_categories)

i = 0

while max(data_categories['id'].keys()) > i:
    categories = Category.objects.create(
        name=data_categories["name"][i],
    )

    print(data_categories['Id'][i])
    i += 1

data_locations = pandas.read_csv('location.csv', sep=",").to_dict()
print(data_locations)

i = 0

while max(data_locations['id'].keys()) > i:
    locations = Location.objects.create(
        name=data_locations["name"][i],
        lat=data_locations["lat"][i],
        lng=data_locations["lng"][i],
    )

    print(data_locations['Id'][i])
    i += 1

data_user = pandas.read_csv('user.csv', sep=",").to_dict()
print(data_user)

i = 0

while max(data_user['id'].keys()) > i:
    user = User.objects.create(
        first_name=data_user["first_name"][i],
        last_name=data_user["last_name"][i],
        user_name=data_user["user_name"][i],
        password=data_user["password_name"][i],
        role=data_user["role"][i],
        age=data_user["age"][i],
        locations=data_user["locations"][i],
    )

    print(data_user['Id'][i])
    i += 1