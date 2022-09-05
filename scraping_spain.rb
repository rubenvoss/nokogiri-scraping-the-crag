require "nokogiri"
require "open-uri"
require "pry"

doc = Nokogiri::HTML(open("./Catalan coastal ranges north, Sportklettern _ theCrag.html"))

# doc = doc.search("#areas div")

doc.search("span.primary-node-name")
# doc.each do |div|
#   div
# end


binding.pry


doc = doc.css("div.node-listview.hide-archived")
# doc = doc.css("div.area")[0]
# doc = doc.css("div.name")

doc = doc.css("span.primary-node-name")

doc = doc[0].children[0].text
# doc = doc.css("span.type")


p doc
