print("=== 心理压力测评数据分析 ===")

# 用列表储存压力得分
pressure_scores = []

# 输入被试的压力得分
for i in range(8):
    while True:
        score = int(input(f"请输入第{i+1}名被试的压力得分(0-50): "))
        if 0 <= score <= 50:
            pressure_scores.append(score)
            break
        else:
            print("得分应该在0-50之间，请重新输入！")

# 计算平均分
total = 0
for score in pressure_scores:
    total += score
average = total / len(pressure_scores)

# 统计结果
low_count = 0
medium_count = 0
high_count = 0

for score in pressure_scores:
    if score <= 15:
        low_count += 1
    elif score <= 30:
        medium_count += 1
    else:
        high_count += 1

# 找出最高分和最低分
max_score = pressure_scores[0]
min_score = pressure_scores[0]
for score in pressure_scores:
    if score > max_score:
        max_score = score
    if score < min_score:
        min_score = score

# 输出结果
print("\n=== 数据分析结果 ===")
print(f"平均压力水平: {average:.1f}")
print(f"压力程度分布:")
print(f"  轻度压力(0-15分): {low_count}人")
print(f"  中度压力(16-30分): {medium_count}人")
print(f"  重度压力(31-50分): {high_count}人")
print(f"最高压力得分: {max_score}, 最低压力得分: {min_score}")

# 给出建议
if average <= 15:
    print("整体压力水平较低，保持良好状态！")
elif average <= 30:
    print("整体压力水平适中，注意调节！")
else:
    print("整体压力水平较高，建议适当放松！")