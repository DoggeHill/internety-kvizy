import json

# Load existing questions
with open('02.json', 'r', encoding='utf-8') as f:
    existing_questions = json.load(f)

# New questions focusing on DAD, NUD, Autoconfiguration, and Security
new_questions = [
  {
    "question": "During Duplicate Address Detection (DAD), what does a node do before assigning an address?",
    "options": [
      "Sends a Neighbor Solicitation with the tentative address as the target",
      "Sends a Router Advertisement to all nodes",
      "Broadcasts an ARP request",
      "Queries the DHCP server"
    ],
    "correct": [0],
    "explanation": "The node sends a Neighbor Solicitation message with the unspecified address (::) as source and the tentative address as the target to check if anyone else is using it."
  },
  {
    "question": "What is the source address used in DAD Neighbor Solicitation messages?",
    "options": [
      "The tentative address being tested",
      "The unspecified address (::)",
      "The link-local address",
      "The global unicast address"
    ],
    "correct": [1],
    "explanation": "During DAD, the source address is the unspecified address (::) because the node hasn't confirmed ownership of any address yet."
  },
  {
    "question": "If a node receives a Neighbor Advertisement in response to its DAD message, what should it do?",
    "options": [
      "Ignore the message and use the address anyway",
      "Not use the tentative address as it's a duplicate",
      "Send another DAD message",
      "Request a new address from DHCPv6"
    ],
    "correct": [1],
    "explanation": "If a node receives a response during DAD, it means another node is already using that address. The node must not use the duplicate address."
  },
  {
    "question": "How many DAD messages must a node send before considering an address safe to use?",
    "options": [
      "At least 1 (DupAddrDetectTransmits default)",
      "Exactly 3",
      "At least 5",
      "Continuously until stopped"
    ],
    "correct": [0],
    "explanation": "The number is configurable via DupAddrDetectTransmits, with a default of 1. The node must wait RetransTimer milliseconds for responses."
  },
  {
    "question": "What is the purpose of the tentative address state in DAD?",
    "options": [
      "To indicate an address is being tested and cannot yet be used for communication",
      "To mark addresses that will expire soon",
      "To identify temporary privacy addresses",
      "To flag addresses assigned by DHCPv6"
    ],
    "correct": [0],
    "explanation": "During the tentative state, the address cannot be used for regular communication except for DAD, NUD, and Router Solicitation messages."
  },
  {
    "question": "In Neighbor Unreachability Detection, what triggers the transition from REACHABLE to STALE?",
    "options": [
      "The ReachableTime timer expires",
      "A packet is sent to the neighbor",
      "The neighbor sends an error message",
      "The router restarts"
    ],
    "correct": [0],
    "explanation": "When ReachableTime expires without any reachability confirmation, the neighbor entry transitions from REACHABLE to STALE state."
  },
  {
    "question": "What are the five states in the NUD state machine?",
    "options": [
      "INCOMPLETE, REACHABLE, STALE, DELAY, PROBE",
      "INIT, READY, ACTIVE, SUSPEND, TERMINATE",
      "NEW, VERIFIED, EXPIRED, INVALID, DELETED",
      "DISCOVER, OFFER, REQUEST, ACKNOWLEDGE, BOUND"
    ],
    "correct": [0],
    "explanation": "NUD uses five states to track neighbor reachability: INCOMPLETE (resolving), REACHABLE (confirmed reachable), STALE (unknown), DELAY (waiting), and PROBE (actively probing)."
  },
  {
    "question": "How does a node confirm forward reachability in NUD?",
    "options": [
      "By receiving upper-layer protocol confirmation (e.g., TCP ACK)",
      "By sending ICMP Echo Requests",
      "By monitoring ARP tables",
      "By checking DNS records"
    ],
    "correct": [0],
    "explanation": "Forward reachability is confirmed through upper-layer protocols (like TCP acknowledgments) indicating successful two-way communication."
  },
  {
    "question": "What happens when a node in STALE state needs to send packets to a neighbor?",
    "options": [
      "It transitions to DELAY state and sets a timer",
      "It immediately transitions to PROBE state",
      "It stays in STALE state indefinitely",
      "It deletes the neighbor cache entry"
    ],
    "correct": [0],
    "explanation": "When sending to a STALE neighbor, the entry moves to DELAY. If no reachability confirmation arrives within DELAY_FIRST_PROBE_TIME, it transitions to PROBE."
  },
  {
    "question": "In the PROBE state, what does a node do to verify neighbor reachability?",
    "options": [
      "Sends unicast Neighbor Solicitation messages",
      "Sends multicast Router Solicitation messages",
      "Broadcasts ARP requests",
      "Sends ICMP Echo Requests"
    ],
    "correct": [0],
    "explanation": "In PROBE state, the node sends unicast Neighbor Solicitation messages directly to the cached link-layer address to verify reachability."
  },
  {
    "question": "What information does a Router Advertisement provide for SLAAC?",
    "options": [
      "Network prefix and prefix length",
      "Prefix lifetime (valid and preferred)",
      "On-link and autonomous flags",
      "Complete IPv6 addresses"
    ],
    "correct": [0, 1, 2],
    "multipleCorrect": True,
    "explanation": "Router Advertisements include prefix information with length, lifetimes, and flags. Nodes use this to generate their own complete addresses via SLAAC."
  },
  {
    "question": "What is the difference between valid lifetime and preferred lifetime in SLAAC?",
    "options": [
      "Valid lifetime is how long an address can be used; preferred lifetime is how long it should be used for new connections",
      "Valid is for unicast, preferred is for multicast",
      "Valid is assigned by routers, preferred by hosts",
      "They are the same value"
    ],
    "correct": [0],
    "explanation": "Addresses remain valid for the valid lifetime but should only be used for new connections during the preferred lifetime. Deprecated addresses (preferred lifetime expired) can still receive traffic."
  },
  {
    "question": "How does a host generate its interface identifier using EUI-64 format?",
    "options": [
      "Inserts FF:FE in the middle of the MAC address and flips the universal/local bit",
      "Uses the MAC address directly without modification",
      "Generates a random 64-bit number",
      "Hashes the MAC address with SHA-256"
    ],
    "correct": [0],
    "explanation": "EUI-64 takes a 48-bit MAC address, inserts FF:FE in the middle to create 64 bits, and inverts the 7th bit (universal/local bit) to create the interface ID."
  },
  {
    "question": "What is the A flag in the Prefix Information option of Router Advertisements?",
    "options": [
      "Autonomous address-configuration flag indicating SLAAC is allowed",
      "Authentication required flag",
      "Anycast address flag",
      "Administrative preference flag"
    ],
    "correct": [0],
    "explanation": "The A (autonomous) flag indicates whether the prefix can be used for stateless address autoconfiguration (SLAAC)."
  },
  {
    "question": "What is the L flag in the Prefix Information option?",
    "options": [
      "On-link flag indicating addresses with this prefix are on the same link",
      "Link-local flag",
      "Loopback flag",
      "Lifetime extension flag"
    ],
    "correct": [0],
    "explanation": "The L (on-link) flag indicates that addresses with this prefix are assigned to the link and can be reached directly without routing."
  },
  {
    "question": "What security vulnerability exists with standard SLAAC?",
    "options": [
      "Rogue routers can advertise malicious prefixes",
      "Interface identifiers based on MAC addresses enable tracking",
      "No authentication of Router Advertisements",
      "Addresses are transmitted in cleartext"
    ],
    "correct": [0, 1, 2],
    "multipleCorrect": True,
    "explanation": "SLAAC vulnerabilities include rogue RA attacks, privacy issues with MAC-based addresses, and lack of RA authentication without SEND."
  },
  {
    "question": "How do Privacy Extensions (RFC 4941) improve SLAAC security?",
    "options": [
      "Generate random, temporary interface identifiers instead of MAC-based ones",
      "Encrypt the IPv6 address",
      "Use shorter addresses",
      "Require password authentication"
    ],
    "correct": [0],
    "explanation": "Privacy Extensions generate cryptographically random interface IDs that change periodically, preventing tracking based on stable MAC-derived identifiers."
  },
  {
    "question": "What is the difference between temporary and stable addresses in Privacy Extensions?",
    "options": [
      "Temporary addresses change periodically for privacy; stable addresses remain constant",
      "Temporary addresses are for IPv4, stable for IPv6",
      "Temporary addresses are shorter",
      "Stable addresses cannot send traffic"
    ],
    "correct": [0],
    "explanation": "Privacy Extensions create both stable addresses (for servers/incoming connections) and temporary addresses (for outgoing connections that change regularly)."
  },
  {
    "question": "How does SEND (Secure Neighbor Discovery) protect against NDP attacks?",
    "options": [
      "Uses cryptographic signatures based on CGA",
      "Validates NDP messages with digital certificates",
      "Encrypts all NDP traffic",
      "Requires DHCP authentication"
    ],
    "correct": [0, 1],
    "multipleCorrect": True,
    "explanation": "SEND uses Cryptographically Generated Addresses (CGA) and RSA signatures to authenticate NDP messages, preventing spoofing and man-in-the-middle attacks."
  },
  {
    "question": "What is the CGA modifier in Cryptographically Generated Addresses?",
    "options": [
      "A value used to make the first 16 bits of the hash match a security parameter",
      "A random encryption key",
      "The router's MAC address",
      "A timestamp for address expiration"
    ],
    "correct": [0],
    "explanation": "The CGA modifier is brute-forced to produce a hash where the leftmost Sec*16 bits are zero, making address forgery computationally expensive."
  },
  {
    "question": "What are the components used to generate a CGA?",
    "options": [
      "Public key",
      "IPv6 subnet prefix",
      "CGA modifier",
      "MAC address"
    ],
    "correct": [0, 1, 2],
    "multipleCorrect": True,
    "explanation": "CGAs are generated using the subnet prefix, modifier value, and the hash of the public key and other parameters, binding the address to the public key."
  },
  {
    "question": "What attack does SEND's timestamp option help prevent?",
    "options": [
      "Replay attacks",
      "SQL injection",
      "Buffer overflow",
      "Cross-site scripting"
    ],
    "correct": [0],
    "explanation": "SEND includes timestamp options to detect and reject replayed NDP messages, ensuring freshness and preventing replay attacks."
  },
  {
    "question": "What is the purpose of the Nonce option in SEND?",
    "options": [
      "To match solicitation messages with their responses",
      "To encrypt NDP messages",
      "To compress packet headers",
      "To calculate checksums"
    ],
    "correct": [0],
    "explanation": "The Nonce option ensures that advertisement messages correspond to specific solicitation messages, preventing off-path attacks."
  },
  {
    "question": "How does SeND prevent address resolution attacks?",
    "options": [
      "By requiring proof of address ownership through CGA verification",
      "By encrypting all traffic",
      "By using only DHCPv6",
      "By disabling autoconfiguration"
    ],
    "correct": [0],
    "explanation": "With SEND, a node must prove ownership of an address by providing the CGA parameters and signing messages with the corresponding private key."
  },
  {
    "question": "What is the RSA Signature option used for in SEND?",
    "options": [
      "To provide digital signature for NDP message authentication",
      "To encrypt the payload",
      "To compress the packet",
      "To indicate routing preferences"
    ],
    "correct": [0],
    "explanation": "The RSA Signature option contains a digital signature covering the NDP message, allowing recipients to verify the sender's identity and message integrity."
  },
  {
    "question": "What happens if a node performing DAD receives a Neighbor Solicitation for the same tentative address?",
    "options": [
      "Both nodes have detected a duplicate and must not use the address",
      "The first node wins and keeps the address",
      "Both nodes can use the address simultaneously",
      "The router assigns a new address to both"
    ],
    "correct": [0],
    "explanation": "If both nodes are performing DAD for the same address simultaneously, both detect the conflict and neither should use the address."
  },
  {
    "question": "What is Optimistic DAD (RFC 4429)?",
    "options": [
      "Allows using an address before DAD completes, with restrictions",
      "Skips DAD entirely for faster configuration",
      "Performs DAD only for global addresses",
      "Uses hardware-based duplicate detection"
    ],
    "correct": [0],
    "explanation": "Optimistic DAD allows limited use of an address (sending but not receiving) before DAD completes, reducing configuration delays while maintaining safety."
  },
  {
    "question": "Which types of addresses require DAD to be performed?",
    "options": [
      "Unicast addresses",
      "Multicast addresses",
      "Anycast addresses",
      "The unspecified address (::)"
    ],
    "correct": [0, 2],
    "multipleCorrect": True,
    "explanation": "DAD must be performed on all unicast and anycast addresses before use. Multicast addresses don't need DAD, and the unspecified address is never assigned."
  },
  {
    "question": "What is the purpose of the Router Lifetime field in Router Advertisements?",
    "options": [
      "Indicates how long the router should be used as a default router",
      "Specifies how long the router has been running",
      "Sets the TTL for packets",
      "Determines prefix validity"
    ],
    "correct": [0],
    "explanation": "Router Lifetime tells hosts how long (in seconds) they should consider this router as a valid default router. A value of 0 means it should not be used as default."
  },
  {
    "question": "What security risk does IPv6 address scanning face compared to IPv4?",
    "options": [
      "The huge address space makes brute-force scanning impractical",
      "IPv6 addresses are encrypted by default",
      "IPv6 doesn't allow port scanning",
      "All IPv6 addresses are hidden from scanners"
    ],
    "correct": [0],
    "explanation": "With 2^64 possible addresses per subnet, random scanning is computationally infeasible in IPv6, unlike IPv4's smaller address spaces."
  }
]

