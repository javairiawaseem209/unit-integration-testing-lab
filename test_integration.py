import pytest
from bank_app import calculate_interest, check_loan_eligibility, transfer



def test_transfer_and_calculate_interest():
    # Transfer funds, then calculate interest on updated receiver
    sender = 1000
    receiver = 500
    amount = 400
    rate = 5
    years = 2

    new_sender, new_receiver = transfer(sender, receiver, amount)

    # Check updated balances after transfer
    assert new_sender == 600
    assert new_receiver == 900

    # Calculate interest on the receiver's new balance
    interest = calculate_interest(new_receiver, rate, years)
    assert interest == pytest.approx(900 * (1 + rate/100)**years)

def test_transfer_check_loan_eligibility():
    # Transfer funds and check eligibility for sender and receiver
    sender = 6000
    receiver = 3000
    amount = 2000
    credit_score = 720

    new_sender, new_receiver = transfer(sender, receiver, amount)

    assert new_sender == 4000
    assert new_receiver == 5000

    # Check loan eligibility after transfer
    assert check_loan_eligibility(new_sender, credit_score) is False
    assert check_loan_eligibility(new_receiver, credit_score) is True
