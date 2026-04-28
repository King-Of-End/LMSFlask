from flask import render_template, url_for


def render_style(filename: str, **kwargs):
    return render_template(filename, **kwargs, styles=url_for('static', filename='styles/style.css'))
