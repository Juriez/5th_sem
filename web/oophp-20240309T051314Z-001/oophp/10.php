<?php 
	abstract class Fruit {
		public abstract function info();
		public abstract function print_taste($taste);
	}

	class Apple extends Fruit {
		public function info() {
			echo "<h1>It's an apple</h1>";
		}
		public function print_taste($taste) {
			echo "<h1>The apple tastes {$taste}</h1>";
		}
	}

	class Orange extends Fruit {
		public function info() {
			echo "<h1>It's an orange</h1>";
		}
		public function print_taste($taste, $price=10) {
			echo "<h1>The orange tastes {$taste} with price BDT {$price} per piece.</h1>";
		}
	}

	$apple = new Apple();
	$apple->info();

	$orange = new Orange();
	$orange->info();

	$apple->print_taste("sweet");
	$orange->print_taste("sweet");
	$orange->print_taste("sweet", 100);
?>