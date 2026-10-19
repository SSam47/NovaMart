import os, json

transcript_path = r"C:\Users\OMEN\.gemini\antigravity-ide\brain\bf6de799-a5f8-4130-abc4-d2f2a26c98ba\.system_generated\logs\transcript.jsonl"
if os.path.exists(transcript_path):
    print("Found transcript!")
    with open(transcript_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"Total lines: {len(lines)}")
    for i, line in enumerate(lines):
        try:
            data = json.loads(line)
            if data.get("type") == "USER_INPUT":
                content = str(data.get("content", ""))
                print(f"L{i:4d} | USER: {content[:100]}")
        except Exception as e:
            pass
else:
    print("Transcript not found at", transcript_path)
