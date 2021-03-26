var $table = $('#table');

var filename = "degree_classification";

// change loading template
function loadingTemplate(message) {
    return '<i class="fa fa-spinner fa-spin fa-fw fa-2x"></i>'
}

// bootstrap table attributes
$(function () {
    $('#table').bootstrapTable({
        exportTypes: ['json', 'xml', 'csv', 'txt', 'excel', 'pdf'],
        sortReset: true,
        sortStable: true,
        theadClasses: "thead-light",
        exportDataType: "all",
        visibleSearch: true,
        minimumCountColumns: 2,
        showColumnsSearch: true,
        exportOptions: {
            fileName: filename
        },
        columns: [
            {
                field: "type",
                title: "Type",
                sortable: true,
                visible: true,
                filterControl: "select"
            },
            {
                field: "anon",
                title: "Anonymized student",
                sortable: true,
                visible: false,
                filterControl: "input"
            },
            {
                field: "mcId",
                title: "StudentID",
                sortable: true,
                visible: false,
                filterControl: "input"
            },
            {
                field: "id",
                title: "Matric No.",
                sortable: true,
                width: 100,
                filterControl: "input"
            },
            {
                field: "grad",
                title: "Graduation Year",
                sortable: true,
                filterControl: "select"
            },
            {
                field: "name",
                title: "Name",
                sortable: true,
                visible: false,
                filterControl: "input"
            },
            {
                field: "first",
                title: "First Name",
                sortable: true,
                filterControl: "input"
            },
            {
                field: "last",
                title: "Last Name",
                sortable: true,
                filterControl: "input"
            },
            {
                field: "plan",
                title: "Acad Plan",
                sortable: true,
                visible: false,
                filterControl: "select"
            },
            {
                field: "gpa4",
                title: "GPA (4 d.p.)",
                sortable: true,
                visible: false,
                filterControl: "input"
            },
            {
                field: "gpa3",
                title: "GPA (3 d.p.)",
                sortable: true,
                visible: false,
                filterControl: "input"
            },
            {
                field: "gpa2",
                title: "GPA (2 d.p.)",
                sortable: true,
                visible: false,
                filterControl: "input"
            },
            {
                field: "gpa1",
                title: "GPA (1 d.p.)",
                sortable: true,
                filterControl: "input"
            },
            {
                field: "gpa",
                title: "GPA",
                sortable: true,
                visible: false,
                filterControl: "select"
            },
            {
                field: "oAward",
                title: "Original Award",
                sortable: true,
                filterControl: "select"
            },
            {
                field: "award",
                title: "Award",
                sortable: true,
                editable: {
                    disabled: !edit,
                    type: 'select',
                    mode: 'inline',
                    source: [
                        {
                            text: "Honors Classification",
                            children: [
                                {value: "01", text: "01"},
                                {value: "0U", text: "0U"},
                                {value: "0L", text: "0L"},
                                {value: "33", text: "33"},
                                {value: "Fail", text: "Fail"}
                            ]
                        },
                        {
                            text: "Other Classifications",
                            children: [
                                {value: "GC", text: "GC"},
                                {value: "DD-UD", text: "DD-UD"},
                                {value: "DD-UM", text: "DD-UM"},
                                {value: "DD-UQ", text: "DD-UQ"},
                                {value: "TBC", text: "TBC"}
                            ]
                        }
                    ]
                },
                filterControl: "select"
            },
            {
                field: "mcAward",
                title: "Degree Honors",
                sortable: true,
                visible: false,
                filterControl: "select"
            },
            {
                field: "notes",
                title: "Notes",
                sortable: true,
                editable: {
                    disabled: !edit,
                    mode: "inline",
                    inputclass: "text-area",
                    emptytext: "Add Note"
                },
                filterControl: "input"
            }
        ],
        // subtable
        onExpandRow: function (index, row, $detail) {
            var $el = $detail.html('<table></table>').find('table')
            var columns = [
                {
                    field: "gradeId",
                    title: "Matric No. (Grades)",
                    visible: false
                },
                {
                    field: "code",
                    title: "Course Code",
                    sortable: true
                },
                {
                    field: "oAlpha",
                    title: "Original Grade",
                    sortable: true,
                },
                {
                    field: "alpha",
                    title: "Alphanumeric Grade",
                    sortable: true,
                    editable: {
                        disabled: !edit,
                        type: 'select',
                        mode: 'inline',
                        source: [
                            {
                                text: "A",
                                children: [
                                    {value: "A1", text: "A1"},
                                    {value: "A2", text: "A2"},
                                    {value: "A3", text: "A3"},
                                    {value: "A4", text: "A4"},
                                    {value: "A5", text: "A5"},
                                ]
                            },
                            {
                                text: "B",
                                children: [
                                    {value: "B1", text: "B1"},
                                    {value: "B2", text: "B2"},
                                    {value: "B3", text: "B3"}
                                ]
                            },
                            {
                                text: "C",
                                children: [
                                    {value: "C1", text: "C1"},
                                    {value: "C2", text: "C2"},
                                    {value: "C3", text: "C3"}
                                ]
                            },
                            {
                                text: "D",
                                children: [
                                    {value: "D1", text: "D1"},
                                    {value: "D2", text: "D2"},
                                    {value: "D3", text: "D3"}
                                ]
                            },
                            {
                                text: "E",
                                children: [
                                    {value: "E1", text: "E1"},
                                    {value: "E2", text: "E2"},
                                    {value: "E3", text: "E3"}
                                ]
                            },
                            {
                                text: "F",
                                children: [
                                    {value: "F1", text: "F1"},
                                    {value: "F2", text: "F2"},
                                    {value: "F3", text: "F3"}
                                ]
                            },
                            {
                                text: "G",
                                children: [
                                    {value: "G1", text: "G1"},
                                    {value: "G2", text: "G2"}
                                ]
                            },
                            {
                                text: "H",
                                children: [
                                    {value: "H", text: "H"},
                                ]
                            },
                            {
                                text: "Special Codes",
                                children: [
                                    {value: "CW", text: "CW"},
                                    {value: "CR", text: "CR"},
                                    {value: "MV", text: "MV"}
                                ]
                            }
                        ]
                    }
                },
                {
                    field: "ttpt",
                    title: "22pt. (4 d.p.)",
                    sortable: true
                },
                {
                field: "subNotes",
                title: "Notes",
                sortable: true,
                searchable: false,
                editable: {
                    disabled: !edit,
                    mode: "inline",
                    inputclass: "text-area",
                    emptytext: "Add Note"
                }
            }
            ]
            $el.bootstrapTable({
                rowStyle: 'rowStyle',
                columns: columns,
                data: row.sub,
            })
        }
    });
});

