from atexit import register
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

register_blueprint=Blueprint('register', __name__, url_prefix='/register')