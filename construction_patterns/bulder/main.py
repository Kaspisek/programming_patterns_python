from abc import ABC
from typing import List


class Product:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()


class AProductBuilder(ABC):
    required_ingredients: List[Product, ] = None

    def buy_sub_products(self) -> List[Product, ]:
        raise NotImplementedError()

    def create_product(self, sub_products: List[Product, ]):
        required_ingredients_names_set = set(map(lambda obj: obj.name, self.required_ingredients))
        sub_products_names_set = set(map(lambda obj: obj.name, sub_products))
        if required_ingredients_names_set != sub_products_names_set:
            raise AttributeError(
                "You do not have right ingredients,\n"
                f"You have to have: {', '.join(map(str, self.required_ingredients))}\n"
                f"You have: {', '.join(map(str, sub_products))}."
            )

    def get_product(self) -> Product:
        raise NotImplementedError()


class BreadBuilder(AProductBuilder):
    required_ingredients = [Product("Flour"), Product("Water"), Product("Salt"), Product("Yeast")]

    def __init__(self):
        self._product = None

    def buy_sub_products(self) -> List[Product, ]:
        return [Product("Flour"), Product("Water"), Product("Salt"), Product("Yeast")]

    def create_product(self, sub_products: List[Product, ]):
        super().create_product(sub_products)
        self._product = Product("Bread")

    def get_product(self) -> Product:
        return self._product


class SandwichBuilder(AProductBuilder):
    required_ingredients = [Product("Ham"), Product("Butter"), Product("Bread")]

    def __init__(self):
        self._product = None

    def buy_sub_products(self) -> List[Product, ]:
        return [Product("Ham"), Product("Butter"), Product("Bread")]

    def create_product(self, sub_products: List[Product, ]):
        super().create_product(sub_products)
        self._product = Product("Sandwitch")

    def get_product(self) -> Product:
        return self._product


class Employee:

    def __init__(self, builder: AProductBuilder, ):
        self._builder = builder

    def make(self):
        sub_products = self._builder.buy_sub_products()
        self._builder.create_product(sub_products)


if __name__ == '__main__':
    builder = BreadBuilder()
    employee = Employee(builder)
    employee.make()
    assert builder.get_product() == Product("Bread")

    builder = SandwichBuilder()
    employee = Employee(builder)
    employee.make()
    assert builder.get_product() == Product("Sandwitch")