import json
from collections import Counter

input_file = "MAGCS_candidates.json"      # 你的输入文件名
output_file = "label_counts.txt"  # 输出频率统计结果

counter = Counter()

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        if not line.strip():
            continue  # 跳过空行
        try:
            data = json.loads(line)
            labels = data.get("matched_label", [])
            counter.update(labels)
        except json.JSONDecodeError as e:
            print(f"解析失败，跳过此行：{line.strip()}")

# 将结果写入输出文件
with open(output_file, "w", encoding="utf-8") as f_out:
    for label, count in counter.most_common():
        f_out.write(f"{label}:\t{count}\n")
