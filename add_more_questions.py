import json

# Load existing questions
with open('02.json', 'r', encoding='utf-8') as f:
    existing_questions = json.load(f)

# New questions focusing on IPv6, NDP, mobile support, security, and QoS
new_questions = [
  {
    "question": "Which NDP message is sent by routers to proactively advertise their presence?",
    "options": [
      "Router Solicitation",
      "Router Advertisement",
      "Neighbor Solicitation",
      "Redirect"
    ],
    "correct": [1],
    "explanation": "Router Advertisement messages are sent periodically by routers or in response to Router Solicitation messages to advertise their presence and configuration parameters."
  },
  {
    "question": "What information can be included in NDP Router Advertisements?",
    "options": [
      "Prefix information for SLAAC",
      "MTU size for the link",
      "Flags indicating address configuration method",
      "MAC addresses of all hosts"
    ],
    "correct": [0, 1, 2],
    "multipleCorrect": True,
    "explanation": "Router Advertisements can include prefixes for autoconfiguration, link MTU, hop limit values, and flags (M and O) for address and other configuration."
  },
  {
    "question": "In Mobile IPv6, what is the purpose of a Home Agent?",
    "options": [
      "To intercept packets destined for the mobile node's home address",
      "To assign temporary IP addresses",
      "To compress IPv6 headers for mobile devices",
      "To tunnel packets to the mobile node's current location"
    ],
    "correct": [0, 3],
    "multipleCorrect": True,
    "explanation": "The Home Agent intercepts packets sent to the mobile node's home address and tunnels them to the mobile node's care-of address at its current location."
  },
  {
    "question": "What is a Care-of Address in Mobile IPv6?",
    "options": [
      "The permanent address assigned to a mobile node",
      "A temporary address indicating the mobile node's current location",
      "The address of the home agent",
      "The address used for return routability testing"
    ],
    "correct": [1],
    "explanation": "A care-of address is a temporary IPv6 address that reflects the mobile node's current point of attachment to the Internet."
  },
  {
    "question": "Which IPv6 security feature was mandatory in the original specification?",
    "options": [
      "TLS",
      "IPsec",
      "SSH",
      "DNSSEC"
    ],
    "correct": [1],
    "explanation": "IPsec was originally mandatory in IPv6 (though this requirement was later relaxed). It provides authentication, integrity, and confidentiality at the network layer."
  },
  {
    "question": "What are the two main IPsec protocols used in IPv6?",
    "options": [
      "AH (Authentication Header)",
      "SSL (Secure Sockets Layer)",
      "ESP (Encapsulating Security Payload)",
      "TLS (Transport Layer Security)"
    ],
    "correct": [0, 2],
    "multipleCorrect": True,
    "explanation": "AH provides authentication and integrity, while ESP provides confidentiality (encryption) in addition to authentication and integrity."
  },
  {
    "question": "How does IPv6 use the Traffic Class field for QoS?",
    "options": [
      "To mark packets with priority or DSCP values",
      "To encrypt quality-sensitive traffic",
      "To compress multimedia packets",
      "To determine routing paths"
    ],
    "correct": [0],
    "explanation": "The Traffic Class field (8 bits) is used similarly to ToS in IPv4, allowing packets to be marked with DiffServ Code Points (DSCP) for QoS treatment."
  },
  {
    "question": "What security risk is associated with NDP in IPv6?",
    "options": [
      "NDP messages can be spoofed without protection",
      "NDP automatically encrypts all traffic",
      "NDP prevents all man-in-the-middle attacks",
      "NDP requires certificate authentication by default"
    ],
    "correct": [0],
    "explanation": "Without SEND (Secure Neighbor Discovery), NDP messages are vulnerable to spoofing attacks, allowing attackers to redirect traffic or perform DoS attacks."
  },
  {
    "question": "What is SEND (Secure Neighbor Discovery)?",
    "options": [
      "A protocol that uses cryptographic signatures to secure NDP messages",
      "A compression algorithm for IPv6 packets",
      "A routing protocol for IPv6 networks",
      "A method for address allocation"
    ],
    "correct": [0],
    "explanation": "SEND uses Cryptographically Generated Addresses (CGA) and RSA signatures to authenticate NDP messages and prevent spoofing attacks."
  },
  {
    "question": "Which type of attack can be performed by spoofing Router Advertisement messages?",
    "options": [
      "Man-in-the-middle attack by advertising a rogue router",
      "Denial of service by advertising invalid prefixes",
      "SQL injection",
      "Redirect legitimate traffic to attacker"
    ],
    "correct": [0, 1, 3],
    "multipleCorrect": True,
    "explanation": "Rogue RA attacks can redirect traffic, cause DoS by invalidating legitimate prefixes, or position the attacker as a man-in-the-middle."
  },
  {
    "question": "What is the purpose of the Redirect message in NDP?",
    "options": [
      "To inform a host of a better first-hop router for a specific destination",
      "To redirect DNS queries to a different server",
      "To change a host's IPv6 address",
      "To block malicious traffic"
    ],
    "correct": [0],
    "explanation": "Routers send Redirect messages to inform hosts about better routes to specific destinations, optimizing path selection."
  },
  {
    "question": "In Mobile IPv6, what is Route Optimization?",
    "options": [
      "A mechanism allowing direct communication between correspondent nodes and mobile nodes",
      "Compressing routing tables",
      "Reducing the number of hops in a network",
      "Automatically selecting the fastest ISP"
    ],
    "correct": [0],
    "explanation": "Route Optimization allows correspondent nodes to send packets directly to a mobile node's care-of address, bypassing the home agent for efficiency."
  },
  {
    "question": "What is Binding Update in Mobile IPv6?",
    "options": [
      "A message sent by the mobile node to register its care-of address",
      "An update to the routing table",
      "A security certificate renewal",
      "A DNS record update"
    ],
    "correct": [0],
    "explanation": "Binding Update messages inform the home agent (and optionally correspondent nodes) about the mobile node's current care-of address."
  },
  {
    "question": "Which IPv6 extension header is used by IPsec for authentication?",
    "options": [
      "Fragment Header",
      "Authentication Header (AH)",
      "Routing Header",
      "Hop-by-Hop Options"
    ],
    "correct": [1],
    "explanation": "The Authentication Header provides connectionless integrity, data origin authentication, and optional anti-replay protection for IPv6 packets."
  },
  {
    "question": "What is the main difference between AH and ESP in IPsec?",
    "options": [
      "AH provides authentication only, ESP provides encryption and authentication",
      "AH is for IPv4, ESP is for IPv6",
      "AH is faster than ESP",
      "ESP cannot work with NAT"
    ],
    "correct": [0],
    "explanation": "AH provides authentication and integrity but not encryption. ESP can provide confidentiality (encryption), authentication, and integrity."
  },
  {
    "question": "How does IPv6 Privacy Extensions enhance security?",
    "options": [
      "By generating temporary random interface identifiers",
      "By encrypting all IPv6 headers",
      "By hiding the MAC address in Router Advertisements",
      "By using shorter addresses"
    ],
    "correct": [0],
    "explanation": "Privacy Extensions (RFC 4941) generate temporary, changing interface IDs instead of using MAC-based identifiers, preventing tracking across networks."
  },
  {
    "question": "What is a Cryptographically Generated Address (CGA)?",
    "options": [
      "An IPv6 address generated from a public key hash",
      "An encrypted IPv6 address",
      "A randomly generated temporary address",
      "An address assigned by DHCP with encryption"
    ],
    "correct": [0],
    "explanation": "CGAs use a hash of a public key to generate the interface identifier, allowing proof of address ownership through digital signatures."
  },
  {
    "question": "Which NDP option is used to advertise the link-layer address?",
    "options": [
      "Source Link-Layer Address option",
      "Target Link-Layer Address option",
      "MTU option",
      "Prefix Information option"
    ],
    "correct": [0, 1],
    "multipleCorrect": True,
    "explanation": "Source Link-Layer Address is used in Router/Neighbor Solicitation and Router/Neighbor Advertisement. Target Link-Layer Address is used in Neighbor Advertisement and Redirect."
  },
  {
    "question": "What happens during the Neighbor Unreachability Detection (NUD) process?",
    "options": [
      "Hosts verify that neighbors are still reachable",
      "Routers detect link failures",
      "The network assigns new addresses",
      "Hosts discover available bandwidth"
    ],
    "correct": [0],
    "explanation": "NUD allows hosts to track the reachability status of neighbors and detect when a neighbor is no longer reachable, updating the neighbor cache accordingly."
  },
  {
    "question": "What are the possible states in the NDP neighbor cache?",
    "options": [
      "INCOMPLETE - waiting for address resolution",
      "REACHABLE - known to be reachable",
      "STALE - no recent reachability confirmation",
      "ENCRYPTED - secure connection established"
    ],
    "correct": [0, 1, 2],
    "multipleCorrect": True,
    "explanation": "NDP defines states including INCOMPLETE, REACHABLE, STALE, DELAY, and PROBE to track neighbor reachability. There is no ENCRYPTED state."
  },
  {
    "question": "In Mobile IPv6, what is Return Routability Test (RRT)?",
    "options": [
      "A security mechanism to verify the mobile node owns both home and care-of addresses",
      "A speed test for mobile connections",
      "A method to find the shortest path",
      "A QoS measurement tool"
    ],
    "correct": [0],
    "explanation": "RRT is a security procedure where correspondent nodes verify that the mobile node is reachable at both its home address and care-of address before enabling route optimization."
  },
  {
    "question": "What is the purpose of the 'O' flag in Router Advertisements?",
    "options": [
      "Indicates hosts should use DHCPv6 for other configuration (not addresses)",
      "Enables IPv6 over IPv4 tunneling",
      "Optimizes routing tables",
      "Opens firewall ports"
    ],
    "correct": [0],
    "explanation": "The Other configuration (O) flag tells hosts to use DHCPv6 to obtain additional configuration information like DNS servers, while still using SLAAC for addresses."
  },
  {
    "question": "How does IPsec transport mode differ from tunnel mode?",
    "options": [
      "Transport mode encrypts only the payload, tunnel mode encrypts the entire packet",
      "Transport mode is faster than tunnel mode",
      "Tunnel mode creates a new IP header, transport mode doesn't",
      "Transport mode works only with TCP"
    ],
    "correct": [0, 2],
    "multipleCorrect": True,
    "explanation": "In transport mode, only the payload is protected. In tunnel mode, the entire original packet is encapsulated in a new IPv6 packet, often used for VPNs."
  },
  {
    "question": "What is the Flow Label field used for in IPv6 QoS?",
    "options": [
      "To identify packets belonging to the same flow for consistent QoS treatment",
      "To encrypt flows",
      "To count the number of flows",
      "To compress packet headers"
    ],
    "correct": [0],
    "explanation": "The 20-bit Flow Label allows routers to identify packets belonging to the same flow and handle them consistently without examining upper-layer headers."
  },
  {
    "question": "Which security feature helps prevent IPv6 address scanning attacks?",
    "options": [
      "The large address space makes brute-force scanning impractical",
      "Randomized interface identifiers",
      "SEND protocol",
      "All subnet addresses are always allocated"
    ],
    "correct": [0, 1],
    "multipleCorrect": True,
    "explanation": "The huge IPv6 address space (2^64 addresses per subnet) makes scanning impractical, and randomized IDs prevent predictable addressing patterns."
  },
  {
    "question": "What is a Mobile IPv6 Correspondent Node?",
    "options": [
      "A node communicating with a mobile node",
      "A router managing mobile connections",
      "A DNS server for mobile devices",
      "A backup home agent"
    ],
    "correct": [0],
    "explanation": "A correspondent node is any IPv6 node that is communicating with a mobile node, which may be mobile or stationary."
  },
  {
    "question": "How does NDP prevent address conflicts?",
    "options": [
      "Through Duplicate Address Detection (DAD)",
      "By using DHCP exclusively",
      "Through encryption",
      "By limiting the number of hosts"
    ],
    "correct": [0],
    "explanation": "DAD uses Neighbor Solicitation messages to check if an address is already in use before a node configures it on its interface."
  },
  {
    "question": "What is the Router Preference option in NDP?",
    "options": [
      "Allows routers to advertise their preference level (high, medium, low)",
      "Sets bandwidth limits for routers",
      "Configures router encryption strength",
      "Determines router uptime"
    ],
    "correct": [0],
    "explanation": "The Router Preference option allows routers to indicate their relative preference for use as a default router, helping hosts choose the best default gateway."
  },
  {
    "question": "Which extension header would be used for end-to-end encryption in IPv6?",
    "options": [
      "Hop-by-Hop Options",
      "ESP (Encapsulating Security Payload)",
      "Fragment Header",
      "Routing Header"
    ],
    "correct": [1],
    "explanation": "ESP provides encryption and can be used in transport mode for end-to-end encryption between source and destination."
  },
  {
    "question": "What is RA Guard?",
    "options": [
      "A security feature that filters Router Advertisement messages",
      "A QoS mechanism",
      "A routing protocol",
      "A compression algorithm"
    ],
    "correct": [0],
    "explanation": "RA Guard is a switch security feature that blocks rogue Router Advertisement messages from unauthorized devices, preventing attacks."
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
print("  • NDP protocol details (messages, options, cache states)")
print("  • Mobile IPv6 (Home Agent, Care-of Address, Binding Updates, Route Optimization)")
print("  • Security (IPsec, AH, ESP, SEND, CGA, Privacy Extensions, RA Guard)")
print("  • QoS (Traffic Class, Flow Label)")
