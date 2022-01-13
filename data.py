from flask_orm_new import db
db.create_all

from flask_orm_new import User


def insert_users():
    user1 = User(
        name='Raymonde N. Lopez',
        email='RaymondeNLopez@teleworm.us',
        dob='1988-03-18'
    )

    user2 = User(
        name='Thais Ferreira Azedevo',
        email='ThaisFerreiraAzedevo@teleworm.us',
        dob='1958-11-02'
    )

    user3 = User(
        name='Kornelis van Egmond',
        email='KornelisvanEgmond@dayrep.com',
        dob='1978-03-18'
    )


    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()


if __name__ == '__main__':
    insert_users()