import java.util.Arrays;
import java.util.Scanner;
import java.util.ArrayList;

public class TowerOfHanoi {
  String name;
  ArrayList[] peg;
  int numDiscs;

  public TowerOfHanoi(String name, int n) {
    this.name = name;
    this.numDiscs = n;
    this.peg = new ArrayList[3];
    for (int i = 0; i < 3; i++) {
      this.peg[i] = new ArrayList<Integer>();
    }

    for (int i = 0; i < n; i++) {
      this.peg[0].add(i);
    }
  }

  private void moveDisc(int src, int des) {
    int last_idx = this.peg[src].size() - 1;
    Object popped = this.peg[src].remove(last_idx);
    this.peg[des].add(popped);
    printTower();
  }

  public void printTower() {
    for (int i = 0; i < this.peg.length; i++) {
      if (this.peg[i].isEmpty()) {
        System.out.print("[ ]");
      } else {
        String formatted_string = this.peg[i].toString()
                .replace(",", "")
                .replace("[", "[ ")
                .replace("]", " ]");
        System.out.printf(formatted_string);
      }

      if (i != this.peg.length - 1) {
        System.out.print(", ");
      }
    }
    System.out.println();
  }

  public void makeMoves(int n, int src, int des, int aux) {
    if (n <= 0) return;
    makeMoves(n-1, src, aux, des);
    moveDisc(src, des);
    makeMoves(n-1, aux, des, src);
    return;
  }
  
  public static void main(String args[]) {
    Scanner input = new Scanner(System.in);
    System.out.println("Enter number of disks: ");
    int n = input.nextInt();
    TowerOfHanoi t = new TowerOfHanoi("Hanoi", n);
    t.printTower();
    t.makeMoves( n, 0, 2, 1 );
  }
  
}
  