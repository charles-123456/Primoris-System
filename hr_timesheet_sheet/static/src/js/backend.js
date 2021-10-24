odoo.define("hr_timesheet_sheet", function(require) {
    "use strict";

    var X2Many2dMatrixRenderer = require("web_widget_x2many_2d_matrix.X2Many2dMatrixRenderer");

    X2Many2dMatrixRenderer.include({
        /**
         * @override
         */
        _renderBodyCell: function() {
            var $cell = this._super.apply(this, arguments);
            if (this.getParent().model === "hr_timesheet.sheet") {
                var $span = $cell.find("span");
//                console.log('span values set as js',$span)
//                console.log('onjects entered',$span.text().rows)
//                 console.log('class matrix data!!!',this.matrix_data.rows[0].data[0].data.value_x)
//                 for (let i=0;i< this.matrix_data.rows.length;i++){
//                  console.log('first for exe')
//                    for(let j=0;j< this.matrix_data.rows[i].data.length;j++){
//                    console.log('second for exe')
//                        if ((this.matrix_data.rows[i].data[j].data.value_x.includes("Sat") || this.matrix_data.rows[i].data[j].data.value_x.includes("Sun"))){
//                            console.log('if exe')
//                            this.matrix_data.rows[i].data[j].data.unit_amount = parseInt("00.00");
//                        }else{
//                            console.log('else exe')
//                            console.log('data i and j',this.matrix_data.rows[i].data[j])
//                            console.log('data last',this.matrix_data.rows[i].data[j].data)
//                            this.matrix_data.rows[i].data[j].data.unit_amount = parseInt("09.00");
//                            console.log(this.matrix_data.rows[i].data[j].unit_amount = parseInt("09.00"))
//                        }
//
//                    }
//                 }
                if ($span.text() === "00:00") {
                    console.log('Executed text muted')
                    console.log('Executed class',$span.addClass)

                    $span.addClass("text-muted");
                } else {
                    console.log('else part execute',$span.wrap($("<strong/>")))
                    $span.wrap($("<strong />"));
                }
            }
            return $cell;
        },
    });
});
