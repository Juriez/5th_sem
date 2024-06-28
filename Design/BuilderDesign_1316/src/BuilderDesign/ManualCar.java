package BuilderDesign;

public class ManualCar {
	private final Cartype cartype;
	private final int seats;
	private final Engine engine;
	private final Transmission transmission;
	private final Tripcomputer tripcomputer;
	private final GpsNavigator gpsnavigator;
	//private double fuel = 0;
	
	public ManualCar(Cartype cartype, int seats, Engine engine, Transmission transmission, Tripcomputer tripcomputer,GpsNavigator gpsnavigator) {
		this.cartype = cartype;
		this.seats = seats;
		this.engine = engine;
		this.transmission = transmission;
		
		this.tripcomputer=tripcomputer;
		
		this.gpsnavigator= gpsnavigator;
	}
		
		public String print() {
			String info = "";
			info += "Type of car: " + cartype + "\n";
	        info += "Count of seats: " + seats + "\n";
	        info += "Engine: volume - " + engine.getVolume() + "; mileage - " + engine.getMileage() + "\n";
	        info += "Transmission: " + transmission + "\n";
	        if (this.tripcomputer != null) {
	            info += "Trip Computer: Functional" + "\n";
	        } else {
	            info += "Trip Computer: N/A" + "\n";
	        }
	        if (this.gpsnavigator != null) {
	            info += "GPS Navigator: Functional" + "\n";
	        } else {
	            info += "GPS Navigator: N/A" + "\n";
	        }
	        return info;
			
		}

}
