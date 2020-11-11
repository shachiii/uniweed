from db import db


class WeedProductModel(db.Model):
    __tablename__ = 'weedproduct'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    crop = db.Column(db.String(80))
    product = db.Column(db.String(80))
    dose = db.Column(db.String(80))

    def __init__(self, name, crop, product, dose):
        self.name = name
        self.crop = crop
        self.product = product
        self.dose = dose

    def json(self):
        return {'name': self.name, 'product': self.product, 'dose': self.dose}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name)

    @classmethod
    def find_object(cls, item_obj):
        # print(item_obj)
        item = cls.query.filter_by(name=item_obj.name, product=item_obj.product, crop=item_obj.crop, dose=item_obj.dose).scalar()
        # print(item)
        if item:
            return True
        else:
            return False

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
