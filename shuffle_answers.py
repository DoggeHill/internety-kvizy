import json
import random

# Set seed for reproducibility
random.seed(42)

# Load the JSON file
with open('02.json', 'r', encoding='utf-8') as f:
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

# Custom JSON encoder to keep 'correct' array on one line
class CompactJSONEncoder(json.JSONEncoder):
    def encode(self, obj):
        if isinstance(obj, list):
            # For lists with only numbers (like correct answers), format on one line
            if all(isinstance(x, int) for x in obj):
                return '[' + ', '.join(str(x) for x in obj) + ']'
        return super().encode(obj)
    
    def iterencode(self, obj, _one_shot=False):
        # Override to handle nested structures
        if isinstance(obj, dict):
            # Manually format the dictionary
            items = []
            for key, value in obj.items():
                key_str = json.dumps(key)
                if key == 'correct' and isinstance(value, list):
                    # Format correct array on one line
                    value_str = '[' + ', '.join(str(x) for x in value) + ']'
                elif isinstance(value, list) and key == 'options':
                    # Keep options as regular multi-line format
                    value_str = json.dumps(value, indent=2, ensure_ascii=False).replace('\n', '\n    ')
                elif isinstance(value, str):
                    value_str = json.dumps(value, ensure_ascii=False)
                else:
                    value_str = json.dumps(value, ensure_ascii=False)
                items.append(f'    {key_str}: {value_str}')
            return iter(['{\n' + ',\n'.join(items) + '\n  }'])
        return super().iterencode(obj, _one_shot)

# Save with compact correct arrays
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
    output_lines.append(f'    "explanation": {json.dumps(question["explanation"], ensure_ascii=False)}')
    comma = ',' if i < len(data) - 1 else ''
    output_lines.append(f'  }}{comma}')

output_lines.append(']')

# Write to file
with open('02.json', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print("\n✓ Successfully shuffled all questions in 02.json")
print("✓ Formatted 'correct' arrays to be on one line")
