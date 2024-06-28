package Prototype_pattern;

public class Rectangle extends Shape {
	public int width;
	public int hight;
	public Rectangle() {
		
	}
	public Rectangle(Rectangle Terget) {
		super(Terget);
		if(Terget != null)
			{
			this.width = Terget.width;
			this.hight = Terget.hight;
			}		
		    
	}

	@Override
	public Shape clone() {
		// TODO Auto-generated method stub
		return new Rectangle(this);
	}
	@Override
	public boolean equals(Object object2) {
		if(!(object2 instanceof Rectangle) || !super.equals(object2))
		return false;
		Rectangle shape = (Rectangle) object2;
		return shape.width == width && shape.hight == hight;
		
		
	}

}
