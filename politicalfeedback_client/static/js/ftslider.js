tempo = 5000

animazione_titolo = "animated fadeInUp"
animazione_desc = "animated slideInLeft"

$(".ftslider li").hide();
primo = $(".ftslider li:first-child");
ultimo = $(".ftslider li:last-child");
primo.show();
primo.find(".titolo").addClass(animazione_titolo);
primo.find(".desc").addClass(animazione_desc);

corrente = primo;

intervallo = setInterval(function () {

		if (corrente.is(':last-child')){
        	prossimo = primo;
        } else {
        	prossimo = corrente.next();
        }
		
        corrente.hide();
        prossimo.fadeIn();

        prossimo.find(".titolo").addClass(animazione_titolo);
		corrente.find(".titolo").removeClass(animazione_titolo);
		prossimo.find(".desc").addClass(animazione_desc);
		corrente.find(".desc").removeClass(animazione_desc);

   		corrente = prossimo;
},tempo);



$(".freccia-dx").on('click touchstart', function(){
	if (corrente.is(':last-child')){
        	prossimo = primo;
        } else {
        	prossimo = corrente.next();
        }
		
        corrente.hide();
        prossimo.fadeIn();

        prossimo.find(".titolo").addClass(animazione_titolo);
		corrente.find(".titolo").removeClass(animazione_titolo);
		prossimo.find(".desc").addClass(animazione_desc);
		corrente.find(".desc").removeClass(animazione_desc);

   		corrente = prossimo;
   		clearInterval(intervallo);
})

$(".freccia-sx").on('click touchstart', function(){
	if (corrente.is(':first-child')){
        	prossimo = ultimo;
        } else {
        	prossimo = corrente.prev();
        }
		
        corrente.hide();
        prossimo.fadeIn();

        prossimo.find(".titolo").addClass(animazione_titolo);
		corrente.find(".titolo").removeClass(animazione_titolo);
		prossimo.find(".desc").addClass(animazione_desc);
		corrente.find(".desc").removeClass(animazione_desc);

   		corrente = prossimo;
   		clearInterval(intervallo);
})