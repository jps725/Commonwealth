from ..models import db, State

def seed_states():
  Alabama = State(name="Alabama")
  Alaska = State(name="Alaska")
  Arizona = State(name="Arizona")
  Arkansas = State(name="Arkansas")
  California = State(name="California")
  Colorado = State(name="Colorado")
  Connecticut = State(name="Connecticut")
  Delaware = State(name="Delaware")
  Florida = State(name="Florida")
  Georgia = State(name="Georgia")
  Hawaii = State(name="Hawaii")
  Idaho = State(name="Idaho")
  Illinois = State(name="Illinois")
  Indiana = State(name="Indiana")
  Iowa = State(name="Iowa")
  Kansas = State(name="Kansas")
  Kentucky = State(name="Kentucky")
  Louisiana = State(name="Louisiana")
  Maine = State(name="Maine")
  Maryland = State(name="Maryland")
  Massachusetts = State(name="Massachusetts")
  Michigan = State(name="Michigan")
  Minnesota = State(name="Minnesota")
  Mississippi = State(name="Mississippi")
  Missouri = State(name="Missouri")
  Montana = State(name="Montana")
  Nebraska = State(name="Nebraska")
  Nevada = State(name="Nevada")
  NewHampshire = State(name="New Hampshire")
  NewJersey = State(name="New Jersey")
  NewMexico = State(name="New Mexico")
  NewYork = State(name="New York")
  NorthCarolina = State(name="North Carolina")
  NorthDakota = State(name="North Dakota")
  Ohio = State(name="Ohio")
  Oklahoma = State(name="Oklahoma")
  Oregon = State(name="Oregon")
  Pennsylvania = State(name="Pennsylvania")
  RhodeIsland = State(name="Rhode Island")
  SouthCarolina = State(name="South Carolina")
  SouthDakota = State(name="South Dakota")
  Tennessee = State(name="Tennessee")
  Texas = State(name="Texas")
  Utah = State(name="Utah")
  Vermont = State(name="Vermont")
  Virginia = State(name="Virginia")
  Washington = State(name="Washington")
  WestVirginia = State(name="West Virginia")
  Wisconsin = State(name="Wisconsin")
  Wyoming = State(name="Wyoming")

  db.session.add(Alabama)
  db.session.add(Alaska)
  db.session.add(Arkansas)
  db.session.add(Arizona)
  db.session.add(California)
  db.session.add(Colorado)
  db.session.add(Connecticut)
  db.session.add(Delaware)
  db.session.add(Florida)
  db.session.add(Georgia)
  db.session.add(Hawaii)
  db.session.add(Idaho)
  db.session.add(Illinois)
  db.session.add(Indiana)
  db.session.add(Iowa)
  db.session.add(Kansas)
  db.session.add(Kentucky)
  db.session.add(Louisiana)
  db.session.add(Maine)
  db.session.add(Maryland)
  db.session.add(Massachusetts)
  db.session.add(Michigan)
  db.session.add(Minnesota)
  db.session.add(Mississippi)
  db.session.add(Missouri)
  db.session.add(Montana)
  db.session.add(Nebraska)
  db.session.add(Nevada)
  db.session.add(NewHampshire)
  db.session.add(NewJersey)
  db.session.add(NewMexico)
  db.session.add(NewYork)
  db.session.add(NorthCarolina)
  db.session.add(NorthDakota)
  db.session.add(Ohio)
  db.session.add(Oklahoma)
  db.session.add(Oregon)
  db.session.add(Pennsylvania)
  db.session.add(RhodeIsland)
  db.session.add(SouthCarolina)
  db.session.add(SouthDakota)
  db.session.add(Tennessee)
  db.session.add(Texas)
  db.session.add(Utah)
  db.session.add(Vermont)
  db.session.add(Virginia)
  db.session.add(Washington)
  db.session.add(WestVirginia)
  db.session.add(Wisconsin)
  db.session.add(Wyoming)

  db.session.commit()

def undo_states():
  db.session.execute('TRUNCATE states RESTART IDENTITY CASCADE;')
  db.session.commit()