package Prototype_pattern;

public class Circle extends Shape {
	public int radious;
	public Circle() {
		
	}
	public Circle(Circle Terget) {
		super(Terget);
		if(Terget != null)
		this.radious = Terget.radious;
	}

	@Override
	public Shape clone() {
		// TODO Auto-generated method stub
		return new Circle(this);
	}
	@Override
	public boolean equals(Object object2) {
		if(!(object2 instanceof Circle ) || !super.equals(object2))
		return false;
		Circle shape = (Circle) object2;
		return shape.radious == radious;
		
		
	}
	

}
