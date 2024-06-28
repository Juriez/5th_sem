package BuilderDesign;

public interface Builder {
	void setCartype(Cartype type);
    void setSeats(int seats);
    void setEngine(Engine engine);
    void setTransmission(Transmission transmission);
    void setTripcomputer(Tripcomputer tripComputer);
    void setGpsNavigator(GpsNavigator gpsNavigator);

}
