#!/usr/bin/env ruby
# A regex matches only capital letters
puts ARGV[0].scan(/[A-Z]/).join
