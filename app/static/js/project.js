$(document).ready(function() {
	// Highlight in the navigation bar the active menu item.
	var path = window.location['pathname'];
	if (path == '/') {
		$('ul.navbar-nav li.home').addClass('active');
	} else if (path.substring(0, 23) == '/flor50/liste-bouquets/') {
		$('ul.navbar-nav li.galleries').addClass('active');
	} else if (path.substring(0, 25) == '/flor50/liste-evenements/') {
		$('ul.navbar-nav li.evenements').addClass('active');
	}
})
