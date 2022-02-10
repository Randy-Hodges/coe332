#!/bin/bash

echo "Generating landing sites..."
python3 generate_sites.py 
echo "Running research..."
python3 calculate_trip.py