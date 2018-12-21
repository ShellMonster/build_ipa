import requests,json,time
from pandas import DataFrame

cookie = str(input('请输入你从浏览器复制的cookie信息：'))  #_9755xjdesxxd_=32; PHPSESSID=tnbpffeasit7utri41pok9fhb5; tutor_id=10864916; tutor_name=%E9%81%93%E9%95%BF; tutor_phone=13148393049; tutor_login_time=1544110183; tutor_sign=f43678a99f609127d294ddfb47ed4e37; tutor_uid=4370584; gr_user_id=ad3a23ad-373f-4ad7-af47-af213750f72b; MEIQIA_EXTRA_TRACK_ID=1DzYWyh0jXUblDuKAJThI80gTTt; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216784bf6092146-0eda676b78d82d-35667607-2304000-16784bf6094651%22%2C%22%24device_id%22%3A%2216784bf6092146-0eda676b78d82d-35667607-2304000-16784bf6094651%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lvt_870cbf2e1f9e809dd8bb9005f25561a8=1544759316,1545323856,1545325310,1545325323; MEIQIA_VISIT_ID=1EcwgU4yErnIK29djW1oGunanLX; tipCookie=true; Hm_lpvt_870cbf2e1f9e809dd8bb9005f25561a8=1545327692; gdxidpyhxdE=741MoSRqefCa5kdZWYZOADEWz0%5CUkhG6LN7Rahw29fqH1yg026Uu5whUwlUzehonQ0nP2Th29sYuYPrOXHikgVcuo7WurU03HpSpIPnXaxKEte3fv%2BtCXqnH0m4zCGKL3ylkNEYNEfTXWw9ClR%2Bgygl%2FzEcEP%2B5x6rLiW0aT8jO%2BJ6p4%3A1545328953204; gr_session_id_9d9c485ce095faca=01058cad-7804-4fb1-80c8-a7b7a5b2a70f; gr_session_id_9d9c485ce095faca_01058cad-7804-4fb1-80c8-a7b7a5b2a70f=true; utm_data=%7B%22c_utm_content%22%3A%22%22%2C%22c_utm_campaign%22%3A%22%22%2C%22c_utm_medium%22%3A%22%22%2C%22c_utm_term%22%3A%22%22%2C%22c_utm_source%22%3A%22%22%2C%22d1_utm_content%22%3A%22%22%2C%22d1_utm_campaign%22%3A%22%22%2C%22d1_utm_medium%22%3A%22%22%2C%22d1_utm_term%22%3A%22%22%2C%22d1_utm_source%22%3A%22%22%2C%22d15_utm_content%22%3A%22%22%2C%22d15_utm_campaign%22%3A%22%22%2C%22d15_utm_medium%22%3A%22%22%2C%22d15_utm_term%22%3A%22%22%2C%22d15_utm_source%22%3A%22%22%2C%22d30_utm_content%22%3A%22%22%2C%22d30_utm_campaign%22%3A%22%22%2C%22d30_utm_medium%22%3A%22%22%2C%22d30_utm_term%22%3A%22%22%2C%22d30_utm_source%22%3A%22%22%2C%22referrer%22%3A%22https%3A//class.sanjieke.cn/course/view/cid/12129770.html%22%7D
headers_teacher = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-length': '48',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': cookie,
    'origin': 'https://class.sanjieke.cn',
    'referer': 'https://class.sanjieke.cn/Course/answers/12129770/11735936',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

headers_student = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-length': '12',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': cookie,
    'origin': 'https://class.sanjieke.cn',
    'referer': 'https://class.sanjieke.cn/Course/answers/12129770/11735936',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

question_id = int(input('请输入作业编号：'))     #11735936 测试编号
page = 1
cid = int(input('请输入班级编号：'))          #12129770   测试编号
grade = int(input('请输入需要爬取的作业类型，"0"为全部爬取，"1"为仅爬取优秀作业：'))   #0  测试编号
Timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))   #获取当前时间


data = {
    'question_id': question_id,
    'page': page,
    'cid': cid,
    'grade': grade
}
#data = str('question_id=' + question_id + '&page=' + page + '&cid=' + cid + '&grade=' + grade).replace("+", "%2B")
#requestsdata = data.encode('utf-8')


