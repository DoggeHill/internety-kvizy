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

# Save the shuffled data
with open('02.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\n✓ Successfully shuffled all questions in 02.json")
