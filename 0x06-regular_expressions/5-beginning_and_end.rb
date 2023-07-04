#!/usr/bin/env ruby
#Regular Expression

# Get the argument from the command line
input = ARGV[0]

# Define the regular expression pattern
pattern = /^h.n$/

# Perform the matching
if input.match(pattern)
  puts input
else
  puts ""
end
