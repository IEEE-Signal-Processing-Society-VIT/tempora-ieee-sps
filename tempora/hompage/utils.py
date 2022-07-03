from tempora.models import Team, MemberInfo, TeamSchema, MemberInfoSchema, Submission, SubmissionSchema

def retrieve_data():
    teams=Team.query.all()
    teams=TeamSchema(many=True).dump(teams)
    for team in teams:
        team_id=team["team_id"]
        members=MemberInfo.query.filter_by(team_id=team_id).all()
        members=MemberInfoSchema(many=True).dump(members)
        team["members"]=members
        
        submission=Submission.query.filter_by(team_id=team_id).order_by(Submission.submission_id.desc()).first()
        submission=SubmissionSchema(many=False).dump(submission)
        team["submission"]=submission
    return teams
        