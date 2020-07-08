from flask import (
    Blueprint,
    render_template,
    request
)
from flask_cors import cross_origin

from src.library.logger.Logger import Logger
from src.web.controller import DEFAULT_WORD, word_service, APPLICATION_PATH

app_controller = Blueprint(
    'AppController',
    __name__,
    template_folder='../pages/templates',
    static_folder='../pages/static',
    static_url_path='/assets'
)
template = "index.html"


class AppController:
    @staticmethod
    @cross_origin()
    @app_controller.route('/', methods=['GET'])
    def index():
        word: str = request.args.get('word', DEFAULT_WORD)
        Logger.info(f"Analysing word {word}")

        response: dict = {
            "elements": word_service.word_analysis(word),
            "application_path": APPLICATION_PATH
        }
        Logger.info(response)

        return render_template(template, **response)