def save(name, job, id, homework_id,class_id, user_id, like_num, work_content, post_time, update_time, work_score, recommend, user_grade, teacher_name, teacher_comment, teacher_date, teacher_update_date):
    df = DataFrame({
        '学员名字': [name],
        '学员岗位': [job],
        'id': [id],
        '作业id': [homework_id],
        '班期id': [class_id],
        '用户id': [user_id],
        '点赞数': [like_num],
        '作业内容': [work_content],
        '提交时间': [post_time],
        '最后更新时间': [update_time],
        '作业分数': [work_score],
        '是否推荐': [recommend],
        '是否优秀': [user_grade],
        '助教名称': [teacher_name],
        '助教评语': [teacher_comment],
        '批改时间': [teacher_date],
        '最后批改时间': [teacher_update_date]
    })
    df.to_csv(
        '~/Downloads/' + Timestamp + '.csv', mode='a', header=False
    )


#获取页数
url_print = 'https://class.sanjieke.cn/Topic/getHomeworkList'
res_print = requests.post(url_print, headers=headers_teacher, data=data)
res_json_print = json.loads(res_print.text)  # 获取内容json层
countpage = res_json_print['data']['countpage']  # 获取总计页数


#定义获取助教评语；
url_teacher = 'https://class.sanjieke.cn/Topic/teacherCorrect'

#获取作业内容；
page = 1
while int(page) <= int(countpage):
    url = 'https://class.sanjieke.cn/Topic/getHomeworkList'
    res = requests.post(url, headers=headers_teacher, data={'question_id': question_id,'page': page, 'cid': cid,'grade': grade})
    res_json = json.loads(res.text)    #获取内容json层
    operation_title = res_json['data']['title']   #获取作业标题
    operation_content = res_json['data']['content']   #获取作业要求详细描述
    page = page + 1
    a = 1
    #for i in range(0, 10):
    for i in res_json['data']['homeWorkList']:
        print('\n------------正在获取第' + str((int(page)-2) * 10 + int(a)) + '条数据；当前总计' + str(countpage) + '页约' + str(countpage * 10) + '条数据！------------')
        user_name = i['name']  #获取学员名字
        user_job = i['job']   #获取学员岗位
        id = i['id']
        homework_id = i['homework_id']   #获取作业id
        class_id = i['class_id']  #获取班期id
        course_id = i['course_id']
        question_id = i['question_id']
        user_id = i['user_id']  #获取用户id
        like_count = i['like_count']   #获取作业点赞数
        user_content = i['content']  #获取用户作业内容
        create_time = i['create_time']   #获取用户作业提交时间
        update_time = i['update_time']   #获取用户作业最后更新时间
        comment_score = i['comment_score']  #获取作业分数
        recommend = i['recommend']   #是否强烈推荐
        user_grade = i['grade']   #是否优秀
        print('📣学员名字：' + user_name + '......')
        try:
            res_teacher = requests.post(url_teacher, headers=headers_student, data={'hid': homework_id})
            res_teacher_json = json.loads(res_teacher.text)
            teacher_name = res_teacher_json['data'][0]['teacher_name']  # 获取助教名字
            teacher_comment = res_teacher_json['data'][0]['comment']  # 获取助教评语
            teacher_date = res_teacher_json['data'][0]['date']  # 获取第一次批改时间
            #teacher_update_date = res_teacher_json['data'][0]['update_time']   #获取最后批改时间
            teacher_update_date = time.strftime("%Y-%m-%d %H:%M:%S", (time.localtime(int(res_teacher_json['data'][0]['update_time']))))
            save(user_name, user_job, id, homework_id, class_id, user_id, like_count, user_content, create_time, update_time, comment_score, recommend, user_grade, teacher_name, teacher_comment, teacher_date, teacher_update_date)
        except:
            print('💥无批改内容，跳过本次批改内容获取！！！')
            save(user_name, user_job, id, homework_id, class_id, user_id, like_count, user_content, create_time, update_time, comment_score, recommend, user_grade, '', '', '', '')
        #teacher_update_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(res_teacher_json['data'][0]['update_time']))  #获取最后批改时间，并转换时间
        a += 1
        time.sleep(1)
    time.sleep(3)
    #time.sleep(random.randint(20, 60))
