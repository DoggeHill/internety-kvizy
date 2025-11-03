import json

# Load the JSON file
with open('03.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total questions: {len(data)}")

# Count and add multipleCorrect flag where needed
multiple_count = 0
for question in data:
    if len(question['correct']) > 1:
        if 'multipleCorrect' not in question or not question['multipleCorrect']:
            question['multipleCorrect'] = True
            multiple_count += 1

print(f"Questions with multiple correct answers: {sum(1 for q in data if len(q['correct']) > 1)}")

# Write back with compact format for correct arrays
output = "[\n"
for i, q in enumerate(data):
    output += "  {\n"
    output += f'    "question": {json.dumps(q["question"])},\n'
    output += '    "options": [\n'
    for j, opt in enumerate(q['options']):
        comma = "," if j < len(q['options']) - 1 else ""
        output += f'      {json.dumps(opt)}{comma}\n'
    output += '    ],\n'
    output += f'    "correct": {json.dumps(q["correct"])}'
    
    if q.get('multipleCorrect'):
        output += ',\n'
        output += f'    "multipleCorrect": true'
    
    if q.get('explanation'):
        output += ',\n'
        output += f'    "explanation": {json.dumps(q["explanation"])}'
    
    output += "\n  }"
    if i < len(data) - 1:
        output += ","
    output += "\n"
output += "]\n"

with open('03.json', 'w', encoding='utf-8') as f:
    f.write(output)

print(f"\n✓ Successfully verified/added 'multipleCorrect' flag to questions in 03.json")
