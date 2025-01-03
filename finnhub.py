import requests
from utilities import get_data

def get_all_stocks(api_key,base_url):
	# Get all stock symbols available
	stock_symbols_url = f"{base_url}/stock/symbol?exchange=US&token={api_key}"
	results=get_data(stock_symbols_url)
	
	return results

def get_stock_groups(symbols, keywords):
	# Filter for tech and AI-related stocks
	matched_stocks = {}
	for symbol in symbols:
		# Use "type" and "description" fields to filter stocks
		description = symbol.get("description", "").lower()
		if any(keyword.lower() in description for keyword in keywords):
			#print(symbol['description'], symbol['symbol'])
			matched_stocks[symbol['symbol']]=symbol['description']

	return matched_stocks
