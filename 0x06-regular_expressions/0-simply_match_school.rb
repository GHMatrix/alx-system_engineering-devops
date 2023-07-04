#!/usr/bin/env ruby
#Regular Expression

# Get the argument from the command line
input = ARGV[0]

# Define the regular expression pattern
pattern = /School/

# Perform the matching and extract all matches
matches = input.scan(pattern)

# Join the matches into a single string
output = matches.join

# Output the result
puts output
