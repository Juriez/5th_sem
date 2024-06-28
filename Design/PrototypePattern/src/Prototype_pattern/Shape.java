package Prototype_pattern;

import java.util.Objects;

public abstract class Shape {
	public int x;
	public int y;
	public String color;
	
	public Shape() {
		
	}
	
	public Shape(Shape Terget) {
		if(Terget != null) {
			this.x = Terget.x;
			this.y = Terget.y;
			this.color = Terget.color;
		}
	}
	
	public abstract Shape clone();
	
	@Override
	public boolean equals(Object object2) {
		if(!(object2 instanceof Shape))
			return false;
		Shape shape = (Shape) object2;
		return shape.x == x && shape.y == y && Objects.equals(shape.color, color);
	}
	

}

