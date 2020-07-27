# Python program to convert the currency
# of one country to that of another country

# Import the modules needed
import requests

class Currency_convertor:
	# empty dict to store the conversion rates
	rates = {}
	def __init__(self, url):
		data = requests.get(url).json()

		# Extracting only the rates from the json data
		self.rates = data["rates"]

	# function to do a simple cross multiplication between
	# the amount and the conversion rates
	def convert(self, from_currency, to_currency, amount):
		initial_amount = amount
		if from_currency != 'EUR' :
			amount = amount / self.rates[from_currency]

		# limiting the precision to 2 decimal places
		amount = round(amount * self.rates[to_currency], 2)
		print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))

# Driver code
if __name__ == "__main__":
	while True:
		YOUR_ACCESS_KEY = '52dfca127973da37ea1a1983a19dfa29'
		url = str.__add__('http://data.fixer.io/api/latest?access_key=', YOUR_ACCESS_KEY)
		c = Currency_convertor(url)
		from_country = input("\nUnited States = USD\n"
							 "Europe = EUR\n"
							 "Japan = JPY\n"
							 "England = GBP\n"
							 "Canada = CAD\n"
							 "India = INR\n"
							 "From Country: ")
		to_country = input(  "\nUnited States = USD\n"
							 "Europe = EUR\n"
							 "Japan = JPY\n"
							 "England = GBP\n"
							 "Canada = CAD\n"
							 "India = INR\n"
							 "TO Country: ")
		amount = int(input("Amount: "))

		c.convert(from_country.upper(), to_country.upper(), amount)

		quit = input('\nIf You Want Exit Press q And If You Want To Use Press u : ')
		if quit == "q" or quit == 'exit':
			break