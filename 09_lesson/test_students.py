# ДОБАВЛЕНИЕ

from db import SessionLocal
from models import Student


def test_create_student():
    session = SessionLocal()

    student = Student(name="Ivan")
    session.add(student)
    session.commit()

    result = session.query(Student).filter_by(name="Ivan").first()

    assert result is not None

    # очистка
    session.delete(result)
    session.commit()
    session.close()


# ИЗМЕНЕНИЕ
def test_update_student():
    session = SessionLocal()

    student = Student(name="OldName")
    session.add(student)
    session.commit()

    student.name = "NewName"
    session.commit()

    updated = session.query(Student).filter_by(name="NewName").first()

    assert updated is not None

    # очистка
    session.delete(updated)
    session.commit()
    session.close()


# УДАЛЕНИЕ
def test_delete_student():
    session = SessionLocal()

    student = Student(name="ToDelete")
    session.add(student)
    session.commit()

    session.delete(student)
    session.commit()

    deleted = session.query(Student).filter_by(name="ToDelete").first()

    assert deleted is None

    session.close()
