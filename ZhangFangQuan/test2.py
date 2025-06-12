import json

input_file = "MAGCS_candidates.json"

min_len = float('inf')
max_len = float('-inf')

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        if not line.strip():
            continue
        try:
            data = json.loads(line)
            labels = data.get("matched_label", [])
            if isinstance(labels, list):
                length = len(labels)
                min_len = min(min_len, length)
                max_len = max(max_len, length)
        except json.JSONDecodeError:
            print(f"跳过无法解析的行：{line.strip()}")

# 如果文件没有有效数据，避免inf输出
if min_len == float('inf'):
    print("没有有效的 matched_label 数据。")
else:
    print(f"matched_label 最小长度: {min_len}")
    print(f"matched_label 最大长度: {max_len}")
