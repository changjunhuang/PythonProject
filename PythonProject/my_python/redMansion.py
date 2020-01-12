from jieba import *
#读入文本
txt=open('红楼梦.txt','r',encoding='utf-8').read()
counts={}
words=lcut(txt)
excludes={'一回','姑娘','银子','这么','几个','还有',\
          '只管','说话','问道','屋里','那些','今儿',\
          '罢了','哪里','打发','自然','外头','一回',\
          '答应','二人','今日','如此','二爷','心里',\
          '她们','不好','不过','一时','过来','不能',\
          '姐姐','大家','老爷','的话','只得','什么',\
          '一个','我们','如今','说道','那里','你们',\
          '知道','起来','这里','出来','众人','自己',\
          '一面','只见','两个','没有','怎么','不是',\
          '不知','这个','听见','这样','咱们','就是','听说',\
          '进来','东西','告诉','回来','只是','这些','不用',\
          '丫头','这些','他们','不敢','出去','所以','如何',\
          '太太','那边','这话','小丫头','人家','看见','媳妇'}
for word in words:
           if len(word)==1:
                      continue
           elif word in {'林妹妹','林姑娘','颦颦','颦儿','潇湘妃子','黛玉'}:
                      rword='林黛玉'
           elif word in {'宝玉','宝哥哥','混世魔王','遮天魔王','富贵闲人','无事忙','绛洞花王','情哥哥','多情公子'}:
                      rword='贾宝玉'
           elif word in {'凤姐','凤辣子','琏二奶奶','熙凤','凤姐儿'}:
                      rword='王熙凤'
           elif word in{'奶奶' ,'老祖宗','史太君','贾母','老太太'}:
                      rword='贾母'
           else:
                      rword=word
           counts[rword]=counts.get(rword,0)+1
for word in excludes:
           del(counts[word])           
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
           word,count=items[i]
           print('{0:<10}{1:>5}'.format(word,count))
           
