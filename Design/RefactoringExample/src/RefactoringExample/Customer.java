package RefactoringExample;

import java.util.ArrayList;
import java.util.Formatter;
import java.util.List;

/**
 * A class representing a customer in the application.
 *
 * @author Martin Fowler
 * @author Zachary Palmer
 */
public class Customer
{
private String name;
private List<Rental> rentals = new ArrayList<Rental>();

public Customer(String name)
{
this.name = name;
}

public String getName()
{
return name;
}

public void addRental(Rental rental)
{
this.rentals.add(rental);
}

public String generateStatement()
{
double totalAmount = 0;
int frequentRenterPoints = 0;
Formatter formatter = new Formatter();
formatter.format("Rental Record for %s\n", getName());
for (Rental rental : this.rentals)
{
double num = 0;
num = rental.getCharge();

// determine amounts for each line
// add frequent renter points
frequentRenterPoints += rental.getFrequentRentalPoints();
// add bonus for a two day new release rental

// show figures for this rental
formatter.format("    %-40s  (%02d)  $%5.2f\n", rental.getMovie().getTitle(), rental.getDaysRented(), rental.getCharge());
totalAmount += rental.getCharge();
}



// add footer lines
formatter.format("Amount owed is $%5.2f\n", totalAmount);
formatter.format("You earned %d frequent renter points",frequentRenterPoints);

String result = formatter.out().toString();
formatter.close();
return result;
}
private double amountFor(Rental arental) {
return arental.getCharge();
}

// private double getTotalCharge() {
//
// }
}
