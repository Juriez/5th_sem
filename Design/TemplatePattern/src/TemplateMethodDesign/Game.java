package TemplateMethodDesign;

public abstract class Game {
	abstract void initialize();
	abstract void startplay();
	abstract void endplay();
	public final void play() {
		initialize();
		
		startplay();
		
		endplay();
		
	}

}
