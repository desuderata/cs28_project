const ttpt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
    12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22];
const gpa = ["Fail", "33", "0L", "0U", "01"];
const labels = {"ttpt": ttpt, "gpa":gpa};
var graph = "gpa";

function setGraphType() {
    graph = document.getElementById("graph").value;
    chart.data = {
        labels: graph ? labels[graph] : gpa,
        datasets: []
    };
    chart.update();
    colorCount = 0;
}
function setGraphDetails() {
    var title = document.getElementById("title").value;
    var xAxis = document.getElementById("axisX").value;
    var yAxis = document.getElementById("axisY").value;
    chart.options.title.text = title ? title : "Students vs. GPA";
    chart.options.scales.yAxes[0].scaleLabel.labelString = yAxis ? yAxis : "Students";
    chart.options.scales.xAxes[0].scaleLabel.labelString = xAxis ? xAxis : "GPA";
    chart.update();
}

function getCount(input) {
    if (graph == "ttpt") {
        count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for (let i=0; i<input.length; i++) {
            count[parseInt(input[i].gpa)]++;
        }
    } else if (graph == "gpa") {
        count = [0, 0, 0, 0, 0];
        for (let i=0; i<input.length; i++) {
            switch (input[i].award) {
                case "Fail":
                    count[0]++;
                    break;
                case "33":
                    count[1]++;
                    break;
                case "0L":
                    count[2]++;
                    break;
                case "0U":
                    count[3]++;
                    break;
                case "01":
                    count[4]++;
                    break;
            }
        }
    }
    return count;
}

function getPercentage(input) {
    console.log(graph)
    count = getCount(input);
    total = count.reduce((a, b) => a + b, 0);
    for (let i=0; i<count.length; i++) {
        count[i] /= total / 100;
    }
    return count;
}

$(function() {
$('#add').click(function() {
    data = $('#dataset').serialize()
        $.ajax({
            headers: { "X-CSRFToken": token },
            url: dataUrl,
            type: "GET",
            data: data,
            success: function (data) {
                // var data = console.log(getData(data));
                $('#message').empty();
                plan = document.getElementById("plan").value;
                year = document.getElementById("year").value;
                type = document.getElementById("type").value;
                if (type) {
                    addDataset(`${plan} | ${year} | ${type=="percentage"?"%":"#"}`,
                        type=="percentage"?getPercentage(data):getCount(data));
                }
            },
            error: function (data) {
                $('#message').html(
                    '<div class="alert alert-danger alert-dismissible fade show" role="alert"> \
                        Error retrieving data. Please ensure that <strong>Academic Year</strong>, \
                        <strong>Academic Plan</strong> and  <strong>Type</strong> are selected. \
                        <button type="button" class="close" data-dismiss="alert" aria-label="Close"> \
                            <span aria-hidden="true">&times;</span> \
                        </button>\
                    </div>')
            }
        })
    })
})

var chart;

$(function() {
    var bar = document.getElementById('bar').getContext('2d');
    chart = new Chart(bar, {
        type: 'bar',
        data: {
            labels: gpa,
            datasets: []
        },
        options: {
            title: {
                display: true,
                text: 'Students vs. GPA'
            },
            tooltips: {
                mode: 'index'
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        min: 0,
                        precision: 0
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Students'
                    }
                }],
                xAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'GPA'
                    }
                }],
            },
            elements: {
                rectangle: {
                    borderWidth: 1
                }
            }
        }
    });
});

function addDataset(label, data) {
    color = colorCount<colors.length-1? colors[colorCount] : getColor();
    colorCount++;
    chart.data.datasets.push({
        label: label,
        data: data,
        backgroundColor: color[1],
        borderColor: color[0]
    });
    chart.update();
}

function removeDataset() {
    chart.data.datasets.pop();
    if (colorCount >= 0) colorCount--;
    console.log(colorCount);
    chart.update();
}

function resetDataset() {
    colorCount = 0;
    console.log(colors);
    chart.data.datasets = [];
    chart.update();
}

function changeTitle(title) {
    chart.options.title = title;
}

var colorCount = 0;

var colors = [
    ['rgba(255, 99, 132, 1)', 'rgba(255, 99, 132, 0.2)'],
    ['rgba(54, 162, 235, 1)', 'rgba(54, 162, 235, 0.2)'],
    ['rgba(255, 206, 86, 1)', 'rgba(255, 206, 86, 0.2)'],
    ['rgba(75, 192, 192, 1)', 'rgba(75, 192, 192, 0.2)'],
    ['rgba(153, 102, 255, 1)', 'rgba(153, 102, 255, 0.2)'],
    ['rgba(255, 159, 64, 1)', 'rgba(255, 159, 64, 0.2)']
]

function getColor() { 
    randCol = Math.round(360 * Math.random())

    return [`hsla(${randCol}, 70%, 80%, 1)`,
            `hsla(${randCol}, 70%, 80%, 0.2)`]
}