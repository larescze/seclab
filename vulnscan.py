import shodan

SHODAN_API_KEY = "eY6WEXyeE95XcmlQjARZZ4u6aO6xJGcF"

api = shodan.Shodan(SHODAN_API_KEY)

# Wrap the request in a try/ except block to catch errors
try:
    # Search Shodan
    results = api.exploits.search('SQLi Apache', page=1)

    # Show the results
    print('Results found: {}'.format(results['total']))
    for result in results['matches']:
        print('Exploit ID: {}'.format(result['_id']))
        print('Source: {}'.format(result['source']))
        print('Description: {}'.format(result['description']))
        print('')
except shodan.APIError as e:
    print('Error: {}'.format(e))
