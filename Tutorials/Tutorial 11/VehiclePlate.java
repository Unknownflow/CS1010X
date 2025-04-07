import java.util.*;

public class VehiclePlate {
 
   public static void main(String[] args) {

      Scanner stdIn = new Scanner(System.in);

      System.out.print("Vehicle Plate (excluding the checksum alphabet at the end): ");
      String plate = stdIn.nextLine();
      plate = plate.toUpperCase();
      String prefix =  plate.replaceAll("[0123456789]", "");
      int suffix = Integer.parseInt(plate.replaceAll("[a-zA-Z]",""));
      char checkSum = generateCheckSum (prefix, suffix);
      System.out.println(checkSum);

      System.out.println("Vehicle Plate is: " + prefix + " " + suffix + " " + checkSum);

   } // end main

   /*********************************************************
      
   **********************************************************/
   public static char generateCheckSum(String prefix, int suffix) {
      int[] fixed_num = {9, 4, 5, 4, 3, 2};
      String[] remainder_letter = {"A", "Z", "Y", "X", "U", "T", "S", "R", "P", "M",
      "L", "K", "J", "H", "G", "E", "D", "C", "B"};
      int[] num_list = {0, 0, 0, 0, 0, 0};

      char a = 'A';
      // if prefix length is 1, the letter is at 2nd pos
      if (prefix.length() == 1) {
         char character = prefix.charAt(0);
         int ascii = character - a + 1;
         num_list[1] = ascii;
      } else {
         // only last 2 prefix letter are taken
         String temp_prefix = prefix.substring(prefix.length() - 2);
         for (int i = 0; i < temp_prefix.length(); i++) {
            char character = temp_prefix.charAt(i);
            int ascii = character - a + 1;
            num_list[i] = ascii;
         }
      }

      String string_suffix = String.valueOf(suffix);
      // add 0 in front of the number until length of number is 4
      while (string_suffix.length() < 4) {
         string_suffix = "0".concat(string_suffix);
      }

      // adding number to arr
      for (int i = 0; i < string_suffix.length(); i++) {
         char num = string_suffix.charAt(i);
         int integer = Character.getNumericValue(num);
         num_list[2+i] = integer;
      }

      int checksum = 0;
      for (int i = 0; i < fixed_num.length; i++) {
         checksum += fixed_num[i] * num_list[i];
      }
      checksum = checksum % 19;
      String suffix_letter = remainder_letter[checksum];
      char suffix_char = suffix_letter.charAt(0);
      return suffix_char;
   }// end generateCheckSum

}// end class 