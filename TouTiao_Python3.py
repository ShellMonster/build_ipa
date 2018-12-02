# coding:utf-8
import requests,json,xlwt,time
from pandas import DataFrame;

group_id = int(input('请输入文章id：'))
Timestamp = int(time.time())
url = ('https://lf.snssdk.com/2/article/information/v23/?fp=zlT_LSGuFYKuFlcbL2U1F2KePMFI&version_code=6.9.8&tma_jssdk_version=1.5.3.2&app_name=news_article&vid=33614A87-B64E-4014-8784-E9DF9B9455C7&device_id=36635690031&channel=App%20Store&resolution=750*1334&aid=13&ab_feature=z1&ab_version=611288,486951,604156,616172,608566,571131,239098,612192,602389,170988,493249,609100,594604,374116,598324,588069,606504,620601,569578,613176,550042,435216,586992,545898,405354,623240,578707,614230,610260,614099,622089,377572,522766,416055,621360,619872,619657,558140,555254,378450,471406,603441,596391,550819,598626,608018,574603,603380,603399,603403,603406,616257,607361,609338,326532,586291,609316,623400,617391,620513,608689,622716,618683,622136,622969,621132,623376,601741,554836,549647,621743,472008,497614,572465,622432,612854,615292,606547,442255,616560,619833,546702,280447,281298,589820,616679,622043,325618,578588,619471,622469,476045,607297,612917,616220,616208,622795,431144,498375,583094,620881,467515,618148,619840,484770,621551,617234,616767,622433,580448,595556,615487,622143,620015,589102,586956,457480,573833,602735,562442,600764,621659&openudid=64b00576052f4b868da91059adc9f8bc4226423c&pos=5pe9vb/x8v788cLx/On47unC7fLuv72nveaXvb29vb/p9PD47un88O2/vae9rKiprqiqr6isrLOkrq+lqqqssZe9vb29v+3v8uv08/74v72nvb97KAR7LAJ6ARy/sZe9vb29v/706eS/vae9v3sAMHgqA3glH7+xl729vb2//vLy7/n08/zp+Mv88ej47r+9p73ml729vb29vb/x8vP69Ono+fi/vae9rK+ts62rpKmkpKulpa2vra2usZe9vb29vb2/8fzp9Ono+fi/vae9rq2zr6SprKqvrKylraqrr6SXvb29veCxl729vb2//Pn57/ju7r+9p72/eygEeywCegEcewAweCoDeCUfdTgieyQLeBEndQ8WewAMdTwKdBwOeBIRdCMEdTwKdTgieyc3dS0qv5e9veCX4A%3D%3D&update_version_code=69836&idfv=33614A87-B64E-4014-8784-E9DF9B9455C7&ac=WIFI&os_version=12.0.1&ssmix=a&device_platform=iphone&iid=52597445474&ab_client=a1,f2,f7,e1&device_type=iPhone%208&idfa=866F44F9-B63C-4304-8C5A-73B1EC94DAF9&article_page=0&' + 'group_id=' + str(group_id) + '&device_id=36635690031&aggr_type=1&item_id=' + str(group_id) + '&from_category=news_tech&as=a2e561e053e86cc0a13896&ts=' +str(Timestamp))
User_Agent = 'User-Agent: News 6.9.8 rv:6.9.8.36 (iPhone; iOS 12.0.1; zh_CN) Cronet'
Cookie = 'odin_tt=68767842315541735457306c794d4b6210bfa6ae28d08d3a46811eb95ce82326aee7bdff9f1a684918e7c9c9eda7af70; alert_coverage=34; install_id=52597445474; ttreq=1$ac1eb08cf4a35c3df0e98cab023f62e4e63daef7'
headers = {
    'Cookie':Cookie,
    'User-Agent':User_Agent,
}
res = requests.get(url,headers=headers)

resjson = json.loads(res.text)      #获取整个json数据
#print(resjson)


Num_one_json = resjson['data']   #定义第一层json变量
#print(Num_one_json)

Old_Article_comments = Num_one_json['comment_count']    #获取原文评论数据
#print(Old_Article_comments)

Old_Like_Num = Num_one_json['like_count']    #获取原文点赞数
#print(Old_Like_Num)

Old_Source = Num_one_json['source']    #获取原文作者名称
#print(Old_Source)

Old_Url = Num_one_json['url']     #获取原文跳转链接
#print(Old_Url)

Old_Title = Num_one_json['share_info']['title']     #获取原文标题
#print(Old_Title)

Old_Fans = Num_one_json['user_info']['fans_count']     #获取原文章博主订阅数
#print(Old_Fans)

Num_Two_json = Num_one_json['ordered_info']     #获取第二层json变量
#print(Num_Two_json)

Recommend_Content = Num_Two_json[2]     #获取推荐文章内容列表

Num_One_Source = Recommend_Content['data'][0]['source']      #获取推荐第一篇文章作者
Num_One_Title = Recommend_Content['data'][0]['title']     #获取推荐第一篇文章标题
Num_One_Publish_Time = Recommend_Content['data'][0]['publish_time']    #获取推荐第一篇文章发布时间
Num_One_Comment_Count = Recommend_Content['data'][0]['comment_count']  #获取推荐第一篇文章评论数
Num_One_Group_id = Recommend_Content['data'][0]['group_id']        #获取推荐第一篇文章ID


