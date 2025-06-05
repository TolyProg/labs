from sqlalchemy import create_engine, MetaData, ForeignKey, \
    Table, Column, Integer, String, text, select, func
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Teacher(Base):
    __tablename__ = 'Teachers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

class Course(Base):
    __tablename__ = 'Courses'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    teacher_id: Mapped[int] = mapped_column(ForeignKey(Teacher.id))

class Student(Base):
    __tablename__ = 'Students'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

class Enrollment(Base):
    __tablename__ = 'Enrollments'
    id: Mapped[int] = mapped_column(primary_key=True)
    student: Mapped[int] = mapped_column(ForeignKey(Student.id))
    course: Mapped[int] = mapped_column(ForeignKey(Course.id))

# engine = create_engine("sqlite+pysqlite:///relative/lab17.db", echo=True)
eng = create_engine("sqlite://", echo=True)
Base.metadata.create_all(eng)

con = eng.connect()
ses = Session(eng)

ses.add_all([
    Course(name='Математический анализ по т. Крузенштерну', teacher_id=2),
    Course(name='Основы квазиметаморфической гомеоморфной культуры', teacher_id=1),
    Course(name='Замкнутые суб-антиметапространства ауфидерзейновой геометрии', teacher_id=4),
    Course(name='Выучи 8 алгоритмов, из них 3 перекрывают остальные', teacher_id=4),
    Course(name='Выучи 42 определения, сдай, забудь', teacher_id=4),
    Course(name='Анекдотическая (реальная) логика', teacher_id=3),
    Course(name='Основы организации отечественных проектных тайм-менеджментных групп с открытым исходным кодом по контролю исполнения надзора над командой специалистов в разработке систем квантового шифрования IP-пакетов для сети из одной и более ЭВМ третьего и старше поколений', teacher_id=1),

    Teacher(name='Контрпродуктов Квазиморф Антикнович'),
    Teacher(name='Всепомнящий Антиян Объяснявич'),
    Teacher(name='Практиков Умослав Быстрорешович'),
    Teacher(name='Зубриловских Яна Итальяновна'),

    Student(name='Бедолагин Пыхтун Стараевич'), *[Enrollment(student=1, course=i) for i in range(0,7)],
    Student(name='Неходинский Прогул Незнаевич'), *[Enrollment(student=2, course=i) for i in range(1,6)],
    Student(name='Леньовский Лежун Допускаевич'), *[Enrollment(student=3, course=i) for i in [0,5]],
    Student(name='Депрессов Устал Помираевич'), *[Enrollment(student=4, course=i) for i in [0,2,3,4,5]],
    Student(name='Степендов Местозанял Лутаевич')
])

ses.flush()

from icecream import ic
# ic(list(ses.execute(text('SELECT * FROM Enrollments'))))

ic('СИСТЕМА ПОИСКА СТАТИСТИКИ, ВЫБОРКИ И АНАЛИЗА Квазиметагомеморф-16М-8У-4000 <<Тюльпанчик>> АКТИВИРОВАНА')

ic('КОЛ-ВО КУРСОВ У ПРЕПОДАВАТЛЯ')
ic(list(ses.execute(
    select(Teacher.name, func.count(Course.id)) \
    .join(Course, Teacher.id == Course.teacher_id) \
    .group_by(Teacher.id)
)))

ic('КОЛ-ВО КУРСОВ У СТУДЕНТА')
ic(list(ses.execute(
    select(Student.name, func.count(func.distinct(Enrollment.course))) \
    .join(Enrollment, Student.id == Enrollment.student, isouter=True) \
    .group_by(Student.id)
)))