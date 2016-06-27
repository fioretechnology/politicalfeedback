define(['jquery','webfont','foundation','modernizr'], function($,WebFont,foundation) {

	$(document).ready(function() {

		WebFont.load({
			google: {
				families: [
					'Open+Sans:400,300,300italic,400italic,600,600italic,700,700italic,800,800italic:latin',
					'Roboto:400,100,100italic,300,300italic,400italic,500,500italic,700,700italic,900,900italic:latin',
					'Montserrat:400,700:latin',
					'Josefin Sans',
				]
			}
		});

		$(document).foundation();
		$( ".leftmenu-toggle" ).on( "click", function() {
			if ( $( "#leftmenu" ).hasClass( "hide" ) ) {
				$( "#leftmenu" ).removeClass( "hide" );
			} else {
				$( "#leftmenu" ).addClass( "hide" );
			}
		});

	});

});
