import requests,bs4,time,re,random
from urllib.request import quote
from pandas import DataFrame

query = input('请输入需要获取的职位名称：')  #搜索职位关键词
city_id = '101210100'  #杭州城市id即为101210100；
industry = ''   #行业
Timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))   #获取当前时间
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1',
    'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'
]

headers ={
    'User-Agent': random.choice(USER_AGENTS)
}


def fanye(num):
    a = 1
    while a < (num//100 + int(1)):
        a = a + 1
        url = 'https://www.xicidaili.com/nn/' + str(a)
        res = requests.get(url, headers=headers, timeout=5).content.decode('utf-8')
        bs4_res = bs4.BeautifulSoup(res, 'html.parser')
        print('正在获取' + url + '链接的ip信息；')
        time.sleep(3)
        #print(bs4_res)
        for i in range(1,101):
            ip = bs4_res.select('table tr')[i]
            bs4_ip = bs4.BeautifulSoup(str(ip),'html.parser')
            ip_source = bs4_ip.select('td')
            ip_num = ip_source[1].getText()  #ip地址
            ip_port = ip_source[2].getText()  #ip端口
            ip_adress = ip_source[3].getText()  #ip地区
            ip_hide = ip_source[4].getText()  #ip是否匿名
            ip_types = ip_source[5].getText()  #ip类型
            #ip_speed = ip_source[6].getText()  #ip速度
            #ip_connect_time = ip_source[7].getText() #ip连接时间
            ip_Survive_time = ip_source[8].getText() #ip存活时间
            ip_verification_time = ip_source[9].getText()  #验证时间
            print(ip_num + ':' + ip_port + ':' + ip_adress + ':' + ip_hide + ':' + ip_types + ':' + ip_Survive_time + ':' + ip_verification_time)
            save(ip_num, ip_port, ip_adress, ip_hide, ip_types, ip_Survive_time, ip_verification_time)
            time.sleep(1)


#定义存储数据函数：
def save(name, rmb, adress, job_link, company, com_info, com_link, hr_info, job_time ):
    df = DataFrame({
        '职位名称': [name],
        '薪资': [rmb],
        '地址及要求': [adress],
        '职位链接': [job_link],
        '公司': [company],
        '公司情况': [com_info],
        '公司链接': [com_link],
        'HR信息': [hr_info],
        '发布时间': [job_time]
    })
    df.to_csv(
        '~/Downloads/' + Timestamp + '.csv', mode='a', header=False
    )

#定义打印函数；
num = int(30)
def print_source(msg):
    #url = 'https://www.zhipin.com/job_detail/?query=' + quote(query.encode('utf-8')) + '&scity=101210100&industry=&position='
    a = 5
    while True:
        url = 'https://www.zhipin.com/c101210100/?query=' + quote(
            query.encode('utf-8')) + '&page=' + str(a) + '&ka=page-' + str(a)
        print('正在获取' + url +  '的招聘信息')
        res = requests.get(url, headers=headers, timeout=5).content.decode('utf-8')
        bs4_res = bs4.BeautifulSoup(res, 'html.parser')
        #print(bs4_res)
        time.sleep(3)
        a = a + 1
        for i in range(1,num):
            print('正在获取第' + str(a) + '页的第' + str(i) + '条职位信息：########')
            time.sleep(3)
            try:
                name = bs4_res.select('.job-list li')[i]
                bs4_name = bs4.BeautifulSoup(str(name), 'html.parser')
                position_name = bs4_name.select('a .job-title')  #获取职位名称
                red_num = bs4_name.select('a .red')           #获取薪资
                com_Claim = bs4_name.select('.info-primary p')    #获取地区及职位基础要求
                job_details = bs4_name.select('.info-primary a')    #获取职详情页
                job_company = bs4_name.select('.info-company a')    #获取公司详情页
                com_information = bs4_name.select('.info-company p')  #获取公司人数等信息
                company_source1 = bs4_name.select('.company-text a')  # 获取公司名称
                hr_information = bs4_name.select('.info-publis h3')  #获取招聘者信息
                job_time = bs4_name.select('.info-publis p')  #获取职位发布时间
                for x in job_details:
                    job_link = 'https://www.zhipin.com' + str(x.get('href'))  #获取职详情页链接
                for c in job_company:
                    com_link = 'https://www.zhipin.com' + str(c.get('href'))  #获取公司详情页链接
                print(position_name[0].getText(), red_num[0].getText(), com_Claim[0].getText(), job_link, company_source1[0].getText(), com_information[0].getText(), com_link, hr_information[0].getText(), job_time[0].getText())
                save(position_name[0].getText(), red_num[0].getText(), com_Claim[0].getText(), job_link, company_source1[0].getText(), com_information[0].getText(), com_link, hr_information[0].getText(), job_time[0].getText())
            except:
                print('本页职位不足，跳过进入下一页')
                break

print_source(111)