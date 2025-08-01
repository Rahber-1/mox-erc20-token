# pragma version ^0.4.0

"""
@license MIT
@title snek_token
@author Rahber Ahmed
@notice This is an ERC20 token written in Vyper
"""

# Import ERC20 interface
from ethereum.ercs import IERC20

implements: IERC20

# Import SnekMate modules
from lib.pypi.snekmate.auth import ownable as ow
from lib.pypi.snekmate.tokens import erc20

# Initialize modules
initializes: ow
initializes: erc20[ownable := ow]

exports: erc20.__interface__

# Token constants
NAME: constant(String[25]) = "snek_token"
SYMBOL: constant(String[5]) = "snek"
DECIMALS: constant(uint8) = 18
EIP712_VERSION: constant(String[20]) = "1"


@deploy
def __init__(initial_supply: uint256):
    ow.__init__()  # Initialize Ownable module
    erc20.__init__(NAME, SYMBOL, DECIMALS, NAME, EIP712_VERSION)  # Init ERC20
    erc20._mint(msg.sender, initial_supply)  # Mint tokens to deployer

@external
def super_mint():
    # We forget to update the total supply!
    amount: uint256 = as_wei_value(100, "ether")
    erc20.totalSupply += amount
    
    erc20.balanceOf[msg.sender] = erc20.balanceOf[msg.sender] + amount
    