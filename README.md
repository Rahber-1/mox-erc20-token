snek_token 🐍

An ERC-20 token implementation in Vyper with extended functionality and property-based fuzz testing using Boa and Hypothesis.

📊 Overview

This project implements an ERC20-compatible token named snek_token in Vyper. It includes ownership controls and mint/burn features via the SnekMate module system. In addition to conventional unit tests, stateful fuzzing is implemented using hypothesis.stateful to test edge cases and ensure invariants are preserved.

🚀 Features

Custom ERC20 token built with Vyper

Ownership management (Ownable pattern)

Controlled minting and burning

super_mint() with fuzz testing to highlight hidden bugs

Unit and stateful fuzz tests using boa and hypothesis

🚧 Project Structure

snek-token/
├── contracts/
│   └── snek_token.vy         # Main Vyper contract
├── script/
│   ├── snek_token_deploy.py   # Deployment and bootstrap logic
├── test/
│   ├── test_snek_token.py      # Unit tests with Boa
│   └── fuzz_snek_token.py      # Stateful fuzzing tests
├── lib/
│   └── pypi/snekmate/         # SnekMate modules (auth, erc20)
└── README.md

📝 Contract Details

NAME: snek_token

SYMBOL: snek

DECIMALS: 18



🚄 Getting Started

1. Installation

Ensure Python 3.12+ is installed and set up a virtual environment:

python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Make sure the following are installed:

boa

hypothesis

eth_utils

2. Compile Contract 

mox compile contracts/snek_token.vy

3. Seoplia testnet
mox run snek_token_deploy --network sepolia

tx broadcasted: 0x7a22cca70a83a73a27ae9b34740e1cd3201bc802bff638ff4c53d5e0556aae0d
0x7a22cca70a83a73a27ae9b34740e1cd3201bc802bff638ff4c53d5e0556aae0d mined in block 0x457ef4790ac1fc164bf7753cdcffa29c9d264dae0b774c123fb98a710376f571!
contract deployed at 0x20D135B468f74FFBD88Cd49aa106CcCB4C32E828
the snek_token contract has been deploy to 0x20D135B468f74FFBD88Cd49aa106CcCB4C32E828

🎮 Testing

✅ Unit Tests

pytest test/test_snek_token.py

🧪 Stateful Fuzzing

pytest test/fuzz_snek_token.py

This runs property-based tests that verify important invariants over multiple contract state transitions.

💡 Invariants Checked

Total Supply Bounds:

assert balance <= totalSupply

No user's balance may exceed the total supply.

Non-Negative Balances:

assert balance >= 0

No account should ever have a negative balance.

🤖 Example Deployment

from script.snek_token_deploy import deploy
contract = deploy()

📄 License

MIT © 2025 

