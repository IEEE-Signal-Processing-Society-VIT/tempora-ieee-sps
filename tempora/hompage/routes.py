from flask import Blueprint, render_template

homepage_blueprint=Blueprint(
    'homepage',
    __name__,
    url_prefix='/',
    template_folder='../../templates',
    static_folder='static',
    static_url_path='/static'
    )

@homepage_blueprint.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')