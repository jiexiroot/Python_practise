height = float(input('请输入您的身高(m):'))
weight = float(input('请输入您的体重(kg):'))
BMI = weight / (height * height)
print('您的 BMI 值为%.2f' % BMI)
if BMI < 18.5:
    print('体重过轻')
elif 18.5 <= BMI <= 23.9:
    print('体重正常')
elif 24 <= BMI <= 27:
    print('体重过重')
elif 28 <= BMI <= 32:
    print('体重肥胖')
else:
    print('非常肥胖')
