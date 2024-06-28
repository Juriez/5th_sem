package BuilderDesign;

public class Car {
	private final Cartype cartype;
	private final int seats;
	private final Engine engine;
	private final Transmission transmission;
	private final Tripcomputer tripcomputer;
	private final GpsNavigator gpsnavigator;
	private double fuel = 0;
	
	public Car(Cartype cartype, int seats, Engine engine, Transmission transmission, Tripcomputer tripcomputer,GpsNavigator gpsnavigator) {
		this.cartype = cartype;
		this.seats = seats;
		this.engine = engine;
		this.transmission = transmission;
		this.tripcomputer = new Tripcomputer();
		if(this.tripcomputer != null) {
		this.tripcomputer.setCar(this);
		}
		this.gpsnavigator = gpsnavigator;
	}
	
	public Cartype getCartype() {
		return cartype;
	}
	
	public double getFuel() {
		return fuel;
	}
	
	public void setFuel() {
		this.fuel=fuel;
	}
	
	public int getSeats() {
		return seats;
	}
	public Engine getEngine() {
		return engine;
	}
	
	public Transmission getTransmission() {
		return transmission;
	}
	public Tripcomputer getTripcomputer() {
		return tripcomputer;
	}
	
	public GpsNavigator getGpsNavigator() {
		return gpsnavigator;
	}

}
