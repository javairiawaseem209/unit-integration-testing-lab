import pytest
from bank_app import deposit, withdraw, calculate_interest, check_loan_eligibility

# ****** Tests for deposit(balance, amount) ******
def test_deposit_valid():
    assert deposit(100, 50) == 150
    assert deposit(0, 1) == 1

def test_deposit_boundary():
    assert deposit(100, 0.01) == 100.01

def test_deposit_invalid():
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        deposit(100, 0)
    with pytest.raises(ValueError):
        deposit(100, -10)

# ****** Tests for withdraw(balance, amount) ******
def test_withdraw_valid():
    assert withdraw(100, 50) == 50
    assert withdraw(50, 50) == 0

def test_withdraw_boundary():
    assert withdraw(100, 0.01) == 99.99

def test_withdraw_invalid():
    with pytest.raises(ValueError, match="Withdraw amount must be positive"):
        withdraw(100, 0)
    with pytest.raises(ValueError):
        withdraw(100, -5)
    with pytest.raises(ValueError, match="Insufficient balance"):
        withdraw(50, 100)

# ****** Tests for calculate_interest(balance, rate, years) ******
def test_calculate_interest_valid():
    assert calculate_interest(1000, 5, 2) == pytest.approx(1102.5)
    assert calculate_interest(0, 10, 5) == 0
    assert calculate_interest(1000, 0, 3) == 1000

def test_calculate_interest_invalid():
    with pytest.raises(ValueError, match="Balance cannot be negative"):
        calculate_interest(-1, 5, 2)
    with pytest.raises(ValueError, match="Rate cannot be negative"):
        calculate_interest(1000, -5, 2)

# ****** Tests for check_loan_eligibility(balance, credit_score) ******
def test_check_loan_eligibility_true():
    assert check_loan_eligibility(5000, 700) is True
    assert check_loan_eligibility(10000, 750) is True

def test_check_loan_eligibility_false():
    assert check_loan_eligibility(4999, 700) is False
    assert check_loan_eligibility(5000, 699) is False

def test_check_loan_eligibility_invalid():
    with pytest.raises(ValueError, match="Balance cannot be negative"):
        check_loan_eligibility(-100, 700)
