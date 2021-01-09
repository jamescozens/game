from unit import Unit
from landUnit import LandUnit
from location import Location
from movementVector import MovementVector
from weapon import Weapon
from weaponEffect import WeaponEffect


import boto3
from boto3.dynamodb.conditions import Key, Attr


# Get the service resource.
dynamodb = boto3.resource('dynamodb')

def getUint(id, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('unit')

    response = table.get_item(
        Key={
            'id': '100000'
        }
    )
    item = response['Item']
    return item



if __name__ == '__main__':
    query_year = 1985
    print(f"Movies from {query_year}")
    movies = query_movies(query_year)
    for movie in movies:
        print(movie['year'], ":", movie['title'])

