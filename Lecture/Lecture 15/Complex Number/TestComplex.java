class TestComplex {
  public static void main(String [] args) {
    // Testing ComplexCart
    Complex a = new ComplexCart(10.0, 12.0);
    Complex b = new ComplexCart(1.0, 2.0); 
    a.add(b);
    System.out.println("a=a+b is " +  a );
    a.minus(b);
    System.out.println("a-b (which is the original a) is " + a); 
    System.out.println("Angle of a is " + a.angle()); 
    a.times(b);
    System.out.println("a x b is " + a);
    Complex test1 = new ComplexCart(3,4);
    Complex test2 = new ComplexCart(5,6);
    test1.divides(test2);
    System.out.println("test1/test2 is " + test1);
    Complex test3 = new ComplexCart(3,-4);
    Complex test4 = new ComplexCart(-5,6);
    test3.divides(test4);
    System.out.println("test3/test4 is " + test3);

    
    // Testing ComplexPolar
    Complex c = new ComplexPolar(10.0,Math.PI/6.0);
    Complex d = new ComplexPolar(10.0,Math.PI/3.0);
    System.out.println("c is " +  c);
    System.out.println("d is " +  d);
    c.add(d);
    System.out.println("c=c+d is " +  c);
    c.minus(d);
    System.out.println("c-d (which is the original c) is " + c);
    c.times(d);
    System.out.println("c=c*d is " + c);
    
    // Testing Combine
    System.out.println("a is " + a );
    System.out.println("d is " + d );
    a.minus(d);
    System.out.println("a=a-d is " + a);
    a.times(d);
    System.out.println("a=a*d is " + a);
    d.add(a);
    System.out.println("d=d+a is " + d);
    d.times(a);
    System.out.println("d=d*a is " + d);
  }
}

