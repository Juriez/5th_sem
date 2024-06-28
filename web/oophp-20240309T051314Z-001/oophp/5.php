<?php
	
	class Fruit {
		public $name;
		public $color;

		public function __construct($name, $color) {
			$this->name = $name;
			$this->color = $color;
		}

		protected function get_info() {
			return $this->name. " ".$this->color;
		}
	}

	class Apple extends Fruit {
		public $weight=50;
		public function show_details() {
			echo "<h1>{$this->get_info()} {$this->weight} </h1>";
		}

	}

	$apple1 = new Apple("apple", "red");
	$apple1->show_details();

?>