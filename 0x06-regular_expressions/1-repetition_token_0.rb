#!/usr/bin/env ruby
#Regular expression

# Script file: regex_match.rb

# Accept one argument from the command line
input = ARGV[0]

# Define the regular expression pattern
pattern = /hbt{2,5}n/

# Perform the regular expression matching
if input.match?(pattern)
  puts "Input matches the pattern!"
else
  puts "Input does not match the pattern."
end
