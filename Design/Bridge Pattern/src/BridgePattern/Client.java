package BridgePattern;

public class Client {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		testDevice(new Laptop());
		testDevice(new Radio());

	}

	private static void testDevice(Device device) {
		// TODO Auto-generated method stub
		System.err.println("Let's test Basic Remote :");
		BasicRemote bremote = new BasicRemote(device);
		bremote.power();
		device.printstatus();
		
		System.err.println("Let's test Modern Remote :");
		ModernRemote mremote = new ModernRemote(device);
		mremote.power();
		mremote.mute();
		device.printstatus();
	}

}
