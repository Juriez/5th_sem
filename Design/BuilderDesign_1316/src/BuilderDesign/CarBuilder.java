package BuilderDesign;

public class CarBuilder implements Builder {
	    private Cartype type;
	    private int seats;
	    private Engine engine;
	    private Transmission transmission;
	    private Tripcomputer tripcomputer;
	    private GpsNavigator gpsnavigator;
	    
	    public void setCartype(Cartype type) {
	        this.type = type;
	    }


	@Override
	public void setSeats(int seats) {
		// TODO Auto-generated method stub
		this.seats = seats;
		
	}

	@Override
	public void setEngine(Engine engine) {
		// TODO Auto-generated method stub
		this.engine = engine;
	}

	@Override
	public void setTransmission(Transmission transmission) {
		// TODO Auto-generated method stub
		this.transmission = transmission;
	}

	@Override
	public void setTripcomputer(Tripcomputer tripcomputer) {
		// TODO Auto-generated method stub
		this.tripcomputer = tripcomputer;
	}

	@Override
	public void setGpsNavigator(GpsNavigator gpsnavigator) {
		// TODO Auto-generated method stub
		this.gpsnavigator = gpsnavigator;	
	}
	
	public Car getResult() {
        return new Car(type, seats, engine, transmission, tripcomputer, gpsnavigator);
    }
	

}
