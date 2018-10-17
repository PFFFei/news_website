from django.shortcuts import render,render_to_response

# Create your views here.
from django.http import HttpResponse
from tool.models import *
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba


def plot(request):
    # Information_news = Information.objects.all()
    # Military_news = Military.objects.all()
    # Sports_news = Sports.objects.all()
    # Entertainment_news = Entertainment.objects.all()
    # Finance_news = Finance.objects.all()
    # Information_news_list = []
    # Military_news_list = []
    # Sports_news_list = []
    # Entertainment_news_list = []
    # Finance_news_list = []
    # I_num = M_num = S_num = E_num = F_num =0
    # slices = []
    # for each_I in Information_news:
    #     I_num += int(each_I.clicks)
    #     Information_news_list.append(str(each_I))
    # slices.append(I_num)
    # str_ = "".join(Information_news_list)
    # Information_news_text = ' '.join(jieba.cut(str_))

    # path = 'msyh.ttc'
    
    # wordcloud = WordCloud(font_path=path).generate(Information_news_text)
    # plt.imshow(wordcloud,interpolation='bilinear')
    # plt.axis("off")
    # plt.savefig("C:/pork/website/static/figure/Information.png")

    # for each_M in Military_news:
    #     M_num += int(each_M.clicks)
    #     Military_news_list.append(str(each_M))
    # slices.append(M_num)
    # str_ = "".join(Military_news_list)
    # Military_news_text = ' '.join(jieba.cut(str_))
    
    # wordcloud = WordCloud(font_path=path).generate(Military_news_text)
    # plt.imshow(wordcloud,interpolation='bilinear')
    # plt.axis("off")
    # plt.savefig("C:/pork/website/static/figure/Military.png")

    # for each_S in Sports_news:
    #     S_num += int(each_S.clicks)
    #     Sports_news_list.append(str(each_S))
    # slices.append(S_num)
    # str_ = "".join(Sports_news_list)
    # Sports_news_text = ' '.join(jieba.cut(str_))
    
    # wordcloud = WordCloud(font_path=path).generate(Sports_news_text)
    # plt.imshow(wordcloud,interpolation='bilinear')
    # plt.axis("off")
    # plt.savefig("C:/pork/website/static/figure/Sports.png")

    # for each_E in Entertainment_news:
    #     E_num += int(each_E.clicks)
    #     Entertainment_news_list.append(str(each_E))
    # slices.append(E_num)
    # str_ = "".join(Entertainment_news_list)
    # Entertainment_news_text = ' '.join(jieba.cut(str_))
    
    # wordcloud = WordCloud(font_path=path).generate(Entertainment_news_text)
    # plt.imshow(wordcloud,interpolation='bilinear')
    # plt.axis("off")
    # plt.savefig("C:/pork/website/static/figure/Entertainment.png")

    # for each_F in Finance_news:
    #     F_num += int(each_F.clicks)
    #     Finance_news_list.append(str(each_F))
    # slices.append(F_num)
    # str_ = "".join(Finance_news_list)
    # Finance_news_text = ' '.join(jieba.cut(str_))
    
    # wordcloud = WordCloud(font_path=path).generate(Finance_news_text)
    # plt.imshow(wordcloud,interpolation='bilinear')
    # plt.axis("off")
    # plt.savefig("C:/pork/website/static/figure/Finance.png")

    # activities = ['Information','Military','Sports','Entertainment','Finance']
    # cols = ['tan','cadetblue','y','palegreen','plum']
    # try:
    # plt.pie(slices,
    #         explode=[0,0.2,0,0,0],
    #         labels=activities,
    #         colors=cols,
    #         startangle=90,
    #         shadow=False,
    #         autopct='%1.1f%%')
    # except ValueError as e:
    #     pass
    # plt.savefig("C:/pork/website/static/figure/Total.png")
    
    return render(request,'news_plot.html')

