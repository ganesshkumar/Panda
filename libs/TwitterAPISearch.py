
from TwitterSearch import *


class TwitterAPISearch:
    def twitterSearch(self,keyword,tweetCount):
        tweetList = []
        try:
            tso = TwitterSearchOrder()
            tso.setKeywords([keyword])
            #tso.setCount(7) # please dear Mr Twitter, only give us 7 results per page
            tso.setIncludeEntities(False)
            tso.setLanguage("en")

            '''ts = TwitterSearch(
                consumer_key = 'QEN0pRUDWBwz3eAnRGt4oA',
                consumer_secret = 'uPKpmdkUyEtHHYTG81hxrDe2kPybRZq8zfAnAvdrA',
                access_token = '109282672-lsdLzFwO2ybQ8f00qZG51JTcel7zTghEBa00R24c',
                access_token_secret = 'TE717i4SK6uuHUBmak8UXLaUijNH2uV1H5HbrCSnG5c'
                )'''

            ts = TwitterSearch(
                consumer_key = 'RqDsNdw2qc482AaTyAQg',
                consumer_secret = '971GEjUVvlzyYotOX44Q1wm2lx6T8QhAWcXaX2ZTz8',
                access_token = '97889597-zq5BNAWr1jrUkMb2G2iH0XGTvAfbIi8cRK2DejtxO',
                access_token_secret = 'eGCTcpvcOTdlUBfIFQ6f7IJIOrwxeYU9bX1nK27KJOw'
            )


            cnt=0
            totcnt=0
            var="Start:"
            for tweet in ts.searchTweetsIterable(tso):
                #print('@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text']))
                if cnt < tweetCount:
                    totcnt=totcnt+1
                    chk=' '.join(x for x in tweet['text'].split(' ') if x.find('http') is -1).strip()
                    if chk not in var and chk[:10] not in var:
                        print chk
                        var=var+chk+"||"
                        tweetList.append(var.strip())
                        cnt=cnt+1
                else:
                    break


        except TwitterSearchException as e: # take care of all those ugly errors if there are some
            print(e)

        return tweetList