#!/usr/bin/env ruby
#Regular Expression


# Accept one argument from the command line
input = ARGV[0]

# Define the regular expression pattern
pattern = /[A-Z]/

# Perform the regular expression matching and extract capital letters
shouted_text = input.scan(pattern).join

# Output the extracted capital letters
puts shouted_text
