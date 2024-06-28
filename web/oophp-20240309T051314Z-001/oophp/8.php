<?php 
	class Fruit {
		public final function show_info() {
			echo "<h1> I am from the Fruit class </h1>";
		}
	}

	class Apple extends Fruit {
		public function show_info() {
			echo "<h1>I am from the Apple class</h1>";
		}
	}

	$apple = new Apple();
	$apple->show_info();
?>