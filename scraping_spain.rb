require "nokogiri"
require "open-uri"
require "pry"

binding.pry
doc = Nokogiri::HTML(open("https://www.thecrag.com/de/klettern/spain/barcelona-area"))
