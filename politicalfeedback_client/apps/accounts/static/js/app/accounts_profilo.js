// This file is part of Politicalfeedback.

// Politicalfeedback is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.

// Politicalfeedback is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.

// You should have received a copy of the GNU General Public License
// along with Politicalfeedback.  If not, see <http://www.gnu.org/licenses/>.

define(["jquery",'datatables.net','datatables.responsive'], function($) {

	$(".sezione-opzioni").hide();
	$(".opzione").click(function(){
		var $a = $(this);
		$(".sezione-opzioni").hide();
		$(".salva").attr("form", "form_" + $a.data("id"));
		$("div #" + $a.data("id")).toggle();
	});

	$('#id_provincia').change(function(){
		$("#id_citta").load("/accounts/elencocitta/"+$('#id_provincia').val()+"/");
		$("#id_citta").removeClass('hide');
		$(".row_citta").removeClass('hide');
	});

	$(document).ready(function() {
		$('#datatable').DataTable( {
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
