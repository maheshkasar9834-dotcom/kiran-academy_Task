# Task 01: Shopping Bill

# 1. Calculate Electronics GST (18%)
def calculateElectronicsGST(a, b):
    total = a + b
    gst = total * 18 / 100
    return total + gst


# 2. Calculate Fashion GST (13%)
def calculateFashionGST(c, d):
    total = c + d
    gst = total * 13 / 100
    return total + gst


# 3. Calculate Food GST (7%)
def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst


# 4. Calculate Total Bill After GST
def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    total = electronics + fashion + food
    return total


# 5. Calculate Final Bill After 20% Discount
def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    final_amount = total - discount

    return final_amount


# Main Program
a = 100
b = 100
c = 100
d = 100
e = 100

electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)

total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)

print("Electronics After GST:", format(electronics, ".2f"))
print("Fashion After GST:", format(fashion, ".2f"))
print("Food After GST:", format(food, ".2f"))
print("Total After GST:", format(total, ".2f"))
print("Discount (20%):", format(discount, ".2f"))
print("Final Payable Amount:", format(final_amount, ".2f"))