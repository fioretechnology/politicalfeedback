define(["jquery",'datatables.net','datatables.responsive', function($) {

	$(document).ready(function() {

		$(document).ready(function() {
			$('#listaschede').DataTable( {
		        "dom": '<lf<t>ip>',
				responsive: true,
				stateSave: true,
				"aLengthMenu": [[10, 25, 50, -1], ["Mostra 10", "Mostra 25", "Mostra 50", "Mostra Tutti"]],
				"language": {
		            "sLengthMenu": "_MENU_",
		            "zeroRecords": "Nessun risultato trovato",
		            "sInfo": "Vista da _START_ a _END_ di _TOTAL_ elementi",
					search: "_INPUT_",
		        	searchPlaceholder: "Cerca",
		            "infoEmpty": "Nessun dato disponibile",
		            "infoFiltered": "(filtrato da _MAX_ dati totali)",
					"paginate": {
				      "previous": "Precedente",
					  "next": "Successiva"
				  }
		        }
		    } );
		} );


	});

});
