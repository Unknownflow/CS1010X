class TestBankAcct
{
  public static void transfer (BankAcct fromAcct, 
                               BankAcct toAcct, double amt) 
  {
    if (fromAcct.withdraw(amt))
      toAcct.deposit(amt);
    else
      System.out.println("Money not enough");
  }
  public static void main( String[] args )
  {
    BankAcct ba1 = new BankAcct();
    BankAcct ba2 = new BankAcct(1234, 99.99);  
    ba1.deposit( 1000 );
    ba2.withdraw( 50.25 );      
    transfer( ba1, ba2, 50.0);
    System.out.println("printing ba1");
    ba1.print();  
    System.out.println("printing ba2");
    ba2.print();
    transfer( ba2, ba1, 100);
    System.out.println("printing ba1");
    ba1.print();
    System.out.println("printing ba2");
    ba2.print();

    SavingAcct sa1 = new SavingAcct(1, 100, 0.1);
    LoanAcct la1 = new LoanAcct(1, -100, 0.1, 120);
    transfer(sa1, la1, 10);
    transfer(sa1, la1, 110);
    transfer(la1, sa1, 10);
    transfer(la1, sa1, 25);
    la1.payInterest();
  }
} 
