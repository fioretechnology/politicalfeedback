$( document ).ready(function() {
    var resetpassword = $("#resetpassword");
	var persoutente = $("#persoutente");
	var loginuser = $("#loginuser");

	resetpassword.hide();

	$("#dim_pass").click(function() {
		loginuser.hide();
		resetpassword.show();
	});
	$("#mailtologin").click(function() {
		resetpassword.hide();
		persoutente.hide();
		loginuser.show();
	});
	$("#passtologin").click(function() {
		resetpassword.hide();
		persoutente.hide();
		loginuser.show();
	});

});
