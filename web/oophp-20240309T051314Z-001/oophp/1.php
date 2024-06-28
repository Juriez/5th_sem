<?php 
	class Person {
		public $first_name;
		public $last_name;
		public $address;
		
		function get_first_name() {
			return $this->first_name;
		}
		
		function set_first_name($first_name) {
			$this->first_name = $first_name;
		}
	}
	
	$person1 = new Person();
	$person1->set_first_name('James'); 
	echo $person1->get_first_name();
	echo "<br>";
	$person1->last_name = 'Bond';
	echo $person1->last_name;

?>
