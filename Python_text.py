import requests,bs4,xlwt,xlrd,os,sys,time
from pandas import DataFrame;
from urllib.request import quote


school_name = input('请输入学校名称，可输入单个字符来匹配：')   #学校名称
address_name  = input('请输入地区名称，需完全正确：')  #地区名称
grade_name = input('请输入学级，例如"高中"等：')   #学级名称
Timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time())))
#http://xuexiao.eol.cn/?cengci=%E9%AB%98%E4%B8%AD_cengci&keywords=%E5%8C%97%E4%BA%AC&local1=%E5%8C%97%E4%BA%AC_local1&local2=

def save(names,links):
    df = DataFrame({
        '学校名称': [names],
        '链接': [links]
    })
    df.to_csv(
        "~/Downloads/" + Timestamp + ".csv", mode='a', header=False
    )

def print_school_name(url):
    #url = 'http://xuexiao.eol.cn/?cengci=' + quote(grade_name.encode('utf-8')) + '_cengci&keywords=' + quote(school_name.encode('utf-8')) + '&local1=' + quote(address_name.encode('utf-8')) + '_local1&local2='
    #搜索结果第一页；
    url = url
    res = requests.get(url).content.decode('utf-8')
    bsurl = bs4.BeautifulSoup(res,'html.parser')
    link = bsurl.select('.right_box a')
    for i in link:
        print(str(i.get('href')) + ' ' + str(i.get_text()))
        name = str(i.get_text())
        link = str(i.get('href'))
        save(name,link)



def fanye(num):
    url = 'http://xuexiao.eol.cn/?cengci=' + quote(grade_name.encode('utf-8')) + '_cengci&keywords=' + quote(
        school_name.encode('utf-8')) + '&local1=' + quote(address_name.encode('utf-8')) + '_local1&local2='
    print_school_name(url)
    list = requests.get(url).content.decode('utf-8')
    bslist = bs4.BeautifulSoup(list,'html.parser')
    page_num = bslist.select('.page font')
    num_list = page_num[0].get_text() #获取搜索的学校数量；
    num_page = round(int(num_list)//int(5)) + int(1)
    for i in range(1,num_page):
        url2 = 'http://xuexiao.eol.cn/?page=' + quote(str(i)) + '&amp;cengci=' + quote(grade_name.encode('utf-8')) + '_cengci&amp;local1=' + quote(school_name.encode('utf-8')) + '_local1&amp;keywords=' + quote(address_name.encode('utf-8'))
        print_school_name(url2)
        #save(str(i.get_text()),str(i.get('href')))

    #for x in range

fanye(1)
