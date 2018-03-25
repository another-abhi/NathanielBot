from chatbot_engine import response
def test_name():
    a=response("Tell me your name")
    assert a=="Hello, my name is Nathaniel."or a=="I'm Nathaniel" or a=="You can call me Nathaniel"
def test_canteen1():
    assert response("where is the canteen",show_details=True)=="Where are you right now"
def test_canteen2():
    assert response("im at the ccf right now",show_details=True)=="You are in the building right now.The ccf is at the first floor and the canteen ath the ground floor"