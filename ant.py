from faker import Faker
from random import randint
import requests

fake = Faker()

# Generate dummy blog psot
insertable = {
  'author'  : randint( 1, 50 ),
  'title'   : fake.text(),
  'snippet' : fake.sentence( nb_words = randint( 200, 300 ) ),
  'content' : fake.sentence( nb_words = randint( 350, 10000 ) ),
  'votes'   : randint( 0, 25000 )
}

requestsCounter = 0

# Descide would it send requests
try:
  feedAnt = open( './feed_ant', 'r' )
  while( feedAnt.read() == 'yes' ):
    # Send the request to leanDB server
    try:
      req = requests.post( 'http://localhost:2020', insertable )
      requestsCounter = requestsCounter + 1
      print( "Requests count: " + str( requestsCounter ) )
    except Exception as e:
      print( 'Unable to send request' )  
except Exception as e:
  print( 'Unable to feed ant!' )

print( 'Stopping the crazy ant!' )
