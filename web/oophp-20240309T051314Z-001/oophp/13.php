<?php 
	class Message {
		public static $alert_message;
		public static function show_alert_message() {
			echo self::$alert_message;
		}
	}

	Message::$alert_message = "Hello World";
	Message::show_alert_message();
?>