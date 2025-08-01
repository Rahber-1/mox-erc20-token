from script.snek_token_deploy import deploy,INITIAL_SUPPLY
import boa 

RANDOM_USER=boa.env.generate_address("RANDOM_USER")
RANDOM_USER2=boa.env.generate_address("RANDOM_USER2")
ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"



def test_total_supply():
    snek_token=deploy()
    assert snek_token.totalSupply()==INITIAL_SUPPLY

def test_snek_token_can_emit_events():
    snek_token=deploy()
    with boa.env.prank(snek_token.owner()):
        snek_token.transfer(RANDOM_USER,INITIAL_SUPPLY)
        logs=snek_token.get_logs()
       # log_owner=logs[0].topics[0]
       # assert log_owner ==snek_token.owner()
    assert snek_token.balanceOf(RANDOM_USER)==INITIAL_SUPPLY

def test_only_owner_can_mint():
    snek_token=deploy()
    with boa.reverts():
        with boa.env.prank(RANDOM_USER):
            snek_token.mint(RANDOM_USER,INITIAL_SUPPLY)
        

def test_more_than_initial_supply_can_not_be_transferred():
    snek_token=deploy()
    with boa.reverts():
        with boa.env.prank(snek_token.owner()):
            snek_token.transfer(RANDOM_USER, INITIAL_SUPPLY+1) 

def test_only_owner_can_burn_token():
    snek_token=deploy()
    with boa.env.prank(snek_token.owner()):
        snek_token.burn(INITIAL_SUPPLY-1)

def test_non_owner_can_have_tokens():
    snek_token=deploy()
    with boa.env.prank(snek_token.owner()):
        snek_token.transfer(RANDOM_USER,INITIAL_SUPPLY//2)
    assert snek_token.balanceOf(RANDOM_USER) ==INITIAL_SUPPLY//2

def test_non_owner_can_transfer_from_his_tokens():
    snek_token=deploy()
    with boa.env.prank(snek_token.owner()):
        snek_token.transfer(RANDOM_USER,INITIAL_SUPPLY)
    print(f"balance of RANDOM_USER is {snek_token.balanceOf(RANDOM_USER)}")
    with boa.env.prank(RANDOM_USER):
        snek_token.transfer(RANDOM_USER2,INITIAL_SUPPLY//2)

def test_ownership_can_be_renounced():
    snek_token=deploy()
    with boa.env.prank(snek_token.owner()):
        snek_token.renounce_ownership()
        assert snek_token.owner() ==ZERO_ADDRESS

def test_owner_can_not_mint_after_ownership_renounced():
    snek_token=deploy()
    with boa.env.prank(snek_token.owner()):
        snek_token.renounce_ownership()
    with boa.reverts():
        with boa.env.prank(snek_token.owner()):
            snek_token.mint(snek_token.owner(),INITIAL_SUPPLY)

def test_ownership_can_be_transferred():
    snek_token=deploy()
    with boa.env.prank(snek_token.owner()):
        snek_token.transfer_ownership(RANDOM_USER)
    assert snek_token.owner() ==RANDOM_USER

def test_minter_can_be_set():
    snek_token = deploy()
    
    with boa.env.prank(snek_token.owner()):
        snek_token.set_minter(RANDOM_USER, True)
    
    assert snek_token.is_minter(RANDOM_USER) == True


    
        









        
    
        



    

    
        
        
