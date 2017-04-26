from tcas.db import Base, CommonMixin
from sqlalchemy import Column, ForeignKey, String


class Upload(CommonMixin, Base):
    """This class represents an upload to the application. It aims to assist in the administration of uploads, for 
    instance preventing duplicate uploads and mapping fields of upoaded files to fields of the domain api data model.
    """

    path = Column(String, nullable=False)
    user_id = Column(String, ForeignKey('user.id'), nullable=True)

    def __init__(self, path):
        self.path = path

    @staticmethod
    def validate_post_data(data):
        if data.file() is not None:
            return data
        else:
            return None

    @staticmethod
    def validate_delete_data(data):
        if data.get('password') is not None:
            return data
        else:
            return None

    def serialize(self):
        return {
            'date_created': self.date_created.__str__(),
            'id': self.id,
            'path': self.path
        }
