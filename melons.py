"""Classes for melon orders."""

class AbstractMelonOrder:

    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class OrderTypeMixin:
    def order_type(self):
        print(self)


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        self.order_type = "domestic"
        self.tax = 0.08
        # self.species = species
        # self.qty = qty
        # self.shipped = False


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder, OrderTypeMixin):
    """An international (non-US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, "international", 0.17)
        self.tax = 0.17
        self.order_type = "international"
        # elf.species = species
        # elf.qty = qty
        # elf.country_code = country_code
        # self.shipped = False
    
    def get_country_code(self, country_code):
        # def get_country_code(self):
        """Return the country code."""
        
        self.country_code = country_code
        return self.country_code