// to highlight rows in the future
function rowStyle(row, index) {
    if (row.type === "Incomplete Course Assessment" ||
        row.type === "Course Grade Adjusted") {
        return {
            classes: 'table-danger'
        }
    }
    if (row.type === "Discretionary") {
        return {
            classes: 'table-warning'
        }
    }
    if (row.type === "Degree Overridden") {
        return {
            classes: 'table-success'
        }
    }
    if (row.type === "Special Code") {
        return {
            classes: 'table-primary'
        }
    }
    if (row.alpha === "CW" ||
        row.alpha === "MV" ||
        row.alpha === "CR") {
        return {
            classes: 'table-danger'
        }
    }
    if (row.alpha === "-") {
        return {
            classes: 'table-danger'
        }
    }
    if (row.alpha != row.oAlpha){
        return {
            classes: 'table-success'
        }
    }

    return 0
}

$('#table').on('editable-shown.bs.table', function() {
    $('#table').bootstrapTable('resetView')
});

$('#table').on('editable-hidden.bs.table', function() {
    $('#table').bootstrapTable('resetView')
});

var isMyCampus = false

$(function() {
    $('#myCampusLayout').click(function() {

        var iteration=$(this).data('iteration')||1

        switch (iteration) {
            case 1:
                isMyCampus = true;
                $table.bootstrapTable('hideColumn', 'anon');
                $table.bootstrapTable('showColumn', 'mcId');
                $table.bootstrapTable('showColumn', 'name');
                $table.bootstrapTable('showColumn', 'plan');
                $table.bootstrapTable('showColumn', 'mcAward');
                $table.bootstrapTable('hideColumn', 'type');
                $table.bootstrapTable('hideColumn', 'id');
                $table.bootstrapTable('hideColumn', 'grad');
                $table.bootstrapTable('hideColumn', 'first');
                $table.bootstrapTable('hideColumn', 'last');
                $table.bootstrapTable('hideColumn', 'gpa4');
                $table.bootstrapTable('hideColumn', 'gpa3');
                $table.bootstrapTable('hideColumn', 'gpa2');
                $table.bootstrapTable('hideColumn', 'gpa1');
                $table.bootstrapTable('hideColumn', 'oAward');
                $table.bootstrapTable('hideColumn', 'award');
                $table.bootstrapTable('hideColumn', 'notes');
                break;

            case 2:
                isMyCampus = false;
                $table.bootstrapTable('hideColumn', 'anon');
                $table.bootstrapTable('hideColumn', 'mcId');
                $table.bootstrapTable('hideColumn', 'name');
                $table.bootstrapTable('hideColumn', 'plan');
                $table.bootstrapTable('hideColumn', 'mcAward');
                $table.bootstrapTable('showColumn', 'type');
                $table.bootstrapTable('showColumn', 'id');
                $table.bootstrapTable('showColumn', 'grad');
                $table.bootstrapTable('showColumn', 'first');
                $table.bootstrapTable('showColumn', 'last');
                $table.bootstrapTable('hideColumn', 'gpa4');
                $table.bootstrapTable('hideColumn', 'gpa3');
                $table.bootstrapTable('hideColumn', 'gpa2');
                $table.bootstrapTable('showColumn', 'gpa1');
                $table.bootstrapTable('showColumn', 'oAward');
                $table.bootstrapTable('showColumn', 'award');
                $table.bootstrapTable('showColumn', 'notes');
                break;
        }
        iteration++;
        if (iteration>2) iteration = 1;
        $(this).data('iteration',iteration);
    });
    $('#anonymize').click(function() {
        var iter=$(this).data('iter')||1;
        switch (iter) {
            case 1:
                if (isMyCampus) {
                    $table.bootstrapTable('showColumn', 'anon');
                    $table.bootstrapTable('hideColumn', 'mcId');
                    $table.bootstrapTable('hideColumn', 'name');
                    break;
                }
                $table.bootstrapTable('showColumn', 'anon');
                $table.bootstrapTable('hideColumn', 'id');
                $table.bootstrapTable('hideColumn', 'first');
                $table.bootstrapTable('hideColumn', 'last');
                break;

            case 2:
                if (isMyCampus) {
                    $table.bootstrapTable('hideColumn', 'anon');
                    $table.bootstrapTable('showColumn', 'mcId');
                    $table.bootstrapTable('showColumn', 'name');
                    break;
                }
                $table.bootstrapTable('hideColumn', 'anon');
                $table.bootstrapTable('showColumn', 'id');
                $table.bootstrapTable('showColumn', 'first');
                $table.bootstrapTable('showColumn', 'last');
                break;
        }
        iter++;
        if (iter>2) iter = 1;
        $(this).data('iter',iter);
    });
});

