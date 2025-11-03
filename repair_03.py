import json

# Read the file
with open('03.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Convert answer format from string to correct array format
for q in questions:
    if 'answer' in q:
        answer_text = q['answer']
        # Find the index of the answer in options
        if answer_text in q['options']:
            answer_index = q['options'].index(answer_text)
            q['correct'] = [answer_index]
        else:
            # If answer not found, default to 0 and print warning
            print(f"Warning: Answer '{answer_text}' not found in options for question: {q['question'][:50]}...")
            q['correct'] = [0]
        # Remove old 'answer' field
        del q['answer']

# Add some multiple choice questions about routing protocols
new_questions = [
    {
        "question": "Which of the following are characteristics of Distance Vector routing protocols? (Select all that apply)",
        "options": [
            "Routers exchange information about their directly connected links",
            "Routers periodically exchange routing tables with neighbors",
            "Uses Bellman-Ford algorithm",
            "Requires complete network topology knowledge"
        ],
        "correct": [1, 2],
        "multipleCorrect": True,
        "explanation": "Distance Vector protocols exchange routing tables with neighbors and use the Bellman-Ford algorithm. They don't exchange link state info or require complete topology knowledge."
    },
    {
        "question": "Which statements are true about RIPv2? (Select all that apply)",
        "options": [
            "Supports Variable Length Subnet Masking (VLSM)",
            "Uses multicast address 224.0.0.9",
            "Maximum hop count is 15",
            "Introduced the Route Tag field"
        ],
        "correct": [0, 1, 3],
        "multipleCorrect": True,
        "explanation": "RIPv2 supports VLSM, uses multicast 224.0.0.9, and introduced Route Tag field. The maximum hop count representing infinity is 16, not 15."
    },
    {
        "question": "Which of the following are components of IGRP's composite metric? (Select all that apply)",
        "options": [
            "Bandwidth (B)",
            "Delay (D)",
            "Load (L)",
            "Jitter (J)"
        ],
        "correct": [0, 1, 2],
        "multipleCorrect": True,
        "explanation": "IGRP uses Bandwidth, Delay, Load, and Reliability (not listed) in its composite metric. Jitter is not part of the IGRP metric."
    },
    {
        "question": "Which are advantages of Link State routing over Distance Vector? (Select all that apply)",
        "options": [
            "Faster convergence",
            "No count-to-infinity problem",
            "Lower memory requirements",
            "Better scalability for large networks"
        ],
        "correct": [0, 1, 3],
        "multipleCorrect": True,
        "explanation": "Link State protocols converge faster, avoid count-to-infinity, and scale better. However, they typically require MORE memory to store complete topology information."
    },
    {
        "question": "Which statements about OSPF are correct? (Select all that apply)",
        "options": [
            "It is a Link State protocol",
            "It uses Dijkstra's algorithm",
            "It supports hierarchical routing with areas",
            "It has a maximum hop count of 16"
        ],
        "correct": [0, 1, 2],
        "multipleCorrect": True,
        "explanation": "OSPF is a Link State protocol using Dijkstra's algorithm with hierarchical areas. It does NOT have a hop count limit (that's RIP)."
    },
    {
        "question": "Which protocols run directly over IP without using TCP or UDP? (Select all that apply)",
        "options": [
            "OSPF",
            "RIP",
            "IGRP",
            "BGP"
        ],
        "correct": [0, 2],
        "multipleCorrect": True,
        "explanation": "OSPF uses IP protocol 89, IGRP uses IP protocol 9. RIP uses UDP port 520, and BGP uses TCP port 179."
    },
    {
        "question": "Which are characteristics of hierarchical routing? (Select all that apply)",
        "options": [
            "Reduces routing table size",
            "Improves scalability",
            "Divides network into areas or domains",
            "Requires all routers to know complete topology"
        ],
        "correct": [0, 1, 2],
        "multipleCorrect": True,
        "explanation": "Hierarchical routing reduces table size, improves scalability, and divides networks into areas. It specifically avoids requiring all routers to know the complete topology."
    },
    {
        "question": "Which statements about BGP are true? (Select all that apply)",
        "options": [
            "It is an Exterior Gateway Protocol (EGP)",
            "It is a path-vector protocol",
            "It uses TCP for reliable message delivery",
            "It is designed for intra-AS routing"
        ],
        "correct": [0, 1, 2],
        "multipleCorrect": True,
        "explanation": "BGP is an EGP path-vector protocol using TCP port 179. It's designed for inter-AS routing, not intra-AS."
    },
    {
        "question": "Which are valid OSPF area types? (Select all that apply)",
        "options": [
            "Backbone area (Area 0)",
            "Stub area",
            "Not-So-Stubby Area (NSSA)",
            "Transit area"
        ],
        "correct": [0, 1, 2],
        "multipleCorrect": True,
        "explanation": "OSPF defines backbone area (Area 0), stub areas, and NSSA. 'Transit area' is not a formal OSPF area type."
    },
    {
        "question": "Which information is contained in OSPF Link State Advertisements (LSAs)? (Select all that apply)",
        "options": [
            "Router ID",
            "Link state information",
            "Link cost/metric",
            "Complete routing table"
        ],
        "correct": [0, 1, 2],
        "multipleCorrect": True,
        "explanation": "LSAs contain Router ID, link state info, and link costs. They don't contain complete routing tables - those are computed locally."
    }
]

# Add new questions
questions.extend(new_questions)

# Write back with compact format for correct arrays
output = "[\n"
for i, q in enumerate(questions):
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
    if i < len(questions) - 1:
        output += ","
    output += "\n"
output += "]\n"

with open('03.json', 'w', encoding='utf-8') as f:
    f.write(output)

print(f"✓ Successfully converted {len(questions) - len(new_questions)} questions from 'answer' format to 'correct' format")
print(f"✓ Added {len(new_questions)} new multiple-choice questions")
print(f"✓ Total questions now: {len(questions)}")
print("\nMultiple-choice questions added cover:")
print("  • Distance Vector protocol characteristics")
print("  • RIPv2 features and capabilities")
print("  • IGRP composite metric components")
print("  • Link State vs Distance Vector advantages")
print("  • OSPF features and characteristics")
print("  • Protocol transport mechanisms")
print("  • Hierarchical routing concepts")
print("  • BGP characteristics")
print("  • OSPF area types")
print("  • OSPF LSA contents")
