var defalut_option = {
    tooltip : {
        trigger: 'axis',
        axisPointer:
        {
            type:"shadow"
        }
    },
    dataZoom:{
        show:true
    },
    legend: {
        data:[]
    },
    calculable : true,
    xAxis : [
        {
            type : 'category',
            boundaryGap : false,
            splitLine:{
                show:false
            },
            axisLine:{
                show:false,
            },
            data:[]
        }
    ],
    yAxis : [
        {
            type : 'value',
            axisLine:{
                show:false,
            },
        },
    ],
    series : []
};

function build_option()
{
    var option = $.extend(true, {}, defalut_option)
    for (var i in arguments)
    {
        option.legend.data.push(arguments[i])
        option.series.push(
        {
            name:arguments[i],
            type:'line',
            smooth:true,
            symbol:'none',
            data:[]
        })
    }
    return option
}

function ConvertHeader(header)
{
    var header_index = {}
    for (var i in header)
    {
        header_index[header[i]] = i//parseInt(i)
    }
    return header_index
}