var calculate_data;

function error(message) {
    $('#message').html(
        `<div class="alert alert-danger alert-dismissible fade show" role="alert"> \
            ${message} \
            <button type="button" class="close" data-dismiss="alert" aria-label="Close"> \
                <span aria-hidden="true">&times;</span> \
            </button>\
        </div>`
    )
}

var clear = function() {$('#message').empty()};


// get students and calculate data
function calculate() {
    calculate_data = $('#calculateForm').serialize();
    $table.bootstrapTable('refreshOptions', {
        exportOptions: {"fileName": document.getElementById("plan").value}
    });
    $.ajax({
        headers: { "X-CSRFToken": token },
        url: calculateUrl,
        type: "POST",
        data: calculate_data,
        success: function (data) {
            clear();
            $table.bootstrapTable('refresh', {
                url: dataUrl.concat("?", calculate_data)
            });
        },
        error: function (data) {
            error('Error retrieving data. Please ensure that both <strong>Graduation Year</strong> and <strong>Academic Plans</strong> are selected.')
        }
    })
}
$(function() {
    $('#calculate').click(function() {
        calculate();
    })
});

// ajax post to update database
$('#table').on('editable-save.bs.table', function(e, field, row, oldValue, $el){
    console.log(e);  // event
    console.log(field);  // field
    console.log(row);  // row as json
    console.log(oldValue);  // old value? it just returns a 0
    console.log($el);  // old value
    if (row.alpha === "-") {
        error('Error updating data. Please ensure that <strong>Alphanumeric Grade</strong> is not <strong><i>Empty</i></strong>');
        return;
    }
    $.ajax({
        headers: { "X-CSRFToken": token },
        url: updateUrl,
        type: "POST",
        data: {
            "field": field,
            "row": JSON.stringify(row),
            "el": $el
        },
        dataType: 'json',
        success: function (data) {
            if (row.gradeId) {
                if (!(field === "subNotes")){
                    clear();
                }
                ajax_calculate(token, row, data);
                // ajax_update(token, row, data);
            } else {
                ajax_update(token, row, data);
            }
        }
    });
    function ajax_calculate(token, row, data) {
        if (row.gradeId) {
            $.ajax({
                headers: { "X-CSRFToken": token },
                url: calculateUrl,
                type: "POST",
                data: {"row": JSON.stringify(row)},
                // dataType: 'json',
                success: function (data) {
                    ajax_update(token, row, data);
                }
            });
        }
    };

    // updates the table on every edit. its possible to refresh manually
    // remove the call to this function if required
    function ajax_update(token, row, data) {
        $.ajax({
            headers: { "X-CSRFToken": token },
            url: dataUrl,
            type: "GET",
            data: calculate_data,
            success: function (data) {
                $table.bootstrapTable('refresh', {
                    url: dataUrl.concat("?", calculate_data)
                });
            }
        });
    };
});

// for search
$(document).ready(function() {
    // check for query param
    var url = new URL(document.location);
    var params = url.searchParams;

    var plan = params.get("plan");
    var year = params.get("year");
    var id = params.get("id");
    if (plan && year && id) {
        $table.bootstrapTable('refreshOptions', {
            searchText: id
        });
        $("#plan").val(plan);
        $("#year").val(year);
        calculate();
    }
});
