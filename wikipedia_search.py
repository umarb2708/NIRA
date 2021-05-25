import wikipedia

def search_in_wiki(query):
    query=query.replace("wiki","").replace("wikipedia","").replace("about","")
    return wikipedia.summary(query, sentences=2)
