
var formstr = '<form action="/your-name/" method="post">{% csrf_token %}{{ form }}<input type="submit" value="Submit" /></form>'

function showExpenseBulkArea() {
	console.log(get_total_forms());
	console.log("show area");
	$("#build-expenses").toggle();//css('display', 'visible');
}

function get_total_forms() {
	return parseInt($('#id_form-TOTAL_FORMS').val());
}

field_indexes = ['date', 'description', 'value']

//* Parse the text obtained by copying the inner html from BB site *//
function parseBBHTML(statement_html) {
	el = text_to_html_element(statement_html);
	remove_columns_from_table(el, ["Dep. Origem", "Documento", "Saldo", "\xa0"])
	map_table_col(el, "Valor", function(value) {
		return parseFloat(value).toFixed(2);
	});
	
	data = {}
	$('tbody  > tr', el).each(function(i) {
		var $tds = $(this).find('td');
		$tds.each(function(j) {
			//$('#id_form-'+ (i+1) +'-'+field_indexes[j], $current_form_row).val($(this).text())
			data['#id_form-'+ (get_total_forms()+i) +'-'+field_indexes[j]] = $(this).text();
		})
	});
	console.log(data);
	fill_form(data);
}

//* Parse the text obtained by copying the text from BB site *//
function parseBBText(extrato_text) {
	data = {}
	// a new entry always start with a date dd/mm/yyyy
	lines = extrato_text.split('\n');
	fields = []
	for(var i=0; i<lines.length; i++){
	    if (isDate(lines[i])) {
	    	entry = {date:'', description:'', value:''}
	    	fields.push(entry);
	    	entry.date = lines[i];
	    	continue;
	    }

	    if (!(isCredit(lines[i]) || isDebit(lines[i]))) {
	    	entry.description += lines[i]
	    	continue;
	    }

	    if (isCredit(lines[i])) {
	    	if (entry.value.length <= 0) {
	    		entry.value = convert_money_to_float(lines[i]);
	    	}
	    	continue;
	    }
	    if (isDebit(lines[i])) {
	    	entry.value = convert_money_to_float(lines[i]);
	    }
	}
	for (var i=0; i<fields.length; i++) {
		entry = fields[i];
		for (var j=0; j<field_indexes.length; j++)
			data['#id_form-'+ (get_total_forms()+i) +'-'+field_indexes[j]] = entry[field_indexes[j]];
	}
	console.log(data);
	fill_form(data);
}

/* 1.280,05 --> 1280.05 */
function convert_money_to_float(value) {
	value = value.replace(/\./g, "").replace(/,/g,".");
	return parseFloat(value).toFixed(2);
}

function isDate(date) {
	var dateReg = /^\d{2}([./-])\d{2}\1\d{4}$/;
    return (date.length === 10 && dateReg.test(date));
}

function isCredit(value) {
	var creditReg = /^\d+[.,\d]* C$/;
	return creditReg.test(value);
}

function isDebit(value) {
	var debitReg = /^\d+[.,\d]* D$/;
	return debitReg.test(value);
}

//* append row in form and return the row *//
function append_row_in_form(qty) {
	for (i=0; i<qty; i++) {
		$("#add-row").trigger('click');
		var $current_form = $('#myForm tbody tr.dynamic-form:last');
	}
	return $current_form;
}

//* fill form based on json data *//
function fill_form(json_values) {
	var $current_form_row = append_row_in_form(Object.keys(json_values).length/3);
	for (var key in json_values) {
		if (json_values.hasOwnProperty(key)) {
			$trs = $('#myForm tbody tr.dynamic-form');
			$(key, $trs).val(json_values[key]);
		}
	}
}

//* Apply the function f to each element of column = header of the table *//
function map_table_col(el, header, f) {
	var target = $('table', el).find('th:contains("' + header +'")');
	var index = (target).index();
	$cell = $('table tr', el).find('td:eq(' + index + ')');
	$cell.each( function() {
		$(this).text(f($(this).text()));
	});
}

function text_to_html_element(text_html) {
	var el = $( '<div></div>' );
	el.html(text_html);
	return el;
}

//* Remove columns from a table given a header list *//
function remove_columns_from_table(el, header_list) {
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