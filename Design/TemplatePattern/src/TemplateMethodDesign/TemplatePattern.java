package TemplateMethodDesign;

public class TemplatePattern {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 Game game = new Cricket();
	      game.play();
	      System.out.println();
	      game = new TableTennis();
	      game.play();	

	}

}
