from decimal import Decimal
import json
import boto3

# https://docs.aws.amazon.com/general/latest/gr/rande.html
# https://docs.aws.amazon.com/general/latest/gr/ddb.html



def load_movies(movies, dynamodb=None):
    if not dynamodb:
        # 52.94.24.0
        # dynamodb.eu-west-1.amazonaws.com
        # eu-west-1
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://dynamodb.eu-west-1.amazonaws.com")

    table = dynamodb.Table('Movies')
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        print("Adding movie:", year, title)
        table.put_item(Item=movie)


if __name__ == '__main__':
    #with open("moviedata.json") as json_file:
     #   movie_list = json.load(json_file, parse_float=Decimal)
    #load_movies(movie_list)