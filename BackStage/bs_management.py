from flask import Blueprint, render_template
from BackStage import model as md
from PublicFunction.token import login_required

BackStage = Blueprint("BackStage", __name__, template_folder='./templates', static_folder='./static',
                      static_url_path='static')


@BackStage.route('/bs_manage')
@login_required
def index():
    """
    返回登录页面
    :return:
    """
    return render_template('pb_index.html')
