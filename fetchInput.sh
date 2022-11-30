#!/bin/bash

DAY=$(date +"%-d")
echo "Pulling input for day $DAY"
wait 2
OUTPUT="./Day $DAY/$DAY.txt"
echo "Writing to file: $OUTPUT"

URL="https://adventofcode.com/2021/day/$DAY/input"
SESSION="53616c7465645f5ffdcaa8788f0650641680efa30a34dbc63d25036840085ce7f207a859d4e2799933e494fb33c3e1ba"

curl --location --request GET "$URL" --header "Cookie: session=$SESSION" -o "$OUTPUT"
echo "Happy Solving :)"

wait 3