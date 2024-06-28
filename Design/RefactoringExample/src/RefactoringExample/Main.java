package RefactoringExample;

import java.util.ArrayList;

import java.util.Arrays;

import java.util.Collections;

import java.util.List;


/**

 * An example main class used to demonstrate the behavior of the application.

 * 

 * @author Zachary Palmer

 */

public class Main

{

	// The following fields contain example data to be used in demonstrating this application.


	/** Some movies that the user may rent. */

	public static final Movie rosencrantzAndGuildensternAreDead = new Movie("Rosencrantz and Guildenstern are Dead",

			Movie.REGULAR);

	public static final Movie suckerpunch = new Movie("Suckerpunch", Movie.REGULAR);

	public static final Movie anastasia = new Movie("Anastasia", Movie.CHILDRENS);

	public static final Movie braveLittleToaster = new Movie("Brave Little Toaster, The", Movie.CHILDRENS);

	public static final Movie citizenKane3D = new Movie("Citizen Kane 3D", Movie.NEW_RELEASE);

	public static final Movie riverTamBeatsUpEveryone = new Movie("River Tam Beats Up Everyone", Movie.NEW_RELEASE);

	public static final Movie sneakers = new Movie("Sneakers", -1);


	/** Some customers which have rented movies. */

	public static final Customer gretelFishweaver;

	public static final Customer danielleDeBarbarac;

	public static final Customer richardCarlisle;

	public static final Customer murrayHewitt;

	public static final List<Customer> customers;


	// initializing the above

	static

	{

		gretelFishweaver = new Customer("Fishweaver, Gretel");

		gretelFishweaver.addRental(new Rental(rosencrantzAndGuildensternAreDead, 2));

		gretelFishweaver.addRental(new Rental(suckerpunch, 2));

		gretelFishweaver.addRental(new Rental(anastasia, 1));

		gretelFishweaver.addRental(new Rental(braveLittleToaster, 5));

		gretelFishweaver.addRental(new Rental(citizenKane3D, 1));

		gretelFishweaver.addRental(new Rental(riverTamBeatsUpEveryone, 3));


		danielleDeBarbarac = new Customer("de Barbarac, Danielle");

		danielleDeBarbarac.addRental(new Rental(anastasia, 2));

		danielleDeBarbarac.addRental(new Rental(anastasia, 2));

		danielleDeBarbarac.addRental(new Rental(anastasia, 2));


		richardCarlisle = new Customer("Carlisle, Sir Richard");

		richardCarlisle.addRental(new Rental(citizenKane3D, 10));


		murrayHewitt = new Customer("Hewitt, Murray");

		murrayHewitt.addRental(new Rental(sneakers, 947));


		customers = Collections.unmodifiableList(new ArrayList<Customer>(Arrays.asList(gretelFishweaver,

				danielleDeBarbarac, richardCarlisle, murrayHewitt)));

	}


	public static void main(String[] args)

	{

		for (Customer customer : customers)

		{

			System.out.println(customer.generateStatement());

			System.out.println("********************************************************************************");

		}

	}

}