Num_Two_Source = Recommend_Content['data'][1]['source']     #获取推荐第二篇文章作者
Num_Two_Title = Recommend_Content['data'][1]['title']      #获取推荐第二篇文章标题
Num_Two_Publish_Time = Recommend_Content['data'][1]['publish_time']    #获取推荐第二篇文章发布时间
Num_Two_Comment_Count = Recommend_Content['data'][1]['comment_count']   #获取推荐第二篇文章评论数
Num_Two_Group_id = Recommend_Content['data'][1]['group_id']        #获取推荐第二篇文章


Num_Thr_Source = Recommend_Content['data'][2]['source']      #获取推荐第三篇文章作者
Num_Thr_Publish_Time = Recommend_Content['data'][2]['publish_time']    #获取推荐第三篇文章发布时间
Num_Thr_Comment_Count = Recommend_Content['data'][2]['comment_count']  #获取推荐第三篇文章评论数
Num_Thr_Title = Recommend_Content['data'][2]['title']      #获取推荐第三篇文章标题
Num_Thr_Group_id = Recommend_Content['data'][2]['group_id']        #获取推荐第三篇文章


Num_Fou_Source = Recommend_Content['data'][3]['source']      #获取推荐第四篇文章作者
Num_Fou_Publish_Time = Recommend_Content['data'][3]['publish_time']    #获取推荐第四篇文章发布时间
Num_Fou_Comment_Count = Recommend_Content['data'][3]['comment_count']   #获取推荐第四篇文章评论数
Num_Fou_Title = Recommend_Content['data'][3]['title']      #获取推荐第四篇文章标题
Num_Fou_Group_id = Recommend_Content['data'][3]['group_id']        #获取推荐第四篇文章

Num_Fiv_Source = Recommend_Content['data'][4]['source']      #获取推荐第五篇文章作者
Num_Fiv_Publish_Time = Recommend_Content['data'][4]['publish_time']    #获取推荐第五篇文章发布时间
Num_Fiv_Comment_Count = Recommend_Content['data'][4]['comment_count']  #获取推荐第五篇文章评论数
Num_Fiv_Title = Recommend_Content['data'][4]['title']      #获取推荐第五篇文章标题
Num_Fiv_Group_id = Recommend_Content['data'][4]['group_id']        #获取推荐第五篇文章


"""时间戳转换"""
timeArray1 = time.localtime(Num_One_Publish_Time)
Timestamp_Num_One_Publish_Time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray1)

timeArray2 = time.localtime(Num_Two_Publish_Time)
Timestamp_Num_Two_Publish_Time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray2)

timeArray3 = time.localtime(Num_Thr_Publish_Time)
Timestamp_Num_Thr_Publish_Time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray3)

timeArray4 = time.localtime(Num_Fou_Publish_Time)
Timestamp_Num_Fou_Publish_Time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray4)

timeArray5 = time.localtime(Num_Fiv_Publish_Time)
Timestamp_Num_Fiv_Publish_Time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray5)

timeArray6 = time.localtime(Timestamp)
Timestamp_Time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray6)

"""时间戳转换"""


df = DataFrame({
    '分类': ['原文文章', '推荐文章', '推荐文章', '推荐文章', '推荐文章', '推荐文章'],
    '标题': [Old_Title, Num_One_Title, Num_Two_Title, Num_Thr_Title, Num_Fou_Title, Num_Fiv_Title],
    '发布账号': [Old_Source, Num_One_Source, Num_Two_Source, Num_Thr_Source, Num_Fou_Source, Num_Fiv_Source],
    '粉丝' :[Old_Fans, '', '', '', '', ''],
    '发布时间': ['', Timestamp_Num_One_Publish_Time, Timestamp_Num_Two_Publish_Time, Timestamp_Num_Thr_Publish_Time, Timestamp_Num_Fou_Publish_Time, Timestamp_Num_Fiv_Publish_Time],
    '点赞数': [Old_Like_Num, '', '', '', '', ''],
    '评论数': [Old_Article_comments, Num_One_Comment_Count, Num_Two_Comment_Count, Num_Thr_Comment_Count, Num_Fou_Comment_Count, Num_Fiv_Comment_Count],
    '统计时间': [Timestamp_Time, Timestamp_Time, Timestamp_Time, Timestamp_Time, Timestamp_Time, Timestamp_Time],
    '跳转链接': [str(Old_Url), 'https://www.toutiao.com/a' + str(Num_One_Group_id), 'https://www.toutiao.com/a' + str(Num_Two_Group_id), 'https://www.toutiao.com/a' + str(Num_Thr_Group_id), 'https://www.toutiao.com/a' + str(Num_Fou_Group_id), 'https://www.toutiao.com/a' + str(Num_Fiv_Group_id)],
})

df.to_csv(
    "/Users/mac/Downloads/" + Timestamp_Time + ".csv"
)

print('请至/Users/mac/Downloads/查看名为当前时间的CSV文件')