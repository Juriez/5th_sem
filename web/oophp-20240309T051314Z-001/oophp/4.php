<?php 
	class Person {
		public $first_name;
		private $last_name;
		protected $address;
		
		function __construct($first_name, $last_name, $address) {
			$this->first_name = $first_name;
			$this->last_name = $last_name;
			$this->address = $address;
		}

		public function get_last_name() {
			return $this->last_name;
		}
	}
	
	$person1 = new Person("james", "bond", "UK");
	echo $person1->first_name;
	//echo "<br>".$person1->last_name;
	//echo "<br>".$person1->address;
	echo "<br>".$person1->get_last_name();

?>
