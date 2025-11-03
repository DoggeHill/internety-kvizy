import json

# Load the JSON file
with open('02.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total questions: {len(data)}")

# Count questions with multiple correct answers
multiple_count = 0

# Add multipleCorrect flag where needed
for question in data:
    correct = question['correct']
    if len(correct) > 1:
        question['multipleCorrect'] = True
        multiple_count += 1

print(f"Questions with multiple correct answers: {multiple_count}")

# Save with compact correct arrays and multipleCorrect flag
output_lines = ['[']
for i, question in enumerate(data):
    output_lines.append('  {')
    output_lines.append(f'    "question": {json.dumps(question["question"], ensure_ascii=False)},')
    output_lines.append('    "options": [')
    for j, opt in enumerate(question['options']):
        comma = ',' if j < len(question['options']) - 1 else ''
        output_lines.append(f'      {json.dumps(opt, ensure_ascii=False)}{comma}')
    output_lines.append('    ],')
    # Format correct on one line
    correct_str = '[' + ', '.join(str(x) for x in question['correct']) + ']'
    output_lines.append(f'    "correct": {correct_str},')
    
    # Add multipleCorrect flag if present
    if 'multipleCorrect' in question:
        output_lines.append(f'    "multipleCorrect": true,')
    
    output_lines.append(f'    "explanation": {json.dumps(question["explanation"], ensure_ascii=False)}')
    comma = ',' if i < len(data) - 1 else ''
    output_lines.append(f'  }}{comma}')

output_lines.append(']')

# Write to file
with open('02.json', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print("\n✓ Successfully added 'multipleCorrect' flag to questions with multiple correct answers")
