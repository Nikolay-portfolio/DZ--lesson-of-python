from user import User
from card import Card
alex = User("Alex")

alex.sayName()
alex.setAge(33)
alex.sayAge()

card = Card()

alex.addCard(card)
alex.getCard().pay(1000)
