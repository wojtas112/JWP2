from app import db

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Teacher %r>' % self.name