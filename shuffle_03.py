import json
import random

# Set seed for reproducibility
random.seed(42)

# Load the JSON file
with open('03.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total questions: {len(data)}")

# Shuffle each question's options and update correct indices
for i, question in enumerate(data):
    options = question['options']
    correct_indices = question['correct']
    
    # Create pairs of (option, is_correct)
    option_pairs = [(opt, idx in correct_indices) for idx, opt in enumerate(options)]
    
    # Shuffle the pairs
    random.shuffle(option_pairs)
    
    # Reconstruct options and correct indices
    new_options = [pair[0] for pair in option_pairs]
    new_correct = [idx for idx, pair in enumerate(option_pairs) if pair[1]]
    
    question['options'] = new_options
    question['correct'] = new_correct

# Calculate distribution of correct answers
correct_positions = []
for q in data:
    correct_positions.extend(q['correct'])

from collections import Counter
distribution = Counter(correct_positions)
print("\nDistribution of correct answer positions:")
for pos in sorted(distribution.keys()):
    print(f"  Position {pos}: {distribution[pos]} times ({distribution[pos]/len(correct_positions)*100:.1f}%)")

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

print(f"\n✓ Successfully shuffled all questions in 03.json")
