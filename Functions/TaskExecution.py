from Functions.TakeCommand import takeCommand
import Features.Search.YoutubeSearch as ys
import Features.Search.GoogleSearch as gs
import Features.Search.ScrapData as sd
import Features.Search.HowTo as ht
import Features.Search.SearchWiki as sw
import Features.Open.OpenSoftware as os
import Features.Email.SendEmail as se

#Task execution function
def taskExe():
    while True:
        query = takeCommand()
        Query = query.replace("david ","")

        if 'google search' in query:
            query = Query.replace("google search ","")
            print(f": {query}")
            gs.googleSearch(query)

        elif 'youtube search' in query:
            print(f": {query}")
            ys.youTubeSearch()
        
        elif 'extract data' in query:
            print(f": {query}")
            sd.scrapData()
        
        elif 'how to' in query:
            print(f": {query}")
            ht.howTo(Query)

        elif 'wikipedia' in query:
            print(f": {query}")
            sw.searchWiki()

        elif 'open software' in query:
            print(f": {query}")
            os.openSoftware()

        elif 'send email' in query:
            print(f": {query}")
            se.get_email_info()

