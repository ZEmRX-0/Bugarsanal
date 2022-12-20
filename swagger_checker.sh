#!/bin/bash

# Check each URL in the input file for the presence of a Swagger API
while read -r url; do
  # Send a GET request to the URL
  response=$(curl -s "$url")
  # Search the response for the string "swagger"
  if [[ $response =~ "swagger" ]]; then
    # Print the version of the Swagger API if the string is found
    output="$url: $(echo "$response" | grep -oE "\"swagger\" *: *\"[^\"]+\"" | grep -oE "\"[^\"]+\"" | sed 's/"//g')"
    echo "$output"
    echo "$output" >> "$2"
  fi
done < "$1"

