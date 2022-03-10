import json

import pandas as pd


def main() -> None:
    
    #  Load files into pandas
    restaurant_info = pd.read_csv('dataset/restaurants_info.csv', sep=';')
    restaurant_list = pd.read_json('dataset/restaurants_list.json')
    restaurant = restaurant_list.merge(restaurant_info, on='objectID', how='left')

    #  List of available payment options
    payement_list = ['Visa', 'MasterCard', 'AMEX', 'Discover', 'Diners Club', 'Carte Blanche']
    
    #  Clean options payment
    restaurant['payment_options'] = restaurant.payment_options.apply(lambda x: intersection(x, payement_list))
   
    #  Drop useless columns
    restaurant = restaurant.drop(columns=['phone', 'phone_number', 'address', 'dining_style', 'state', 'price',
                                          'country', 'postal_code'])
    
    #  Save as json format
    restaurant_json = restaurant.to_json(orient="records")

    #  Check that json format is correct and improve indent
    restaurant_parsed = json.loads(restaurant_json)
    restaurant_output = json.dumps(restaurant_parsed, indent=4)
    
    # Write output un file
    with open('restaurants.json', 'w') as output_file:
    	output_file.write(restaurant_output)
    

def intersection(payment_available, payment_list) -> list:
    return list(set(payment_available) & set(payment_list))

if __name__ == "__main__":
    main()
