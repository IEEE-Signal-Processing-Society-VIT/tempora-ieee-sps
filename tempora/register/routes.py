from flask import Blueprint, render_template, request, redirect, url_for
from tempora.models import Team
from tempora import db
import json
from .utils import add_team, add_member, isValidTeam, getTeamName, add_submission


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
    #GET Method
    if request.method=="GET":
        message=request.args.get('message')
        if message: # Team Already Exists redirect to register page
            message=json.loads(message)
            message=message["error"]  
        else: # Normal Page Load
            message="Phoenix"
        return render_template('register.html', message=message)
    
    #POST Method
    if request.method=="POST":
        (team_name, name, reg_no, email, phone, team_size) = (request.form['team_name'], request.form['name'], request.form['reg_no'], request.form['email'], request.form['phone'], request.form['team_size'])
        # session['messages'] = messages
        if db.session.query(Team).filter_by(team_name=team_name).first():
            name_exists={}
            name_exists['error']="Name Exists, Try again."
            name_exists=json.dumps(name_exists)
            return redirect(url_for('register.register', message=name_exists))
        
        messages={}
        messages['team_id']=add_team(team_name, team_size)
        messages['lead_id']=add_member(messages['team_id'], name, reg_no, email, phone)
        
        if team_size==str(1):
            messages=json.dumps(messages)
            return redirect(url_for('register.submission', message=messages))
        messages['team_size']=team_size
        messages=json.dumps(messages)
        return redirect(url_for('register.team', messages=messages))
        
@register_blueprint.route('/team', methods=['GET', 'POST'])
def team():
    if request.method=="GET":
        messages=request.args['messages']
        if messages:
            messages=json.loads(messages)
            team_id=messages['team_id']
            team_name=getTeamName(team_id)
            lead_id=messages['lead_id']
            team_size=messages['team_size']
            if isValidTeam(team_id, lead_id):
                return render_template('register_teammates.html', team_id=team_id, lead_id=lead_id, team_name=team_name, team_size=list(range(1,int(team_size))))
        return "<h1>Not Authorised</h1>"
    if request.method=="POST":
        team_size=request.form['team_size']
        team_id=request.form['team_id']
        
        for i in list(range(2, int(team_size)+1)):
            (name, reg_no, email, phone) = (request.form['name'+str(i)], request.form['reg_no'+str(i)], request.form['email'+str(i)], request.form['phone'+str(i)])
            member=add_member(team_id, name, reg_no, email, phone)
        
        messages={}
        messages['team_id']=team_id
        messages=json.dumps(messages)
        return redirect(url_for('register.submission', message=messages))
         
@register_blueprint.route('/submission', methods=['GET', 'POST'])
def submission():
    if request.method=="GET":
        messages=request.args['message']
        if messages:
            messages=json.loads(messages)
            team_id=messages['team_id']
            team_name=getTeamName(team_id)
            return render_template('submission.html', team_id=team_id, team_name=team_name)
    if request.method=="POST":
        (team_id, title, abstract, objective, novelty, 
         technology_stack, document_link, business_strategy) = (
             request.form['team_id'], request.form['title'], request.form['abstract'], 
         request.form['objective'], request.form['novelty'], request.form['technology_stack'], 
         request.form['document_link'], request.form['business_strategy'])
        
        submission=add_submission(team_id, title, abstract, objective, novelty, technology_stack, document_link, business_strategy)
        if submission:
            return render_template('submission_success.html')