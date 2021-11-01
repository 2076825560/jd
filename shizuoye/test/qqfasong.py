import yagmail
yam=yagmail.SMTP(user='2063527051@qq.com',
                 password='dnhyvscvokbqhhae',
                 host='smtp.qq.com'
                 )
yam.send(
         to=['2063527051@qq.com','813513353@qq.com'],
         subject='10.29作业',
         contents='10.29日志，报告',
         attachments=[r'C:\Users\86199\Desktop\py\shizuoye\test\baogao.html',r'C:\Users\86199\Desktop\py\shizuoye\logg.log'])