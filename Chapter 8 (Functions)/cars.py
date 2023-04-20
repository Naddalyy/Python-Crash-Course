def make_car(manufacturer, model_name, **car_info):
    """Builds a dictionary containing everything we know about a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)