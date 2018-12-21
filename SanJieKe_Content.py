import requests,json,time
from pandas import DataFrame

cookie = str(input('\n请输入你从浏览器复制的cookie信息：'))
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
grade = 0   #int(input('请输入需要爬取的作业类型，"0"为全部爬取，"1"为仅爬取优秀作业：'))   #0  测试编号
Timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))   #获取当前时间


data = {
    'question_id': question_id,
    'page': page,
    'cid': cid,
    'grade': grade
}
#data = str('question_id=' + question_id + '&page=' + page + '&cid=' + cid + '&grade=' + grade).replace("+", "%2B")
#requestsdata = data.encode('utf-8')


def save(name, job, id, homework_id,class_id, user_id, like_num, work_content, post_time, update_time, work_score, recommend, user_grade, teacher_name, teacher_comment, teacher_date, teacher_update_date, operation_title):
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
        '~/Downloads/' + operation_title +Timestamp + '.csv', mode='a', header=False
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
        if user_name != '道长一不会技术的推广不是好运营':
            print('📣学员名字：' + user_name + '......')
            try:
                res_teacher = requests.post(url_teacher, headers=headers_student, data={'hid': homework_id})
                res_teacher_json = json.loads(res_teacher.text)
                teacher_name = res_teacher_json['data'][0]['teacher_name']  # 获取助教名字
                teacher_comment = res_teacher_json['data'][0]['comment']  # 获取助教评语
                teacher_date = res_teacher_json['data'][0]['date']  # 获取第一次批改时间
                #teacher_update_date = res_teacher_json['data'][0]['update_time']   #获取最后批改时间
                teacher_update_date = time.strftime("%Y-%m-%d %H:%M:%S", (time.localtime(int(res_teacher_json['data'][0]['update_time']))))
                save(user_name, user_job, id, homework_id, class_id, user_id, like_count, user_content, create_time, update_time, comment_score, recommend, user_grade, teacher_name, teacher_comment, teacher_date, teacher_update_date, operation_title)
            except:
                print('💥无批改内容，跳过本次批改内容获取！！！')
                save(user_name, user_job, id, homework_id, class_id, user_id, like_count, user_content, create_time, update_time, comment_score, recommend, user_grade, '', '', '', '', operation_title)
            #teacher_update_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(res_teacher_json['data'][0]['update_time']))  #获取最后批改时间，并转换时间
            a += 1
            time.sleep(1)
        else:
            print('本页数据有误，跳过爬取......')
            continue
    #time.sleep(3)
    #time.sleep(random.randint(20, 60))
