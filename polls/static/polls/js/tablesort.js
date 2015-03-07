function comparer(index) {
    return function(a, b) {
        var valA = getCellValue(a, index), valB = getCellValue(b, index);
        //some columns have 1st, 2nd, 3rd, etc
        valA = valA.trim().replace(/(\d+)(nd|rd|st|th)/, '$1');
        valB = valB.trim().replace(/(\d+)(nd|rd|st|th)/, '$1');
            return $.isNumeric(valA) && $.isNumeric(valB) ? valA - valB : valA.localeCompare(valB)
    }
}

function getCellValue(row, index){
    return $(row).children('td').eq(index).html() 
}

//thank you stackoverflow
$(document).ready(function(){
    $('th').click(function(){
        var table = $(this).parents('table').eq(0);
        var rows = table.find('tr:gt(0)').toArray().sort(comparer($(this).index()));
        this.asc = !this.asc;
        if (!this.asc){
            rows = rows.reverse();
        }
        for (var i = 0; i < rows.length; i++){
            table.append(rows[i]);
        }
    });
});
