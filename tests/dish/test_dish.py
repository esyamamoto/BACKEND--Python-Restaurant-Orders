import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 2
def test_dish():
    test_dish01 = Dish("lasanha berinjela", 27.00)
    test_dish02 = Dish("lasanha presunto", 25.90)

    test_dish01.add_ingredient_dependency(Ingredient("berinjela"), 15)

    test_dish02.add_ingredient_dependency(Ingredient("presunto"), 15)

    assert test_dish01.get_ingredients() == {Ingredient("berinjela")}
    assert test_dish02.get_ingredients() == {Ingredient("presunto")}

    #assert test_dish01.get_restrictions() == {Restriction.ANIMAL_DERIVED, Restriction.ANIMAL_MEAT}
    assert test_dish02.get_restrictions() == {Restriction.ANIMAL_DERIVED, Restriction.ANIMAL_MEAT}
    assert hash(test_dish01) == hash(test_dish01)
    assert hash(test_dish02) != hash(test_dish01)
    assert test_dish01.__eq__(test_dish01) == True
    assert test_dish01.__eq__(test_dish02) == False
    assert repr(test_dish01) == "Dish('lasanha berinjela', R$27.00)"
    assert test_dish01.name == "lasanha berinjela"

    with pytest.raises(TypeError): 
        Dish("lasanha laranja", "nao e numero kk")

    with pytest.raises(ValueError): 
        Dish("lasanha", -27.00)

   
