const canGetCookie = 0;//是否支持存储Cookie 0 不支持 1 支持
//默认账号密码
let CodeVal = 0;
Code();

function Code() {
    if (canGetCookie === 1) {
        createCode("AdminCode");
        const AdminCode = getCookieValue("AdminCode");
        showCheck(AdminCode);
    } else {
        showCheck(createCode(""));
    }
}

function showCheck(a) {
    CodeVal = a;
    const c = document.getElementById("myCanvas");
    const ctx = c.getContext("2d");
    ctx.clearRect(0, 0, 1000, 1000);
    ctx.font = "80px 'Hiragino Sans GB'";
    ctx.fillStyle = "#E8DFE8";
    ctx.fillText(a, 0, 100);
}

$(document).keypress(function (e) {
    // 回车键事件
    if (e.which === 13) {
        $('input[type="button"]').click();
    }
});
//粒子背景特效
$('body').particleground({
    dotColor: '#E8DFE8',
    lineColor: '#133b88'
});
$('input[name="pwd"]').focus(function () {
    $(this).attr('type', 'password');
});
$('input[type="text"]').focus(function () {
    $(this).prev().animate({'opacity': '1'}, 200);
});
$('input[type="text"],input[type="password"]').blur(function () {
    $(this).prev().animate({'opacity': '.5'}, 200);
});
$('input[name="login"],input[name="pwd"]').keyup(function () {
    var Len = $(this).val().length;
    if (!$(this).val() === '' && Len >= 5) {
        $(this).next().animate({
            'opacity': '1',
            'right': '30'
        }, 200);
    } else {
        $(this).next().animate({
            'opacity': '0',
            'right': '20'
        }, 200);
    }
});
function Login_prompt_box(){
    // 登录提示框
    const lpb = '一生之中至少要有两次冲动，\n一次为奋不顾身的爱情，一次为说走就走的旅行。';
    const index = layer.alert(lpb, {
        icon: 6,
        time: 4000,
        offset: 't',
        closeBtn: 0,
        title: '友情提示',
        btn: [],
        anim: 2,
        shade: 0
    });
    layer.style(index, {
        color: '#777'
    });
}
layui.use('layer', function () {
    // 登录验证
    Login_prompt_box()
    //非空验证
    $('input[type="button"]').click(function () {

        const login = $('input[name="login"]').val();
        const pwd = $('input[name="pwd"]').val();
        const code = $('input[name="code"]').val();

        if (login === '') {
            ErroAlert('请输入您的账号');
        } else if (pwd === '') {
            ErroAlert('请输入密码');
        } else if (code === '' || code.length !== 4) {
            ErroAlert('输入验证码');
        } else {
            //认证中..
            // fullscreen();
            $('.login').addClass('test'); //倾斜特效
            setTimeout(function () {
                $('.login').addClass('testtwo'); //平移特效
            }, 300);
            setTimeout(function () {
                let new_authent = $('.authent')
                new_authent.show().animate({right: -320}, {
                    easing: 'easeOutQuint',
                    duration: 600,
                    queue: false
                });
                new_authent.animate({opacity: 1}, {
                    duration: 200,
                    queue: false
                }).addClass('visible');
            }, 500);
            //登陆
            const JsonData = {login: login, pwd: pwd, code: code};
            //此处做为ajax内部判断

            $.ajax({
                url: "/LoginModule/ver_inf",
                type: "POST",
                data: JsonData,
                success: function (data) {
                    setTimeout(function () {
                        $('.authent').show().animate({right: 90}, {
                            easing: 'easeOutQuint',
                            duration: 600,
                            queue: false
                        }).animate({opacity: 0}, {
                            duration: 200,
                            queue: false
                        }).addClass('visible');
                        $('.login').removeClass('testtwo'); //平移特效
                    }, 2000);
                    setTimeout(function () {
                        $('.authent').hide();
                        $('.login').removeClass('test');
                        if (data['code'] === 200) {
                            //登录成功
                            $('.login div').fadeOut(100);
                            $('.success').fadeIn(1000);
                            const token = data['token']
                            localStorage.setItem('z-token',token);
                            window.location.href="/BackStage/";
                            //跳转操作
                        } else {
                            ErroAlert(data['msg']);
                        }
                    }, 2400);
                },
                error: function () {
                    ErroAlert("验证失败");
                }
            })
        }
    })
})