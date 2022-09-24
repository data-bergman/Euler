quote = "they stumble who run fast"
start = 0
space_index = quote.find(" ")

while space_index != len(quote):

    space_index = start+quote[start:].find(" ")+1
    if(space_index==start):
        space_index=len(quote)
    else: space_index-=1
    print(quote[start:space_index])
    start=space_index+1