package BridgePattern;

public interface Device {
	boolean isEnabled();
	void enable();
	void disable();
	int getVolume();
	void setVolume(int percent);
	int getChannel();
	void setCahnnel(int channel);
	void printstatus();

}
