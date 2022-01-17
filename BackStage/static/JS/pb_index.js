window.onload =function() {
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
        type:'POST',
        data:'',
        headers:{
            'z-token':localStorage.getItem("z-token")
        },
        success: function (data) {
            let name_p = data['name']
            let mailbox_p = data['mailbox']
            if (name_p === undefined){
                window.location.href = '/LoginModule'
            }else{
            $("#name_p").text(name_p)
            $("#mailbox_p").text(mailbox_p)
            }

        },
        error:function (data){

        }
    })
}
function sign_out() {
    localStorage.clear()
    window.location.href = '/LoginModule'


}
