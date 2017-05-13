
function build_expense_chart(expenses_chart_data, receipts_chart_data) {
    //console.log(chart_data)
    var categories = [];
    var expenses_values = [];
    var receipts_values = [];

    $.each(expenses_chart_data, function(k, v) {
        categories.push(k);
        expenses_values.push(v);
    });

    $.each(receipts_chart_data, function(k, v) {
        receipts_values.push(v);
    });
    //console.log(receipts_values);

    //console.log(categories);
    //console.log(values);
    //console.log(expenses_values);
    //console.log(receipts_values);
    $(function () { 
        var myChart = Highcharts.chart('chart-1', {
            chart: {
                renderTo: 'container',
                type: 'column',
            },
            title: {
                text: 'Despesas por Categoria'
            },
            xAxis: {
                categories:categories
            },
            yAxis: {
                title: {
                    text: 'R$'
                }
            },
            series: [{
                name: 'Despesas',
                data: expenses_values, //[29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4],
                //pointStart: Date.UTC(2010, 0, 1),
                //pointInterval: 3600 * 1000 // one hour
            },
            {
                name: 'Receitas',
                data: receipts_values,
            }],
            
                
            
        });
    });
}