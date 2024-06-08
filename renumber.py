import json


qid = 0
output = []
with open("multi-image_eval-data.jsonl", "r") as f:
    for line in f:
        json_line = json.loads(line)
        json_line["question_id"] = qid
        # json_line["text"] += " In your response, describe each image before answering the question."
        output.append(json_line)
        qid += 1

with open("multi-image_eval-data_1.jsonl", "w") as f:
    for line in output:
        f.write(json.dumps(line) + "\n")