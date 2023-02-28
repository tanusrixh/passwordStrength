import cohere

co = cohere.Client('yourAPIKey')

new = input("Enter a password: ")

response = co.classify(
    model='09856ff5-6248-44e6-811b-8d7f3b210c65-ft',
    inputs=[new]

)

print('Strength of Password: {}'.format(response.classifications))
