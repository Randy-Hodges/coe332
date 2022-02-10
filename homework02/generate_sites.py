#!/usr/bin/env python3

import json
import random

def generate_landing_sites(num_sites: int):
    '''
    Generates five landing sites with random latitudes (between 16.0 - 18.0 degrees North) and 
    longitudes (between 82.0 - 84.0 degrees East). Also includes a random meteorite composition 
    from the list ["stony", "iron", "stony-iron"].

    Args:
        num_sites (int): number of sites to be generated.

    Generates:
        A json file with one key, “sites”, whose value is a list of dictionaries.
    '''
    # (could 100% be parameters, but I don't feel like writing docstrings about these values atm)
    deg_north_lower = 16.0
    deg_north_upper = 18.0
    deg_east_lower = 82.0
    deg_east_upper = 84.0
    meteorite_list = ["stony", "iron", "stony-iron"]

    site_dict = {
        "sites": []
    }

    for site_id in range(1, num_sites + 1):
        # Create landing site
        temp_dict = {}
        temp_dict["site id"] = site_id
        temp_dict["latitude"] = random.uniform(deg_north_lower, deg_north_upper)
        temp_dict["longitude"] = random.uniform(deg_east_lower, deg_east_upper)
        temp_dict["composition"] = meteorite_list[random.randint(0,2)]
        # Append landing site to site_dict
        site_dict["sites"].append(temp_dict)

    # Put site_dict into a json file
    with open("landing_sites.json", "w") as f:
        json.dump(site_dict, f)

if __name__ == '__main__':
    generate_landing_sites(5)










