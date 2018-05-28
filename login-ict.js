var qData = {"action": "login", "username": "xxx", "password": "xxx", "ac_id": "1", "ip":"x.x.x.x"}
$.getJSON("https://gw.ict.ac.cn/cgi-bin/srun_portal", qData, function(data) {
    if (data.error == "ok") {
        $.cookie('access_token', data.access_token)
        location.href = location.protocol + "//" + location.hostname + "/srun_portal_pc_succeed.php?ac_id=1&username=fengxiao&ip=10.30.10.233&access_token="+data.access_token
    }
})
