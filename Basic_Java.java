// Subscript - the method of pulling out an element from a string.
String name = "Raj";
System.out.println(name.charAt(0));

// Nested If else
Scanner sc = new Scanner(System.in);
System.out.print("Give in cm.. ");
int height = sc.nextInt();
int bill = 0;
if (height >= 120) {
    System.out.println("eligible");
    System.out.print("Age pls.. ");
    int age = sc.nextInt();
    if (age < 12) {
        bill = 5;
    } else if (age <= 18) {
        bill = 7;
    } else {
        bill = 10;
    }
    System.out.println("total bill " + bill);
} else {
    System.out.println("not eligible");
}
sc.close();

// Random
import java.util.Random;
Random random = new Random();
int number = random.nextInt(10) + 1;
System.out.println(number);

// Use Lambda
int[] myList = {1, 2, 3};
for (int x : myList) {
    System.out.print(x * x + " ");
}

// Heighest Number
int[] numbers = {78, 89, 22, 90, 55, 23};
int highestNumber = 0;
int secondHighestNumber = 0;
for (int n : numbers) {
    if (n > highestNumber) {
        secondHighestNumber = highestNumber;
        highestNumber = n;
    } else if (n > secondHighestNumber && n != highestNumber) {
        secondHighestNumber = n;
    }
}
System.out.println(highestNumber);
System.out.println(secondHighestNumber);

// Lowest Number
int[] numbers = {10, 30, 20, 5, 4, 90, 80, 60};
int lowest = Integer.MAX_VALUE;
int secondLowest = Integer.MAX_VALUE;
for (int num : numbers) {
    if (num < lowest) {
        secondLowest = lowest;
        lowest = num;
    } else if (num < secondLowest && num != lowest) {
        secondLowest = num;
    }
}
System.out.println("Lowest: " + lowest);
System.out.println("Second Lowest: " + secondLowest);

// Prime_number
boolean isPrime = true;
for (int i = 2; i < number; i++) {
    if (number % i == 0) {
        isPrime = false;
    }
}
if (isPrime) {
    System.out.println("It's prime");
} else {
    System.out.println("It's not prime");
}
Scanner sc = new Scanner(System.in);
System.out.print("Enter number: ");
int n = sc.nextInt();
primeCheck(n);
sc.close();