# -*- coding:utf-8 -*-
# @文件名称  :public_func
# @项目名称  :PersonalBlog.py
# @软件名称  :PyCharm
# @创建时间  : 2022-01-19 18:07
# @用户名称  :DELL
def r_code(code):
    code_dict = {
        100: {"inter_en": "Continue", "inter_ch": "继续", "explain": "客户端应当继续发送请求。", "inter_sol": "人家… 还要…"},
        101: {"inter_en": "Switching Protocols", "inter_ch": "转换协议",
              "explain": "服务器已经理解了客户端的请求，并将通过Upgrade消息头通知客户端采用不同的协议来完成这个请求。", "inter_sol": "服务姬傲娇中"},
        102: {"inter_en": "Processing", "inter_ch": "", "explain": "由WebDAV（RFC 2518）扩展的状态码，代表处理将被继续执行。",
              "inter_sol": "造人中…"},
        200: {"inter_en": "OK", "inter_ch": "正常", "explain": "请求已成功，请求所希望的响应头或数据体将随此响应返回。", "inter_sol": "欢迎回来, 主人"},
        201: {"inter_en": "Created", "inter_ch": "已创建", "explain": "表示服务器在请求的响应中建立了新文档；应在定位头信息中给出它的URL。",
              "inter_sol": ""},
        202: {"inter_en": "Accepted", "inter_ch": "接受", "explain": "服务器已接受请求，但尚未处理完。", "inter_sol": ""},
        203: {"inter_en": "Non-Authoritative Information", "inter_ch": "非官方信息",
              "explain": "表示文档被正常的返回，但是由于正在使用的是文档副本所以某些响应头信息可能不正确。", "inter_sol": "俺是小三"},
        204: {"inter_en": "No Content", "inter_ch": "无内容",
              "explain": "表示服务器成功处理了请求，但不需要返回任何实体内容，并且希望返回更新了的元信息。在并没有新文档的情况下，确保浏览器继续显示先前的文档。",
              "inter_sol": "小姐呢？！怎么没有？"},
        205: {"inter_en": "Reset Content", "inter_ch": "重置内容", "explain": "意思是虽然没有新文档但浏览器要重置文档显示。这个状态码用于强迫浏览器清除表单域。",
              "inter_sol": "先生，给你换个小姐？"},
        206: {"inter_en": "Partial Content", "inter_ch": "局部内容",
              "explain": "该请求必须包含Range头信息来指示客户端希望得到的内容范围，并且可能包含If-Range来作为请求条件。", "inter_sol": ""},
        207: {"inter_en": "Multi-Status", "inter_ch": "多种状态",
              "explain": "由WebDAV(RFC 2518)扩展的状态码，代表之后的消息体将是一个XML消息，并且可能依照之前子请求数量的不同，包含一系列独立的响应代码。",
              "inter_sol": "搞个NP。嘿嘿…"},
        300: {"inter_en": "Multiple Choices", "inter_ch": "多重选择", "explain": "表示被请求的文档可以在多个地方找到，并将在返回的文档中列出来。",
              "inter_sol": "先生，请点菜。"},
        301: {"inter_en": "Moved Permanently", "inter_ch": "永久迁移",
              "explain": "指所请求的文档在别的地方；文档新的URL会在定位响应头信息中给出。浏览器会自动连接到新的URL。", "inter_sol": "人家搬家了"},
        302: {"inter_en": "Found", "inter_ch": "找到", "explain": "与301有些类似，只是定位头信息中所给的URL应被理解为临时交换地址而不是永久的。",
              "inter_sol": "亲，先等下啦，人家先去洗白白嘛。。。"},
        303: {"inter_en": "See Other", "inter_ch": "参见其他信息",
              "explain": "和 301、302 相似，只是如果最初的请求是 POST，那么新文档（在定位头信息中给出）药用 GET 找回。", "inter_sol": ""},
        304: {"inter_en": "Not Modified", "inter_ch": "没有修改",
              "explain": "如果客户端发送了一个带条件的GET请求且该请求已被允许，而文档的内容（自上次访问以来或者根据请求的条件）并没有改变，则服务器应当返回这个状态码。304响应禁止包含消息体，因此始终以消息头后的第一个空行结尾。",
              "inter_sol": "好久不见，还是风味犹存啊。"},
        305: {"inter_en": "Use Proxy", "inter_ch": "使用代理", "explain": "表示所请求的文档要通过定位头信息中的代理服务器获得。",
              "inter_sol": "泡妞是需要拉皮条的。"},
        306: {"inter_en": "Switch Proxy", "inter_ch": "切换代理", "explain": "在最新版的规范中，306状态码已经不再被使用。",
              "inter_sol": "这店里的鸡太差了，换个。"},
        307: {"inter_en": "Temporary Redirect", "inter_ch": "临时重定向",
              "explain": "在响应为303时按照GET和POST请求转向；而在307响应时则按照GET请求转向而不是POST请求。", "inter_sol": "不是这里, 换个地方啦"},
        400: {"inter_en": "Bad Request", "inter_ch": "错误请求", "explain": "指出客户端请求中的语法错误。", "inter_sol": "不要把奇怪的东西给人家嘛"},
        401: {"inter_en": "Unauthorized", "inter_ch": "未授权", "explain": "表示客户端在授权头信息中没有有效的身份信息时访问受到密码保护的页面。",
              "inter_sol": "对上对联，才让进洞房。"},
        403: {"inter_en": "Forbidden", "inter_ch": "禁止", "explain": "表示除非拥有授权否则服务器拒绝提供所请求的资源。",
              "inter_sol": "这里不可以啦!"},
        404: {"inter_en": "Not Found", "inter_ch": "未找到", "explain": "告诉客户端所给的地址无法找到任何资源。",
              "inter_sol": "这里什么都没有 — 人家是平的啦"},
        405: {"inter_en": "Method Not Allowed", "inter_ch": "方法未允许",
              "explain": "表示请求方法(GET, POST, HEAD, PUT, DELETE, 等)对某些特定的资源不允许使用。", "inter_sol": "打开方式不对"},
        406: {"inter_en": "Not Acceptable", "inter_ch": "无法访问", "explain": "表示请求资源的MIME类型与客户端中Accept头信息中指定的类型不一致。",
              "inter_sol": "啊啊啊,慢着!!好疼"},
        407: {"inter_en": "Proxy Authentication Required", "inter_ch": "代理服务器认证要求", "explain": "该状态指出客户端必须通过代理服务器的认证。",
              "inter_sol": ""},
        408: {"inter_en": "Request Timeout", "inter_ch": "请求超时", "explain": "指服务端等待客户端发送请求的时间过长。", "inter_sol": ""},
        409: {"inter_en": "Conflict", "inter_ch": "冲突", "explain": "该状态通常与PUT请求一同使用，409 状态常被用于试图上传版本不正确的文件时。",
              "inter_sol": "找小姐找到了自己媳妇，然后…"},
        410: {"inter_en": "Gone", "inter_ch": "已经不存在",
              "explain": "告诉客户端所请求的文档已经不存在并且没有更新的地址。410状态不同于404，410是在指导文档已被移走的情况下使用，而404则用于未知原因的无法访问。",
              "inter_sol": "那个，你是个好人……"},
        411: {"inter_en": "Length Required", "inter_ch": "需要数据长度",
              "explain": "表示服务器不能处理请求，除非客户端发送Content-Length头信息指出发送给服务器的数据的大小。", "inter_sol": "太长了…进不去"},
        412: {"inter_en": "Precondition Failed", "inter_ch": "先决条件错误", "explain": "指出请求头信息中的某些先决条件是错误的。",
              "inter_sol": "先买房，然后才能结婚。"},
        413: {"inter_en": "Request Entity Too Large", "inter_ch": "请求实体过大", "explain": "告诉客户端现在所请求的文档比服务器现在想要处理的要大。",
              "inter_sol": ""},
        414: {"inter_en": "Request URI Too Long", "inter_ch": "请求URI过长",
              "explain": "用于在URI过长的情况时。这里所指的URI是指URL中主机、域名及端口号之后的内容。", "inter_sol": "这… 太长了啦"},
        415: {"inter_en": "Unsupported Media Type", "inter_ch": "不支持的媒体格式", "explain": "意味着请求所带的附件的格式类型服务器不知道如何处理。",
              "inter_sol": "石女"},
        416: {"inter_en": "Requested Range Not Satisfiable", "inter_ch": "请求范围无法满足",
              "explain": "表示客户端包含了一个服务器无法满足的Range头信息的请求。", "inter_sol": ""},
        417: {"inter_en": "Expectation Failed", "inter_ch": "期望失败", "explain": "表示在请求头Expect中指定的预期内容无法被服务器满足。",
              "inter_sol": "没房，只能分手了。"},
        418: {"inter_en": "I’m a teapot", "inter_ch": "我是杯具",
              "explain": "本操作码是在1998年作为IETF的传统愚人节笑话,并不需要在真实的HTTP服务器中定义。", "inter_sol": "我就是个杯具啊"},
        421: {"inter_en": "There are too many connections from your internet address", "inter_ch": "该IP发起的链接过多。",
              "explain": "从当前客户端所在的IP地址到服务器的连接数超过了服务器许可的最大范围。", "inter_sol": ""},
        422: {"inter_en": "Unprocessable Entity", "inter_ch": "错误实体", "explain": "请求格式正确，但是由于含有语义错误，无法响应。",
              "inter_sol": ""},
        423: {"inter_en": "Locked", "inter_ch": "锁定", "explain": "当前资源被锁定。", "inter_sol": ""},
        424: {"inter_en": "Failed Dependency", "inter_ch": "错误关联", "explain": "由于之前的某个请求发生的错误，导致当前请求失败。",
              "inter_sol": ""},
        425: {"inter_en": "Unordered Collection", "inter_ch": "乱序集合",
              "explain": "在WebDav Advanced Collections草案中定义，但是未出现在《WebDAV顺序集协议》（RFC 3658）中。", "inter_sol": ""},
        426: {"inter_en": "Upgrade Required", "inter_ch": "升级要求", "explain": "客户端应当切换到TLS/1.0。", "inter_sol": ""},
        428: {"inter_en": "Precondition Required", "inter_ch": "要求先决条件",
              "explain": "先决条件是客户端发送 HTTP 请求时，如果想要请求能成功必须满足一些预设的条件。", "inter_sol": "主人~~不要这么快么~人家还没湿呢。"},
        429: {"inter_en": "Too Many Requests ", "inter_ch": "太多请求", "explain": "当你需要限制客户端请求某个服务数量时，该状态码就很有用，也就是请求速度限制。",
              "inter_sol": "主人~~我快要受不了了~"},
        431: {"inter_en": "Request Header Fields Too Large ", "inter_ch": "请求头字段太大",
              "explain": "某些情况下，客户端发送 HTTP 请求头会变得很大，那么服务器可发送 431状态码 来指明该问题。", "inter_sol": "主人~~这么大方不进去的~~"},
        449: {"inter_en": "Retry With", "inter_ch": "稍后重试", "explain": "由微软扩展，代表请求应当在执行完适当的操作后进行重试。", "inter_sol": ""},
        451: {"inter_en": "Unavailable for Legal Reasons", "inter_ch": "正被审查", "explain": "代表那些因为法律原因而倒下的网站。",
              "inter_sol": "不要啦我们还没领证呀"},
        500: {"inter_en": "Internal Server Error", "inter_ch": "内部服务器错误", "explain": "服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。",
              "inter_sol": "糟了,身体变得有点奇怪了"},
        501: {"inter_en": "Not Implemented", "inter_ch": "未实现", "explain": "服务器不支持当前请求所需要的某个功能。", "inter_sol": ""},
        502: {"inter_en": "Bad Gateway", "inter_ch": "错误的网关", "explain": "作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。",
              "inter_sol": "进错了吗？"},
        503: {"inter_en": "Service Unavailable", "inter_ch": "服务无法获得", "explain": "表示服务器由于在维护或已经超载而无法响应。",
              "inter_sol": "不要…人家还没准备好啦"},
        504: {"inter_en": "Gateway Timeout", "inter_ch": "网关超时", "explain": "指出接收服务器没有从远端服务器得到及时的响应。",
              "inter_sol": ""},
        505: {"inter_en": "HTTP Version Not Supported", "inter_ch": "不支持的 HTTP 版本",
              "explain": "表示服务器并不支持在请求中所标明 HTTP 版本。", "inter_sol": "放开我,放开我,不要中出啊,会怀孕的(但其实是男生,不会怀孕)"},
        506: {"inter_en": "Variant Also Negotiates", "inter_ch": "",
              "explain": "代表服务器存在内部配置错误：被请求的协商变元资源被配置为在透明内容协商中使用自己，因此在一个协商处理中不是一个合适的重点。", "inter_sol": ""},
        507: {"inter_en": "Insufficient Storage", "inter_ch": "", "explain": "服务器无法存储完成请求所必须的内容。",
              "inter_sol": "都流出来了…"},
        509: {"inter_en": "Bandwidth Limit Exceeded", "inter_ch": "", "explain": "服务器达到带宽限制。这不是一个官方的状态码，但是仍被广泛使用。",
              "inter_sol": "今天不接客了"},
        510: {"inter_en": "Not Extended", "inter_ch": "", "explain": "获取资源所需要的策略并没有没满足。", "inter_sol": "没车没钱还想泡妞？"},
        511: {"inter_en": "Network Authentication Required ", "inter_ch": "要求网络认证",
              "explain": "在你想使用web服务的时候需要重定向到认证页面，在走HTTP通信中都是这么做的，", "inter_sol": "主人~~不要蒙住我的眼睛~会好兴奋的！~"},
        4002: {"inter_en": "Account password error", "inter_ch": "账号密码错误", "explain": "客户端发送的账号密码不存在与本地。", "inter_sol": "来不了"},
        4003: {"inter_en": "Verification code error", "inter_ch": "验证码错误", "explain": "客户端输入的验证码错误。", "inter_sol": "输入错误"},
        4004: {"inter_en": "Verification failed", "inter_ch": "验证未通过", "explain": "客户端无法通过安全验证", "inter_sol": "没通过"},
        4103: {"inter_en": "missing parameter token", "inter_ch": "缺少参数token", "explain": "客户端未发送token。", "inter_sol": "不让验一验的吗"},
        4101: {"inter_en": "Login expired", "inter_ch": "登录已过期", "explain": "客户端应当继续发送请求。", "inter_sol": "改口费到期了"},
    }
    if code in code_dict.keys():
        return code_dict[code]
    else:
        return {"inter_en": "", "inter_ch": "", "explain": "。", "inter_sol": ""}
