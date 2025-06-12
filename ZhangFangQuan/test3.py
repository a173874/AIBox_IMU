import json

input_file = "MAGCS_candidates.json"
output_file = "filtered.json"

# 目标 label 集合
target_labels = {"11413529", "512554520", "177264268","48103436"}

with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
    for line in f_in:
        if not line.strip():
            continue
        try:
            data = json.loads(line)
            labels = data.get("matched_label", [])
            if any(label in target_labels for label in labels):
                json.dump(data, f_out, ensure_ascii=False)
                f_out.write("\n")
        except json.JSONDecodeError:
            print(f"跳过无法解析的行：{line.strip()}")
