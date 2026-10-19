
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self, tax_rate=0.05):
        self.products = []
        self.tax_rate = tax_rate

    def add_product(self, product):
        self.products.append(product)

    def display_bill(self):
        if not self.products:
            print("No products added.")
            return

        print("\n" + "=" * 65)
        print("                       BILL")
        print("=" * 65)
        print(f"{'Product':<20}{'Price':>12}{'Quantity':>12}{'Total':>15}")
        print("-" * 65)

        subtotal = 0

        for product in self.products:
            total = product.get_total()
            subtotal += total

            print(
                f"{product.name:<20}"
                f"{product.price:>12.2f}"
                f"{product.quantity:>12}"
                f"{total:>15.2f}"
            )

        tax = subtotal * self.tax_rate
        final_total = subtotal + tax

        print("-" * 65)
        print(f"{'Subtotal:':>49} ₹{subtotal:>10.2f}")
        print(f"{'Tax (5%):':>49} ₹{tax:>10.2f}")
        print(f"{'Final Total:':>49} ₹{final_total:>10.2f}")
        print("=" * 65)


bill = Bill(tax_rate=0.05)

bill.add_product(Product("Notebook", 50, 2))
bill.add_product(Product("Pen", 10, 5))
bill.add_product(Product("Bag", 500, 1))

bill.display_bill()
