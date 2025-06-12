import json
import pandas as pd

# 输入文件路径
freq_file = "label_counts.txt"
label_info_file = "MAGCS_label.json"
output_excel = "id_name_freq.xlsx"

# 第一步：读取频率文件
id_to_freq = {}
with open(freq_file, "r", encoding="utf-8") as f:
    for line in f:
        if not line.strip():
            continue
        parts = line.strip().split(":\t")
        if len(parts) == 2:
            id_, freq = parts
            id_to_freq[id_] = int(freq)

# 第二步：读取标签文件，匹配 ID 获取 name
id_to_name = {}
with open(label_info_file, "r", encoding="utf-8") as f:
    for line in f:
        if not line.strip():
            continue
        try:
            data = json.loads(line)
            label_id = data.get("label")
            name = data.get("name")
            if label_id in id_to_freq:
                if len(name) == 1:
                    id_to_name[label_id] = name[0]
                else:
                    id_to_name[label_id] = name
                    print(f"警告：ID {label_id} 的名称列表长度不为 1，实际长度为 {len(name)}")
        except json.JSONDecodeError:
            print(f"跳过无法解析的行：{line.strip()}")

# 第三步：构建 DataFrame 并导出 Excel
rows = []
for id_, freq in id_to_freq.items():
    name = id_to_name.get(id_, "[未知名称]")
    rows.append((id_, name, freq))

df = pd.DataFrame(rows, columns=["ID", "名称", "频率"])
df.to_excel(output_excel, index=False)
