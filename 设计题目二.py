print("=== 学习状态评估系统 ===")

# 输入被试学习情况
study_time = float(input("请输入每天平均学习时间(小时): "))
homework_rate = int(input("请输入作业完成率(0-100): "))
class_performance = input("请输入课堂表现(积极/一般/不积极): ")

print("\n=== 评估结果 ===")

# 评估学习状态
if study_time >= 4 and homework_rate >= 90 and class_performance == "积极":
    status = "优秀"
    print(f"学习状态: {status}")
    print("评价: 你的学习状态非常好！继续保持！")
    
elif study_time >= 3 and homework_rate >= 80 and (class_performance == "积极" or class_performance == "一般"):
    status = "良好"
    print(f"学习状态: {status}")
    print("评价: 学习状态不错，还有提升空间！")
    
elif study_time >= 2 and homework_rate >= 70:
    status = "中等"
    print(f"学习状态: {status}")
    print("评价: 基本达标，需要更加努力！")
    
else:
    status = "需改进"
    print(f"学习状态: {status}")
    print("评价: 需要认真反思和改进学习方法！")

# 具体建议
print("\n=== 改进建议 ===")
if study_time < 2:
    print("建议增加学习时间，每天至少学习2小时")
if homework_rate < 70:
    print("建议提高作业完成质量，争取完成70%以上")
if class_performance == "不积极":
    print("建议在课堂上更积极参与讨论和互动")

# 鼓励语句
if status == "优秀":
    print("继续保持优秀的学习习惯！")
elif status == "良好":
    print("再加把劲，你离优秀很近了！")
elif status == "中等":
    print("相信自己，你可以做得更好！")
else:
    print("不要气馁，从今天开始努力！")