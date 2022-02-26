import java.util.*;
class Placement{
 static Scanner sc;
public static void main(String[] args)
{     sc = new Scanner(System.in);
      int cse,ece,mech,hscore;
      System.out.println("Enter the no of students placed in CSE:");
      cse = sc.nextInt();
      System.out.println("Enter the no of students placed in ECE:");
      ece = sc.nextInt();
      System.out.println("Enter the no of students placed in MECH:");
      mech = sc.nextInt();
      if (cse <  0 || ece < 0 || mech < 0)
       System.out.println("Input is Invalid");
      else{
      if(cse >= mech && cse >= ece)
       hscore = cse;
      else if(ece >= cse && ece >= mech)
       hscore = ece;
      else
       hscore = mech;
      if(cse == hscore && ece == hscore && mech == hscore)
       System.out.println("None of the department has got the highest placement");
      else if(cse == hscore && ece == hscore)
       System.out.println("Highest placement\nCSE\nECE");
      else if(ece == hscore && mech == hscore)
       System.out.println("Highest placement\nECE\nMECH");
      else if(cse == hscore && mech == hscore)
       System.out.println("Highest placement\nCSE\nMECH");
      else if(cse == hscore)
       System.out.println("Highest placement\nCSE");
      else if(ece == hscore)
       System.out.println("Highest placement\nECE");
      else
       System.out.println("Highest placement\nMECH");
      }
}
}
