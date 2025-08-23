def calculate_discount(price, discount_percentage):
    if discount_percentage >=20:
        discount_amount = price * (discount_percentage/100)
        return price - discount_amount
    else:
        return price
    
    def main():
        try:
            original_price = float(input("Enter the original price of the item: "))
            discount_percentage = float(input("Enter the discount percentage: "))

            if original_price < 0 or discount_percentage < 0:
                print("Error: price and discount percentage must be non-negative")
                return
            
            final_price = calculate_discount(original_price, discount_percentage)

            if discount_percentage >= 20:
                print(f"Discount applied: {discount_percentage: .2f}% off")
            else:
                print("No discount applied (discount must be higher than 20%).")
            print(f"Final price: Ksh{fianl_price: .2f}")
        except ValueError:
            print("please enter valid values.")
    
    if __name__=="__main__":
        main()