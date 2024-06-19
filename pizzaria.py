class PizzaComponent:
    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost
    
class Massa(PizzaComponent):
    cost=0.0
    
class Decorator(PizzaComponent):
    def __init__(self, pizzaComponent):
        self.component = pizzaComponent

    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)
    
    def getDescription(self):
        return self.component.getDescription() + ' ' + PizzaComponent.getDescription(self)
    
class Mussarela(Decorator):
    cost=12.50
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Calabresa(Decorator):
    cost=12.50
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Peperoni(Decorator):
    cost=12.50
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)
        
class Bacon(Decorator):
    cost=12.50
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Molho(Decorator):
    cost=5.50
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)

class Catupiry(Decorator):
    cost=7.50
    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


pizzaCalaBacon = Molho(Bacon(Calabresa(Massa())))

print(pizzaCalaBacon.getDescription() + ":R$" + str(pizzaCalaBacon.getTotalCost()))