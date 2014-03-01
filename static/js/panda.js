search = function() {
    var target = document.getElementById('load');
    var spinner = new Spinner(opts).spin(target);
    $.getJSON($root_url + 'search', {
        
        search: document.getElementById('search').value,
    }, function(data) {
        spinner.stop();
        if (data.result == "ITEM_NOT_FOUND")
            document.getElementById('not-found').style.display = 'Block';
        else {
            document.getElementById('not-found').style.display = 'None';
            window.analysis = data;
            set_highchart(data);
            set_barchart(data);
        }
    });
}

var opts = {
  lines: 9, // The number of lines to draw
  length: 27, // The length of each line
  width: 3, // The line thickness
  radius: 25, // The radius of the inner circle
  corners: 1, // Corner roundness (0..1)
  rotate: 0, // The rotation offset
  direction: 1, // 1: clockwise, -1: counterclockwise
  color: '#ff0000', // #rgb or #rrggbb or array of colors
  speed: 0.9, // Rounds per second
  trail: 40, // Afterglow percentage
  shadow: false, // Whether to render a shadow
  hwaccel: false, // Whether to use hardware acceleration
  className: 'spinner', // The CSS class to assign to the spinner
  zIndex: 2e9, // The z-index (defaults to 2000000000)
  top: '3', // Top position relative to parent in px
  left: '1' // Left position relative to parent in px
};

set_highchart = function(data) {

    sentiments = data['amzn_senti'];
    total = sentiments['positive'] + sentiments['negative'] + sentiments['neutral']
    positive_percent = sentiments['positive'] * 100 / total;
    negative_percent = sentiments['negative'] * 100/ total;
    neutral_percent = sentiments['neutral'] * 100/ total;
    // Build the chart
    $('#amzn-pie').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false
        },
        title: {
            text: 'Amazon'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>',
            yDecimals: 2
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    color: '#000000',
                    connectorColor: '#000000',
                    formatter: function() {
                        return '<b>'+ this.point.name +'</b>: '+ Math.round(this.percentage) +' %';
                    }
                }
            }
        },
        series: [{
            type: 'pie',
            name: 'Customer Sentiment',
            data: [
                { name: 'Positive', 
                  y: positive_percent,
                  color: '#00ff00',
                },
                { name: 'Negative', 
                  y: negative_percent,
                  color: '#ff0000',
                },
                { name: 'Neutral', 
                  y: neutral_percent,
                  color: '#666666',
                },
            ]
        }]
    });

    sentiments = data['flip_senti'];
    total = sentiments['positive'] + sentiments['negative'] + sentiments['neutral']
    positive_percent = sentiments['positive'] * 100 / total;
    negative_percent = sentiments['negative'] * 100/ total;
    neutral_percent = sentiments['neutral'] * 100/ total;
    // Build the chart
    $('#flip-pie').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false
        },
        title: {
            text: 'Flipkart'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>',
            yDecimals: 2
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    color: '#000000',
                    connectorColor: '#000000',
                    formatter: function() {
                        return '<b>'+ this.point.name +'</b>: '+ Math.round(this.percentage) +' %';
                    }
                }
            }
        },
        series: [{
            type: 'pie',
            name: 'Customer Sentiment',
            data: [
                { name: 'Positive', 
                  y: positive_percent,
                  color: '#00ff00',
                },
                { name: 'Negative', 
                  y: negative_percent,
                  color: '#ff0000',
                },
                { name: 'Neutral', 
                  y: neutral_percent,
                  color: '#666666',
                },
            ]
        }]
    });

    sentiments = data['twitter_senti'];
    total = sentiments['positive'] + sentiments['negative'] + sentiments['neutral']
    positive_percent = sentiments['positive'] * 100 / total;
    negative_percent = sentiments['negative'] * 100/ total;
    neutral_percent = sentiments['neutral'] * 100/ total;
    // Build the chart
    $('#twitter-pie').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false
        },
        title: {
            text: 'Twitter'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>',
            yDecimals: 2
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    color: '#000000',
                    connectorColor: '#000000',
                    formatter: function() {
                        return '<b>'+ this.point.name +'</b>: '+ Math.round(this.percentage) +' %';
                    }
                }
            }
        },
        series: [{
            type: 'pie',
            name: 'Customer Sentiment',
            data: [
                { name: 'Positive', 
                  y: positive_percent,
                  color: '#00ff00',
                },
                { name: 'Negative', 
                  y: negative_percent,
                  color: '#ff0000',
                },
                { name: 'Neutral', 
                  y: neutral_percent,
                  color: '#666666',
                },
            ]
        }]
    });
}

set_barchart = function(data) {
    $('#features-bar').highcharts({
        chart: {
        type: 'column'
        },
        title: {
            text: 'Features'
        },
        xAxis: {
            categories: ['Display', 'Battery', 'RAM', 'Storage']
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Number'
            },
            stackLabels: {
                enabled: true,
                style: {
                    fontWeight: 'bold',
                    color: (Highcharts.theme && Highcharts.theme.textColor) || 'gray'
                }
            }
        },
            legend: {
            align: 'right',
            x: -70,
            verticalAlign: 'top',
            y: 20,
            floating: true,
            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColorSolid) || 'white',
            borderColor: '#CCC',
            borderWidth: 1,
            shadow: false
        },
        tooltip: {
            formatter: function() {
                return '<b>'+ this.x +'</b><br/>'+
                    this.series.name +': '+ this.y +'<br/>'+
                    'Total: '+ this.point.stackTotal;
            }
        },
        plotOptions: {
            column: {
                stacking: 'normal',
                dataLabels: {
                    enabled: true,
                    color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white',
                    style: {
                        textShadow: '0 0 3px black, 0 0 3px black'
                    }
                }
            }
        },
        series: [{
            name: 'Positive',
            data: [5, 3, 4, 7]
        }, {
            name: 'Neutral',
            data: [2, 2, 3, 2]
        }, {
            name: 'Negative',
            data: [3, 4, 4, 2]
        }]
    });
}