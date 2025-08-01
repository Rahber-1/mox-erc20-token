import boa
from eth.constants import UINT_256_MAX,ZERO_ADDRESS
from hypothesis.stateful import (
    RuleBasedStateMachine,
    invariant,
    rule,
    initialize
)
from boa.test.strategies import strategy
from boa.util.abi import Address
from hypothesis import settings,assume
from hypothesis import strategies as st

from script.snek_token_deploy import deploy

MINTER_SIZE=10

class super_mint_fuzzer(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
    @initialize()
    def setup(self):
        self.contract=deploy()
        self.minters=[Address("0x" + ZERO_ADDRESS.hex())]
        while Address("0x" + ZERO_ADDRESS.hex()) in self.minters:
            self.minters=[boa.env.generate_address() for i in range(MINTER_SIZE)]
    
    @rule(
        amount=strategy("uint256"),
        minter_seed=st.integers(min_value=0,max_value=MINTER_SIZE-1)
    )
    def mint(self,amount,minter_seed):
        assume(self.contract.totalSupply()+amount <UINT_256_MAX)
        address=self.minters[minter_seed]
        self.contract.mint(address,amount)
    @rule(
        minter_seed=st.integers(min_value=0,max_value=MINTER_SIZE-1)
    )
    def super_mint(self,minter_seed):
        address=self.minters[minter_seed]
        with boa.env.prank(address):
            self.contract.super_mint()
    
    @invariant()
    def totalBalance_of_users_must_not_exceed_totalSupply(self):
        totalSupply=self.contract.totalSupply()
        for address in self.minters:
            balance =self.contract.balanceOf(address)
            assert balance <=totalSupply,f"balance of {address} have exceeded totalSupply"

    @invariant()
    def no_account_has_negative_balance(self):
        for address in self.minters:
            balance=self.contract.balanceOf(address)
            assert balance>=0, f"balance of {address} is negative"


super_mint_fuzzer=super_mint_fuzzer.TestCase
super_mint_fuzzer.settings = settings(max_examples=100, stateful_step_count=20)


