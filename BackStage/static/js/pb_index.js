window.onload = function () {
    $(".meun-item").click(function () {
        $(".meun-item").removeClass("meun-item-active");
        $(this).addClass("meun-item-active");
        const itmeObj = $(".meun-item").find("img");
        itmeObj.each(function () {
            let items = $(this).attr("src");
            items = items.replace("_grey.png", ".png");
            items = items.replace(".png", "_grey.png")
            $(this).attr("src", items);
        });
        let attrObj = $(this).find("img").attr("src");
        attrObj = attrObj.replace("_grey.png", ".png");
        $(this).find("img").attr("src", attrObj);
    });
    $("#topAD").click(function () {
        $("#topA").toggleClass(" glyphicon-triangle-right").toggleClass(" glyphicon-triangle-bottom");
    });
    $("#topBD").click(function () {
        $("#topB").toggleClass(" glyphicon-triangle-right").toggleClass(" glyphicon-triangle-bottom");
    });
    $("#topCD").click(function () {
        $("#topC").toggleClass(" glyphicon-triangle-right").toggleClass(" glyphicon-triangle-bottom");
    });
    $(".toggle-btn").click(function () {
        $("#leftMeun").toggleClass("show");
        $("#rightContent").toggleClass("pd0px");
    })
    $.ajax({
        url: '/BackStage/get_user',
        type: 'POST',
        data: '',
        headers: {
            'z-token': localStorage.getItem("z-token")
        },
        success: function (data) {
            let name_p = data['name']
            let mailbox_p = data['mailbox']
            if (name_p === undefined) {
                window.location.href = '/LoginModule'
            } else {
                $("#name_p").text(name_p)
                $("#mailbox_p").text(mailbox_p)
            }

        },
        error: function (data) {

        }
    })
    $.ajax({
        url: '/BackStage/res_manage',
        type: 'GET',
        data: '',
        headers: {
            'z-token': localStorage.getItem("z-token")
        },
        success: function (data) {
            let catalog_list = data['name'];
            let first_level = catalog_list['p_url'];
            let catalog_list_son = catalog_list['son'];
            let len = catalog_list_son.length;
            let father_ele = $('#catalog');
            for (let i = 0; i < len; i++) {
                let cls = catalog_list_son[i];
                let len = cls['son'].length;
                let new_ele_list = "<li class='son_li'>";
                let url_join = first_level+cls['p_url']
                new_ele_list += "<span  class='meun-title son_span' href='"+ url_join +"'>"+cls['p_name']+"</span>";
                new_ele_list += "<ul class='grand_son_ul'>";
                for (let j = 0; j < len; j++) {
                    let grandson = cls['son'][j];
                    new_ele_list += "<li class='grand_son_li'>";
                        new_ele_list += "<img src='/BackStage/static/Images/"+grandson['p_img_url']+"' alt=''/>";
                        let url_join_son = url_join +'/'+ grandson['p_url']
                        new_ele_list += "<span  class='meun-item meun-item-active grand_son_span' href='"+ url_join_son +"'>"+grandson['p_name']+"</span>";
                    new_ele_list += "</li>";
                }
                new_ele_list += " </ul>";
                new_ele_list += "</li>";
                father_ele.append(new_ele_list)
            }
            father_ele.on("click",'.grand_son_span',function(){
                dire_click(this);
            });
        },
        error: function (data) {

        }
    })
}
function dire_click(data){
    let click_url = $(data).attr('href')
    $.ajax({
        url:click_url,
        data:'',
        type:'post',
        headers: {
            'z-token': localStorage.getItem('z-token')
        },
        success:function (data){
            console.log(typeof (data));
            console.log(data);
            $('#pd_tc_iframe').append(data);
        },
        error:function (err){

        }
    })
    return false
}
function sign_out() {
    localStorage.clear()
    window.location.href = '/LoginModule'


}
