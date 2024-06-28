package Prototype_pattern;

import java.util.ArrayList;
import java.util.List;

public class Clone {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<Shape> shape = new ArrayList<>();
		List<Shape> scopy = new ArrayList<>();
		
		Circle circle = new Circle();
		circle.x = 100;
		circle.y = 150;
		circle.color = "red";
		circle.radious = 5;
		shape.add(circle);
		
		Circle anotherCircle = (Circle)circle.clone();
		shape.add(anotherCircle);
		
		Rectangle rectangle = new Rectangle();
		rectangle.width = 200;
		rectangle.hight = 100;
		rectangle.color = "blue";
		shape.add(rectangle);
		
		cloneAndCompare(shape,scopy);

	}

	private static void cloneAndCompare(List<Shape> shape, List<Shape> scopy) {
		// TODO Auto-generated method stub
		for(Shape shapes : shape) {
			scopy.add(shapes.clone());
		}
		for(int i=0;i<shape.size();i++) {
			if(shape.get(i) != scopy.get(i)) {
				System.err.println(i + ": Shapes are different objects!");
				
				if(shape.get(i).equals(scopy.get(i)))
					System.err.println(i + ": And they are identicle.");
				else
					System.err.println(i+ ": But they are not identicle");
			}
			else
				System.err.println(i + ": Shape object are the same");
			
		}
		
	}

}
