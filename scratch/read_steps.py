import json

transcript_path = r"C:\Users\OMEN\.gemini\antigravity-ide\brain\bf6de799-a5f8-4130-abc4-d2f2a26c98ba\.system_generated\logs\transcript.jsonl"
with open(transcript_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx in [545, 593, 616, 636]:
    for i in range(idx - 1, min(len(lines), idx + 20)):
        try:
            d = json.loads(lines[i])
            calls = d.get("tool_calls", [])
            for c in calls:
                print(f"L{i:3d} call: {c}")
        except:
            pass
