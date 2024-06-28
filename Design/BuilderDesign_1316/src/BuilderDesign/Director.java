package BuilderDesign;

public class Director {
	public void constructSportsCar(Builder builder) {
        builder.setCartype(Cartype.SPORTS_CAR);
        builder.setSeats(2);
        builder.setEngine(new Engine(3.0, 0));
        builder.setTransmission(Transmission.SEMI_AUTOMATIC);
        builder.setTripcomputer(new Tripcomputer());
        builder.setGpsNavigator(new GpsNavigator());
    }

    public void constructCityCar(Builder builder) {
        builder.setCartype(Cartype.CITY_CAR);
        builder.setSeats(2);
        builder.setEngine(new Engine(1.2, 0));
        builder.setTransmission(Transmission.AUTOMATIC);
        builder.setTripcomputer(new Tripcomputer());
        builder.setGpsNavigator(new GpsNavigator());
    }

    public void constructSUV(Builder builder) {
        builder.setCartype(Cartype.SUV);
        builder.setSeats(4);
        builder.setEngine(new Engine(2.5, 0));
        builder.setTransmission(Transmission.MANUAL);
        builder.setGpsNavigator(new GpsNavigator());
    }

}
