from models.number import Number
from models.fraction import Fraction
from models.library import Library
from models.date_model import Date
from views.view import View

class Controller:
    def run(self):
        # Number
        a = Number(10)
        b = Number(5)
        View.show("Number +", a + b)
        View.show("Number -", a - b)
        View.show("Number *", a * b)
        View.show("Number /", a / b)

        # Fraction
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        View.show("Fraction +", f1 + f2)
        View.show("Fraction -", f1 - f2)
        View.show("Fraction *", f1 * f2)
        View.show("Fraction /", f1 / f2)

        # Library
        lib1 = Library("Central", "Odesa", 1000)
        lib2 = Library("City", "Kyiv", 800)

        lib1 += 200
        View.show("Library after +=", lib1)
        View.show("Library > ?", lib1 > lib2)

        # Date
        d1 = Date(1, 1, 2026)
        d2 = Date(10, 1, 2026)

        View.show("Days between", d2 - d1)
        View.show("Date + 5 days", d1 + 5)