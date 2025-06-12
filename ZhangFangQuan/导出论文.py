import json

# 文件路径
filtered_file = "filtered.json"      # 上一步中筛选出来的条目
paper_file = "MAGCS_paper.json"            # 包含全部 paper 条目的文件
output_file = "matched_papers.json"  # 输出文件

# 第一步：收集需要的 paper ID
target_ids = set()

with open(filtered_file, "r", encoding="utf-8") as f:
    for line in f:
        if not line.strip():
            continue
        try:
            data = json.loads(line)
            paper_id = data.get("paper")
            if paper_id is not None:
                target_ids.add(paper_id)
        except json.JSONDecodeError:
            print(f"跳过无法解析的行：{line.strip()}")

# 第二步：在 paper.json 中查找匹配的条目
with open(paper_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
    for line in f_in:
        if not line.strip():
            continue
        try:
            data = json.loads(line)
            paper_id = data.get("paper")
            if paper_id in target_ids:
                json.dump(data, f_out, ensure_ascii=False)
                f_out.write("\n")
        except json.JSONDecodeError:
            print(f"跳过无法解析的行：{line.strip()}")
