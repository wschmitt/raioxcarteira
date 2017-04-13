
var formstr = '<form action="/your-name/" method="post">{% csrf_token %}{{ form }}<input type="submit" value="Submit" /></form>'

function parseText(statement_html) {
	//var el = document.createElement( 'html' );
	//el.innerHTML = text;//"<html><head><title>titleTest</title></head><body><a href='test0'>test01</a><a href='test1'>test02</a><a href='test2'>test03</a></body></html>";
	//console.log("oi, printa caralho");
	//test = $(".add-row");
	
	//console.log($.fn.formset.options);
	//console.log("testing" + test);
	var field_indexes = ['date', 'description', 'value']
	el = remove(statement_html, ["Dep. Origem", "Documento", "Saldo", "\xa0"])
	el = validate_col(el, "Valor", function(value) {
		//console.log(e);
		return parseFloat(value).toFixed(2);
	} );
	//el = addRows(el, "Teste");
	//$('div[id="estatement_container"]').append(el);
	//document.getElementById('estatement_container').innerHTML = el;
	$('tbody  > tr', el).each(function(i) {
		$("#add-row").trigger('click');
		var $current_form = $('#myForm tbody tr.dynamic-form:last');
		//console.log($current_form);
		var $tds = $(this).find('td');
		
		$tds.each(function(j) {
			//console.log($('#id_form-2-date', $current_form))
			//console.log($current_form.html());
			//console.log($('#id_form-'+ (i+1) +'-date', $current_form));
			//if (j.toString() in field_indexes) {
			//console.log($('#id_form-'+ (i+1) +'-'+field_indexes[j], $current_form))
			$('#id_form-'+ (i+1) +'-'+field_indexes[j], $current_form).val($(this).text())
			//}
			//console.log($(this).text());

		})
		
	});

	$("#new-entries-header").css('visibility', 'visible');

	//td = el.getElementsByTagName( 'td' ); // Live NodeList of your anchor elements
	//var columns = el.getElementsByTagName('tbody')[0].getElementsByTagName('td');
    //    for(columnIt = 0; columnIt < columns.length; columnIt++) {
    //        var column = columns[columnIt];
    //        console.log(column.innerHTML);
    //    }
	//console.log(td);

}

function validate_col(el, header, f) {
	var target = $('table', el).find('th:contains("' + header +'")');
	var index = (target).index();
	$cell = $('table tr', el).find('td:eq(' + index + ')');
	$cell.each( function() {
		$(this).text(f($(this).text()));
	});
	return el;
}

function remove(statement_html, header_list) {
	var el = $( '<div></div>' );
	el.html(statement_html);

	header_list.forEach( 
		function (str, i) {
		// Get target th with the name you want to remove.
		var target = $('table', el).find('th:contains("' + str +'")');

		// Find its index among other ths 
		var index = (target).index();
		//console.log("Removing column with index " + index + "(" + str + ")");
		// For each tr, remove all th and td that match the index.
		$('table tr', el).find('th:eq(' + index + '),td:eq(' + index + ')' ).remove();

	});
	return el;
}

function addRows(el, header) {
	el.ready(function(){
		$('table', el).find('th').eq(1).after('<th style="width:10%;">Category</th>');
	    $('table', el).find('tr').each(function(){
	    	//console.log(this.text);
	        $(this).find('td').eq(1).after('<td style="width:10%;"> '+ formstr +'</td>');
	    });
	});
	return el;
}