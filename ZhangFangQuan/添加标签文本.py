import json

# 输入文件路径
freq_file = "label_counts.txt"
label_info_file = "MAGCS_label.json"
output_file = "id_name_freq.txt"

# 第一步：读取频率文件
id_to_freq = {}
with open(freq_file, "r", encoding="utf-8") as f:
    for line in f:
        if not line.strip():
            continue
        parts = line.strip().split(":\t")
        if len(parts) == 2:
            id_, freq = parts
            id_to_freq[id_] = freq

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
                id_to_name[label_id] = name[0]
        except json.JSONDecodeError:
            print(f"跳过无法解析的行：{line.strip()}")

# 第三步：输出到文件
with open(output_file, "w", encoding="utf-8") as f_out:
    for id_, freq in id_to_freq.items():
        name = id_to_name.get(id_, "[未知名称]")
        f_out.write(f"{id_}:\t{name}:\t{freq}\n")