# Combine existing and new questions
all_questions = existing_questions + new_questions

# Save with compact correct arrays
output_lines = ['[']
for i, question in enumerate(all_questions):
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
    if question.get('multipleCorrect'):
        output_lines.append(f'    "multipleCorrect": true,')
    
    output_lines.append(f'    "explanation": {json.dumps(question["explanation"], ensure_ascii=False)}')
    comma = ',' if i < len(all_questions) - 1 else ''
    output_lines.append(f'  }}{comma}')

output_lines.append(']')

# Write to file
with open('02.json', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print(f"✓ Successfully added {len(new_questions)} new questions")
print(f"✓ Total questions now: {len(all_questions)}")
print(f"\nNew questions cover:")
print("  • Duplicate Address Detection (DAD) - 6 questions")
print("    - DAD process and messages")
print("    - Tentative address state")
print("    - DupAddrDetectTransmits")
print("    - Optimistic DAD")
print("  • Neighbor Unreachability Detection (NUD) - 5 questions")
print("    - 5-state machine (INCOMPLETE, REACHABLE, STALE, DELAY, PROBE)")
print("    - State transitions")
print("    - Reachability confirmation")
print("  • Autoconfiguration - 6 questions")
print("    - SLAAC prefix information")
print("    - Valid vs preferred lifetime")
print("    - EUI-64 interface ID generation")
print("    - A and L flags")
print("    - Router lifetime")
print("  • Security - 13 questions")
print("    - Privacy Extensions (RFC 4941)")
print("    - SEND protocol details")
print("    - CGA generation and components")
print("    - RSA signatures and timestamps")
print("    - Nonce option")
print("    - Attack prevention")
