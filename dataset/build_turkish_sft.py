# -*- coding: utf-8 -*-
import json
import random
from datasets import load_dataset

print("1/3: Loading TFLai/Turkish-Alpaca...")
ds_alpaca = load_dataset("TFLai/Turkish-Alpaca", split="train")
print(f"Loaded {len(ds_alpaca)} Alpaca samples.")

print("2/3: Loading AlicanKiraz0/Turkish-CoT-Instruct-Dataset...")
ds_cot = load_dataset("AlicanKiraz0/Turkish-CoT-Instruct-Dataset", split="train")
print(f"Loaded {len(ds_cot)} CoT samples.")

all_samples = []

# Process Alpaca
for item in ds_alpaca:
    instruction = str(item.get("instruction", "")).strip()
    inp = str(item.get("input", "")).strip()
    output = str(item.get("output", "")).strip()
    
    if not instruction or not output:
        continue
    
    user_content = f"{instruction}\n\n{inp}".strip() if inp else instruction
    
    all_samples.append({
        "conversations": [
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": output}
        ]
    })

# Process CoT
for item in ds_cot:
    messages = item.get("messages", [])
    if not messages:
        continue
    
    # Filter valid conversations
    convs = []
    for m in messages:
        role = m.get("role", "")
        content = m.get("content", "")
        if role and content:
            convs.append({"role": role, "content": content})
            
    if convs:
        all_samples.append({"conversations": convs})

print(f"Total collected samples: {len(all_samples)}")
random.seed(42)
random.shuffle(all_samples)

output_path = "/Users/erentatar/AI/minimind/dataset/sft_turkce.jsonl"
with open(output_path, "w", encoding="utf-8") as f:
    for s in all_samples:
        f.write(json.dumps(s, ensure_ascii=False) + "\n")

print(f"3/3: Successfully saved {len(all_samples)} samples to {output_path}!")
