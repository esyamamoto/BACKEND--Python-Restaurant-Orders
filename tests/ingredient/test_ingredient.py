from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ing01 = Ingredient("queijo mussarela")
    ing02 = Ingredient("farinha")
    ing03 = Ingredient("bacon")
    ing04 = Ingredient("manteiga")
    

    assert ing01.name == "queijo mussarela"
    
    assert ing01.name != ing02.name

    # igualdade
    assert ing01.__eq__(ing01) == True
    assert ing01.__eq__(ing02) == False

    # __repr__
    assert ing01.__repr__() == "Ingredient('queijo mussarela')"
    assert ing02.__repr__() != ing01.__repr__

    # __hash__
    assert ing01.__hash__() == hash("queijo mussarela")
    assert ing02.__hash__() != ing01.__hash__()

    # restricao
    assert ing02.restrictions == {Restriction.GLUTEN}
    # so tem 1 de farinha
