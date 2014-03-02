import re
from SentimentAnalyser import SentimentAnalyser


class FunctionExtractor:
	def __init__(self):
	    self.battery = []
            self.screen = []
            self.display = []
            self.ram = []
            self.storage = []

        def splitParagraphIntoSentences(self,paragraph):
                sentenceList = []
                sentenceEnders = re.compile('[.!,?]')
                sentenceList = sentenceEnders.split(paragraph)
		return sentenceList


	def function_analysis(self,res):
		res1=[]
		res1 =str(res)
		res1 = res1.replace("!", "")
		res1 = res1.replace("'", "")
		res1 = res1.replace("[", "")
		res1 = res1.replace("/", "")
		res1 = res1.replace("]", ".")
		res1 = res1.replace("\n", "")

		res1 = self.splitParagraphIntoSentences(res1)
		coun1 = len(res1)

		chcklist = ["battery","display","screen","ram","storage"]
		finalfeature= []
		for x in range(0,coun1):
			arr = res1[x]
			arr.lower
			if any(word in arr for word in chcklist): 
				finalfeature.append(arr)

		return finalfeature


	def function_analysis_new(self,res):
                res1=[]
                res1 =str(res)
                res1 = res1.replace("!", "")
                res1 = res1.replace("'", "")
                res1 = res1.replace("[", "")
                res1 = res1.replace("/", "")
                res1 = res1.replace("]", ".")
                res1 = res1.replace("\n", "")

                res1 = self.splitParagraphIntoSentences(res1)
                coun1 = len(res1)

                chcklist = ["battery","display","screen","ram","storage"]
                finalfeature= []
		bat = []
		disp = []
		scr = []
		ra = []
		stor = []
                for x in range(0,coun1):
                        arr = res1[x]
                        arr.lower
                        if 'battery' in arr:
				bat.append(arr)
			if 'display' in arr:
                                disp.append(arr)
			if 'screen' in arr:
                                scr.append(arr)
			if 'ram' in arr:
                                ra.append(arr)
			if 'storage' in arr:
                                stor.append(arr)
                
		return {'battery':bat,'display':disp,'screen':scr,'ram':ra,'storage':stor}


	def calculate_features(self,data1,data2,data3):
                features = self.function_analysis_new(data1)
		self.battery.extend(features['battery'])
	        self.screen.extend(features['screen'])
	        self.display.extend(features['display'])
	        self.ram.extend(features['ram'])
	        self.storage.extend(features['storage'])
	
	        features1 = self.function_analysis_new(data2)
                #print features1['battery']
		self.battery.extend(features1['battery'])
                self.screen.extend(features1['screen'])
                self.display.extend(features1['display'])
                self.ram.extend(features1['ram'])
                self.storage.extend(features1['storage'])

	        features2 = self.function_analysis_new(data2)
                #print features2['battery']
		self.battery.extend(features2['battery'])
                self.screen.extend(features2['screen'])
                self.display.extend(features2['display'])
                self.ram.extend(features2['ram'])
                self.storage.extend(features2['storage'])
		
		#print self.battery	
		senti = SentimentAnalyser()
		battery_senti = senti.get_sentiments(self.battery)
		battery_screen = senti.get_sentiments(self.screen)
		battery_display = senti.get_sentiments(self.display)
		battery_ram = senti.get_sentiments(self.ram)
		battery_storage = senti.get_sentiments(self.storage)                	
	
		return {'battery':battery_senti,'display':battery_display,'ram':battery_ram,'storage':battery_storage}
