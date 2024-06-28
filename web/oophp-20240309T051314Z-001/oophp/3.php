<?php 
	class Person {
		public $first_name;
		public $last_name;
		public $address;
		
		function __construct($first_name, $last_name, $address) {
			$this->first_name = $first_name;
			$this->last_name = $last_name;
			$this->address = $address;
		}
		
		function __destruct() {
			echo "<br>The object of the person class has been destructed";
		}
	}
	
	$person1 = new Person("james", "bond", "UK");
	echo $person1->first_name . " " . $person1->last_name . " " . $person1->address;

?>
