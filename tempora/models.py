from tempora import db # Import the database
class Register(db.Model):
    team_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_name = db.Column(db.String(100), nullable=False)
    team_mem_count= db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return "Team Name: {} \n No. of Members: {}".format(self.team_name, self.team_mem_count)
        
class MemberInfo(db.Model):
    member_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_id = db.Column(db.Integer, db.ForeignKey('register.team_id'), nullable=False)
    member_name = db.Column(db.String(100), nullable=False)
    reg_no= db.Column(db.String(100), nullable=True)
    member_email = db.Column(db.String(100), nullable=False)
    member_phone = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return "Member Name: {} \n Reg. No.: {} \n Email: {} \n Phone: {}".format(self.member_name, self.reg_no, self.member_email, self.member_phone)
    
