import re

class FunctionExtractor:
	def __init__(self):
	    pass

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
		battery = []
		display = []
		screen = []
		ram = []
		storage = []
                for x in range(0,coun1):
                        arr = res1[x]
                        arr.lower
                        if 'battery' in arr:
				battery.append(arr)
			if 'display' in arr:
                                display.append(arr)
			if 'screen' in arr:
                                screen.append(arr)
			if 'ram' in arr:
                                ram.append(arr)
			if 'storage' in arr:
                                storage.append(arr)
                
		return finalfeature

