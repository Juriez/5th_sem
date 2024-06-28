<?php 
	class Alert {
		const MESSAGE_INFO = "This is an alert INFO message";
		const MESSAGE_DANGER = "This is an alert DANGER message";
		public function show_alert_info() {
			echo self::MESSAGE_INFO;
		}
	}

	$alert = new Alert();
	$alert->show_alert_info();
	echo "<br>";
	echo Alert::MESSAGE_DANGER;

?>