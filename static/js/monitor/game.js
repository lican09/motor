


$(document).ready(function() {

    // 设置路径
    require.config({
        paths: {
            echarts: '/static/js'
        }
    })

    // 加载
    require(
    [
        'echarts',
        'echarts/chart/line'
    ],
    function (ec) {
        Chart1 = ec.init(document.getElementById('Chart1'), "macarons")
        Chart2 = ec.init(document.getElementById('Chart2'), "macarons")
        Chart3 = ec.init(document.getElementById('Chart3'), "macarons")

        $(window).bind("resize", Chart1.resize)
        $(window).bind("resize", Chart2.resize)
        $(window).bind("resize", Chart3.resize)

        Chart1.showLoading({
            effect:"whirling",
        })
        Chart2.showLoading({
            effect:"whirling",
        })
        Chart3.showLoading({
            effect:"whirling",
        })


        AJAX("", function(response){

                header = ConvertHeader(response.header)
                table = response.table

                // 基本信息
                var option = build_option("玩家对象数", "房间对象数", "定时器对象数", "档案对象数")
                for (var i in table)
                {
                    option.xAxis[0].data.push(table[i][header["record_time"]]);
                    option.series[0].data.push(table[i][header["player_obj"]]);
                    option.series[1].data.push(table[i][header["room_obj"]]);
                    option.series[2].data.push(table[i][header["timer_obj"]]);
                    option.series[3].data.push(table[i][header["storage_obj"]]);
                }
                Chart1.setOption(option);
                Chart1.hideLoading();

                // 网络统计front
                var option = build_option("接收：实际", "接收：吞吐", "接收：线路", 
                    "发送：实际", "发送：吞吐", "发送：线路",
                    "内核内存", "正在恢复的会话数", "成功恢复的会话数", "会话总数", 
                    "已经打开的会话数", "统计时段")
                for (var i in table)
                {
                    option.xAxis[0].data.push(table[i][header["record_time"]]);
                    option.series[0].data.push(table[i][header["front_recv_bytes"]]);
                    option.series[1].data.push(table[i][header["front_recv_counts"]]);
                    option.series[2].data.push(table[i][header["front_recv_trans_bytes"]]);
                    option.series[3].data.push(table[i][header["front_send_bytes"]]);
                    option.series[4].data.push(table[i][header["front_send_counts"]]);
                    option.series[5].data.push(table[i][header["front_send_trans_bytes"]]);
                    option.series[6].data.push(table[i][header["front_vm_mem_bytes"]]);
                    option.series[7].data.push(table[i][header["front_session_recovering_"]]);
                    option.series[8].data.push(table[i][header["front_session_recover_ok_"]]);
                    option.series[9].data.push(table[i][header["front_all_session_count_"]]);
                    option.series[10].data.push(table[i][header["front_all_session_open_"]]);
                    option.series[11].data.push(table[i][header["front_timer_period"]]);
                }
                Chart2.setOption(option);
                Chart2.hideLoading();


                // 网络统计login
                var option = build_option("接收：实际", "接收：吞吐", "接收：线路", 
                    "发送：实际", "发送：吞吐", "发送：线路",
                    "内核内存", "失败的连接数", "正在恢复的连接数", "恢复成功的连接数", "连总数", 
                    "已经打开的连数", "统计时段")
                for (var i in table)
                {
                    option.xAxis[0].data.push(table[i][header["record_time"]]);
                    option.series[0].data.push(table[i][header["login_recv_bytes"]]);
                    option.series[1].data.push(table[i][header["login_recv_counts"]]);
                    option.series[2].data.push(table[i][header["login_recv_trans_bytes"]]);
                    option.series[3].data.push(table[i][header["login_send_bytes"]]);
                    option.series[4].data.push(table[i][header["login_send_counts"]]);
                    option.series[5].data.push(table[i][header["login_send_trans_bytes"]]);
                    option.series[6].data.push(table[i][header["login_vm_mem_bytes"]]);
                    option.series[7].data.push(table[i][header["login_connect_failed"]]);
                    option.series[8].data.push(table[i][header["login_connect_recovering"]]);
                    option.series[9].data.push(table[i][header["login_connect_recover_ok"]]);
                    option.series[10].data.push(table[i][header["login_all_connect_count"]]);
                    option.series[11].data.push(table[i][header["login_all_connect_open"]]);
                    option.series[12].data.push(table[i][header["login_timer_period"]]);
                }
                Chart3.setOption(option);
                Chart3.hideLoading();
        })

    });

});