//Subclass
class LoanAcct extends BankAcct
{
  protected double _rate;
  protected double _limit;

  public LoanAcct(int aNum, double bal, double rate, double limit) {
    // Write your code here
    super(aNum, bal);
    _rate = rate;
    _limit = limit;
  }

  //New method in subclass
  public void payInterest() {
    // Write your code here
    _balance += _rate * _limit;
  }

  //Method Overriding
  public boolean withdraw( double amount ) {
    // Write your code here
    double new_balance = _balance - amount;
    if (new_balance < -_limit) {
      return false;
    }
    _balance = new_balance;
    return true;
  }

  public void deposit( double amount ) {
    // Write your code here
    _balance += amount;
  }
}