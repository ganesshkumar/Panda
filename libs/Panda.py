from AmazonScrapper import AmazonScrapper
from SentimentAnalyser import SentimentAnalyser
from FlipKartScrapper import FlipKartScrapper
from MongoDBClient import MongoDBClient
from TwitterAPISearch import TwitterAPISearch
from FunctionExtractor import FunctionExtractor
from CNETScrapper import CNETScrapper

class Panda:
    db_client = MongoDBClient()

    def __init__(self):
        pass

    def process(self, item):
        amazon = AmazonScrapper(item['amzn_url'])
        print ('Amazon Scrapper Done')
        flip_urls = item['flip_url'].split('|')
        flipkart = FlipKartScrapper(flip_urls[0], flip_urls[1])
        print ('Flipkart Scrapper Done')

        analyser = SentimentAnalyser()
        print ('SentimentAnalyser Initialized')
        amazon_reviews = amazon.get_all_reviews(item['amzn_hash'])
        print ('Amazon reviews retrived')
        amazon_analysis = analyser.get_sentiments(amazon_reviews['titles'])
        print amazon_analysis
        print ('Amazon Analysis Done')
        flipkart_reviews = flipkart.get_review_data(item['flip_hash'])
        print ('Flipkart reviews retrived')
        flipkart_analysis = analyser.get_sentiments(flipkart_reviews['titles'])
        print flipkart_analysis
        print ('Flipkart Analysis Done')
        item['amzn_senti'] = self.add_senti(item['amzn_senti'], amazon_analysis)
        item['amzn_hash'] = amazon_reviews['md5']
        item['amzn_rating'] = amazon_reviews['rating']

        item['flip_senti'] = self.add_senti(item['flip_senti'], flipkart_analysis)
        item['flip_hash'] = flipkart_reviews['md5']
        item['flip_rating'] = flipkart_reviews['rating']
        
        Panda.db_client.save(item);
        twitter = TwitterAPISearch()
        tweets = twitter.twitterSearch(item['title'], 100)
        print 'Done with Twitter scrapping'
        twitter_reviews = analyser.get_sentiments(tweets)

        item['twitter_senti'] = self.add_senti(item['twitter_senti'], twitter_reviews)
        print 'Done with twitter senti'
        fn_extractor = FunctionExtractor()
        feature_rating = fn_extractor.calculate_features(flipkart_reviews, amazon_reviews, twitter_reviews)
        
        if len(feature_rating) is 0:
            feature_rating = item['feature_rating']
            
        date=flipkart_reviews['date'] + amazon_reviews['dates']
        senti=flipkart_analysis['senti_list'] + amazon_analysis['senti_list']
        date_senti = {}

        for iter in xrange(0,len(date)):
            if date[iter] not in date_senti:
                date_senti[date[iter]]={'Positive':0,'Negative':0,'Neutral':0}

            date_senti[date[iter]][senti[iter]]= int(date_senti[date[iter]][senti[iter]]) + 1
        print date_senti

        item['date_rating'] = date_senti

        cnet = CNETScrapper()
        cnet.get_CNET_rating()

        Panda.db_client.save(item);
        return {'amzn_senti': item['amzn_senti'],
                'amzn_rating': item['amzn_rating'],
                'flip_senti': item['flip_senti'],
                'flip_rating': item['flip_rating'],
               }


    def add_senti(self, senti1, senti2):
        senti1['positive'] += senti2['positive']
        senti1['negative'] += senti2['negative']
        senti1['neutral'] += senti2['neutral']
        return senti1


if __name__ == "__main__":
    search_term = 'Moto G'#request.args.get('search', '', type=str)
    item = MongoDBClient().get(search_term)
    panda = Panda()
    res = panda.process(item)
