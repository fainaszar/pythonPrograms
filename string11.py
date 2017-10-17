#Divive string into K parts and printing them after removing duplicate enteries of a letter.
#incomplete
def merge_the_tools(string, k):
    # your code goes here
    
    parts = len(string)/k
    sList=[]
    oList=[]
    start=0
    for i in range(parts):
        sList.append(string[start:start+parts])
        start+=3
   
    for word in sList:
        
        output=""
        
        for i in range(0,len(word)):
            count = word.count(word[i])
            
            if (count > 1) :
                output = word[::-1]
               
                output = output.replace(word[i],'',1)
                output= output.strip()
                output = output[::-1]
                
                
                
                
                
        oList.append(output)
        
            
        
    for word in oList:
        print word
        


if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    