package BridgePattern;

public class Radio implements Device {
	
	private boolean on = false;
	private int volume = 30;
	private int channel = 1;

	@Override
	public void enable() {
		// TODO Auto-generated method stub
		
		on = true;
	}

	@Override
	public void disable() {
		// TODO Auto-generated method stub
		on = false;
	}

	@Override
	public int getVolume() {
		// TODO Auto-generated method stub
		return volume;
	}

	@Override
	public void setVolume(int percent) {
		// TODO Auto-generated method stub
		if(percent>100)
			volume = 100;
		else if(percent<0)
			volume = 0;
		else
			volume = percent;
		
	}

	@Override
	public int getChannel() {
		// TODO Auto-generated method stub
		return channel;
	}

	@Override
	public void setCahnnel(int channel) {
		// TODO Auto-generated method stub
		this.channel = channel;
		
	}

	@Override
	public void printstatus() {
		// TODO Auto-generated method stub
		System.err.println("It's radio.");
		System.err.println("It is " + (on? "enabled" : "disabled"));
		System.err.println("Current volume : " + volume + "%");
		System.err.println("Current Channel : "+ channel);
		System.err.println("\n \n");
		
	}

	@Override
	public boolean isEnabled() {
		// TODO Auto-generated method stub
		return on;
	}

}
