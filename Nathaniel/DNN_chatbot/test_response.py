from .chatbot_engine import response
def test_name():
    a=response("Tell me your name")
    assert a=="Hello, my name is Nathaniel."or a=="I'm Nathaniel" or a=="You can call me Nathaniel"
def test_canteen1():
    assert response("where is college canteen",show_details=True)=="Where are you right now"
    
def test_name2():
    a=response("Who are you")
    print(a)
    assert a=="Hello, my name is Nathaniel."or a=="I'm Nathaniel" or a=="You can call me Nathaniel"

def test_depts():
    a=response("What departments are there ?")
    assert a=="Our departments are  CS, EC, MECH and BT" or a== "We teach CS, EC, MECH and BT"

def test_facilities():
    a=response("What are the facilities")
    assert a=="We provide wifi, libarary , a central computing facility and many other features."

def test_sport():
    a=response("what are the sports")
    assert a=="We have a basketball court, a cricket net, a volleyball court and 2 badminton courts."or a== "We encourage students to play badminton, football, volleyball, cricket and basketball here."  

def test_sport1():
    a=response("what are sports facilites are there")
    assert a=="We have a basketball court, a cricket net, a volleyball court and 2 badminton courts."or a== "We encourage students to play badminton, football, volleyball, cricket and basketball here."      