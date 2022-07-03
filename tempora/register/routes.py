from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

register_blueprint = Blueprint(
    'register', 
    __name__, 
    url_prefix='/register', 
    template_folder='../../templates', 
    static_folder='static',
    static_url_path='/static'
    )

@register_blueprint.route('/', methods=['GET', 'POST'])
def register():
    return render_template('form.html')