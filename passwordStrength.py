import cohere
from cohere.classify import Example
co = cohere.Client('WgZFoDpnpQkxA80dUmDKcRivf7oYZF2VodsdynBN')
#old = input("Enter a password: ")
new = input("Enter a password: ")

response = co.classify(
    model='09856ff5-6248-44e6-811b-8d7f3b210c65-ft',
    inputs=[new]

)

print('Strength of Password: {}'.format(response.classifications))
