#!/usr/bin/env rubyi
#Regular expression

i# Accept one argument from the command line
input = ARGV[0]

# Extract sender, receiver, and flags using regular expressions
sender = input.match(/\[from:([^\]]+)\]/)&.captures&.first
receiver = input.match(/\[to:([^\]]+)\]/)&.captures&.first
flags = input.match(/\[flags:([^\]]+)\]/)&.captures&.first

# Output the sender, receiver, and flags
puts "#{sender},#{receiver},#{flags}"
