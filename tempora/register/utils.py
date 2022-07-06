from tempora.models import Team, MemberInfo, TeamSchema, MemberInfoSchema, Submission, SubmissionSchema
from tempora import db

def add_team(team_name, team_size):
    team = Team(team_name=team_name, team_size=team_size)
    db.session.add(team)
    db.session.commit()
    team=db.session.query(Team).filter_by(team_name=team_name).first()
    team=TeamSchema(many=False).dump(team)
    team=team["team_id"]
    return team

def add_member(team_id, member_name, reg_no, email, phone):
    is_member=db.session.query(MemberInfo).filter_by(reg_no=reg_no).filter_by(team_id=team_id).first()
    if is_member: 
        is_member.member_name=member_name
        is_member.member_email=email
        is_member.member_phone=phone
        is_member.reg_no=reg_no
        db.session.commit()
    else:
        member = MemberInfo(team_id=team_id, member_name=member_name, reg_no=reg_no, member_email=email, member_phone=phone)
        db.session.add(member)
        db.session.commit()
    member=db.session.query(MemberInfo).filter_by(member_name=member_name).filter_by(team_id=team_id).first()
    member=MemberInfoSchema(many=False).dump(member)
    member=member["member_id"]
    return member

def isValidTeam(team_id, lead_id):
    team=db.session.query(Team).filter_by(team_id=team_id).first()
    lead=db.session.query(MemberInfo).filter_by(member_id=lead_id).first()
    if team and lead:
        return True
    return False

def getTeamName(team_id):
    team=db.session.query(Team).filter_by(team_id=team_id).first()
    team=TeamSchema(many=False).dump(team)
    team=team["team_name"]
    return team

def add_submission(team_id, title, abstract, objective, novelty, technology_stack, document_link, business_strategy):
    is_submission=db.session.query(Submission).filter_by(team_id=team_id).first()
    if is_submission:
        is_submission.title=title
        is_submission.abstract=abstract
        is_submission.objective=objective
        is_submission.novelty=novelty
        is_submission.technology_stack=technology_stack
        is_submission.document_link=document_link
        is_submission.business_strategy=business_strategy
        db.session.commit()
    else: 
        submission = Submission(team_id=team_id, title=title, abstract=abstract, objective=objective, novelty=novelty, technology_stack=technology_stack, document_link=document_link, business_strategy=business_strategy)
        db.session.add(submission)
        db.session.commit()
    submission=db.session.query(Submission).filter_by(team_id=team_id).first()
    submission=SubmissionSchema(many=False).dump(submission)
    submission=submission["submission_id"]
    return submission