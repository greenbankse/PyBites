cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    return ', '.join(cars['Jeep'])
print(get_all_jeeps(cars))


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [x[0] for x in cars.values()]
print(get_first_model_each_manufacturer(cars))


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    cars = ' '.join([' '.join(x) for x in cars.values()]).split(' ')
    return sorted([x for x in cars if grep.lower() in x.lower()])
print(get_all_matching_models(cars,'trail'))
print(get_all_matching_models(cars,'CO'))


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    # for make, models in cars.items():
    #     cars[make] = sorted(models)
    # return cars
    return {manufacturer: sorted(models) for
            manufacturer, models in cars.items()}
print(sort_car_models(cars))