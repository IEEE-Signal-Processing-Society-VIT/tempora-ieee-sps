from tempora import db, ma # Import the database

class Team(db.Model):
    __tablename__ = 'team'
    team_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_name = db.Column(db.String(100), nullable=False, unique=True)
    team_size= db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return "Team Name: {} \n No. of Members: {}".format(self.team_name, self.team_mem_count)
        
class MemberInfo(db.Model):
    __tablename__ = 'member_info'
    member_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'), nullable=False)
    member_name = db.Column(db.String(100), nullable=False)
    reg_no= db.Column(db.String(100), nullable=True)
    member_email = db.Column(db.String(100), nullable=False, unique=True)
    member_phone = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return "Member Name: {} \n Reg. No.: {} \n Email: {} \n Phone: {}".format(self.member_name, self.reg_no, self.member_email, self.member_phone)
    
class Submission(db.Model):
    __tablename__ = 'submission'
    submission_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    abstract = db.Column(db.String(1000), nullable=False)
    objective = db.Column(db.String(1000), nullable=False)
    novelty = db.Column(db.String(1000), nullable=False)
    technology_stack = db.Column(db.String(1000), nullable=False)
    document_link= db.Column(db.String(1000), nullable=False)
    business_strategy = db.Column(db.String(1000), nullable=False)

class TeamSchema(ma.Schema):
    class Meta:
        model=Team
        fields = ('team_id', 'team_name', 'team_size')
        
class MemberInfoSchema(ma.Schema):
    class Meta:
        model=MemberInfo
        fields = ('member_id', 'team_id', 'member_name', 'reg_no', 'member_email', 'member_phone')
        
class SubmissionSchema(ma.Schema):
    class Meta:
        model=Submission
        fields = ('submission_id', 'team_id', 'title', 'abstract', 'objective', 'novelty', 'tehcnology_stack', 'doc_link', 'business_strategy')