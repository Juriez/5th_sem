<?php
	interface IShape {
		public function print_shape();
	}

	class Square implements IShape {
		public function print_shape() {
			echo "<h1>Square</h1>";
		}
	}

	class Circle implements IShape {
		public function print_shape() {
			echo "<h1>Circle</h1>";
		}
	}

	$square = new Square();
	$circle = new Circle();

	$square->print_shape();
	$circle->print_shape();

?>