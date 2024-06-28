package BridgePattern;

public class BasicRemote implements Remote {
	protected Device device;
	public BasicRemote() {
		
	}
	public BasicRemote(Device device) {
		this.device = device;
	}

	@Override
	public void power() {
		// TODO Auto-generated method stub
		System.err.println("Remote : Power toggle ");
		if(device.isEnabled())
			device.disable();
		else
			device.enable();
		
	}

	@Override
	public void volumeDown() {
		// TODO Auto-generated method stub
		System.err.println("Volume Down :");
		device.setVolume(device.getVolume()-5);
		
	}

	@Override
	public void volumeUp() {
		// TODO Auto-generated method stub
		System.err.println("Volume UP :");
		device.setVolume(device.getVolume()+5);
		
	}

	@Override
	public void channelDown() {
		// TODO Auto-generated method stub
		System.err.println("Channel Down :");
		device.setCahnnel(device.getChannel()-1);
		
		
	}

	@Override
	public void channelUp() {
		// TODO Auto-generated method stub
		System.err.println("Channel Up :");
		device.setCahnnel(device.getChannel()+1);
		
	}

}
