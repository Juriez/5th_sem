package BridgePattern;

public class ModernRemote extends BasicRemote {
	//protected Device device;
	
	public ModernRemote(Device device) {
		super.device = device;
	}
	public void mute() {
		System.err.println("Mute is the latest operation that could not found in Basic Remote.");
		System.err.println("Remote Mute : ");
		device.setVolume(0);
	}
	
	

}
