import tkinter as tk  # Imports tkinter
from tkinter import *  # Imports all of tkinter
from tkinter import messagebox  # Imports messagebox
import _sqlite3  # Import sqlite3

productName = []  # Makes product name into list
productPrice = []  # Makes product price into list

storeWindow = tk.Tk()  # The main GUI
storeWindow.title("The Store")  # The name of the GUI
storeWindow.geometry('400x600')  # Provides Screen resolution for GUI

width, height = 400, 600  # Settings for the width and height
screen_width = storeWindow.winfo_screenwidth()  # Receives the screen width
screen_height = storeWindow.winfo_screenheight()  # Receives the screen height
x_cord = int((screen_width / 2) - (width / 2))  # Gets the screen width and divides by two
y_cord = int((screen_height / 2) - (height / 2))  # Gets the screen height and divides by two
storeWindow.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))


def receive_products():  # Receive products function
    product = open('Products', 'r')  # Open products.txt file where the products are
    product_names = []  # Places products as dictionary
    for item in product:
        product_names.append(item)  # Add product names to item

    for item in product_names:
        entry_divide = item.split(",")  # Splits the text file
        name = entry_divide[0]  # Name goes into 0
        price = entry_divide[1]  # Price goes into 1

        productName.append(name)  # Product names are added to name
        productPrice.append(price)  # Product prices are added to price

    print(productName)  # Displays product name
    print(productPrice)  # Displays product price


receive_products()


class MainStore:
    def show_store(self):  # The section where products are shown
        global storeWindow  # Global variable called StoreWindow
        storelbl_frame = LabelFrame(storeWindow, text="Store Items")  # # Label from show_store
        storelbl_frame.pack(fill="both", expand="yes", padx="18", pady="32", )

        storeitem_frame = Frame(storelbl_frame)  # Frames for product
        storeitem_frame.pack(padx="18", pady="32")

        for item in productName:  #
            namelist = productName.index(item)
            price_list = productPrice[namelist]
            price = ("£" + price_list)  # Adds £ symbol to prices

            item_frame = Frame(storeitem_frame, pady="15")  # frame for items
            item_frame.pack(fill="both", expand="yes")

            name_lbl = Label(item_frame, text=item, font=("Verdana", 12), fg="Blue")  # Name label configuration
            name_lbl.pack(side="left")

            price_label = Label(item_frame, text=price, font=('Verdana', 12), fg='red')  # Price label configuration
            price_label.pack(side='left')

            includecart_btn = Button(item_frame, text="Place in cart", font=('Verdana', 15),
                                     fg="darkred", bg="darkgrey",
                                     command=lambda i=item: includecart(i))
            includecart_btn.pack(side="right")  # Places product in cart button

        btntocart = Button(storeWindow, text=" View Cart", font=("Verdana", 15, "bold"),
                           fg="red", bg="white", cursor="hand2", command=cart)
        btntocart.pack(pady="6")  # Button for looking at cart


def cart():  # Cart function
    cart_window = Toplevel()  # TopLevel opens new frame
    cart_window.title("Shopping Basket")  # Cart windows title
    cart_window.geometry("400x500")  # Cart windows screen resolution

    cart_items = cart_function.getcart_products()  # gets function from variable

    cartitems_lblframe = LabelFrame(cart_window, text="Cart Items")  # Section where products in cart are shown
    cartitems_lblframe.pack(fill="both", expand="yes", padx="20", pady="10")

    cartitems_frame = Frame(cartitems_lblframe, padx=3, pady=3)  # Frame for cart items
    cartitems_frame.pack()

    pricecalculation = 0  # The default price
    index = 0
    for item in cart_items:
        namelist = productName.index(item)
        pricelist = productPrice[namelist]
        Price = ("£" + pricelist)  # Adds £ symbol to prices

        item_frame = Frame(cartitems_frame, pady="5")  # item frame
        item_frame.pack(fill="both", expand="yes")

        name_lbl = Label(item_frame, text=item, font=("Verdana", 12), fg="Blue")  # Name label configuration
        price_lbl = Label(item_frame, text=Price, font=('Verdana', 12), fg='red')  # Price label configuration
        includecart_btn = Button(item_frame, text="Delete", font=("Verdana", 13, "bold"), fg="red", bg="darkgrey",
                                 cursor="hand2", command=lambda i=index: deletecart(i, cart_window))
        # Remove product from cart button

        name_lbl.pack(side="left")  # Name label location
        price_lbl.pack(side="left")  # Price label location
        includecart_btn.pack(side="right")  # Button label location

        pricecalculation = pricecalculation + int(pricelist)  # Price calculation including product price
        index += 1

    checkout_frame = Frame(cart_window, pady="10")  # Checkout frame
    totalprice_lbl = Label(checkout_frame, text="Total Price : £ %s" % pricecalculation,
                           font=("Verdana", 14, "bold"), fg="#5495B3")
    totalprice_lbl.pack(side="left")  # Displays total price and location

    checkout_btn = Button(cart_window, text="Checkout", command=lambda: checkout(pricecalculation),
                          font=("Verdana", 10))
    checkout_btn.pack(side="bottom")  # Checkout button

    checkout_frame.pack()


def checkout(price):  # Checkout function
    checkout_window = Toplevel()  # TopLevel opens new frame
    checkout_window.title("Checkout")  # Checkout window title
    checkout_window.geometry("700x400")  # Checkout window screen resolution

    cart_items = cart_function.getcart_products()  # gets function from variable

    cartitems_lblframe = LabelFrame(checkout_window, text="Cart Items", width=10, height=20)
    cartitems_lblframe.pack(side="left", fill="y", expand=False, padx="7", pady="7")  # Lists item in cart

    cartitems_frame = Frame(cartitems_lblframe, padx=3, pady=3)
    cartitems_frame.pack()
    index = 0
    for item in cart_items:
        namelist = productName.index(item)
        pricelist = productPrice[namelist]
        Price = ("£" + pricelist)  # Adds £ symbol to prices

        item_frame = Frame(cartitems_frame, pady="5")  # Item frame
        item_frame.pack(fill="both", expand="yes")

        name_lbl = Label(item_frame, text=item, font=("Verdana", 12), fg="Blue")  # Name label configuration
        price_lbl = Label(item_frame, text=Price, font=('Verdana', 12), fg='red')  # Price label configuration

        name_lbl.pack(side="left")  # Name label location
        price_lbl.pack(side="left")  # Price label location

        index += 1

    checkout_frame = Frame(checkout_window, pady="10")  # Checkout frame
    totalprice_lbl = Label(checkout_window, text="Total Price : £ %s" % price,
                           font=("Verdana", 14, "bold"), fg="#5495B3")
    totalprice_lbl.pack(side="bottom")  # Displays cart price and location

    checkout_frame.pack()
    discount_label = tk.Label(checkout_window, text='Enter Discount Here', font=("Verdana", 14, "bold"), fg="#5495B3")
    discount_label.pack()
    discount_input = StringVar()  # Holds a string entered
    discount_entry = Entry(checkout_window, textvariable=discount_input)  # User inputs a discount code
    discount_entry.pack(pady=20)

    discounts_applied = Button(checkout_window, text="Apply Discount")  # Button to apply discount
    discounts_applied.pack(pady=20)

    deliveryoptions = [
        "Free Delivery (Free)",
        "Next Day Delivery (+£5)",
        "Store Collection (Free)"
    ]  # Options available for delivery

    variable = StringVar(checkout_window)  # Holds string for delivery
    variable.set(deliveryoptions[0])  # The default delivery option

    w = OptionMenu(checkout_window, variable, *deliveryoptions)  # Provides a dropdown menu
    w.pack()

    str_out = tk.StringVar(checkout_window)
    str_out.set("Output")  # Displays option chosen

    def my_show(*args):

        delivery_opt = variable.get()  # Receives chosen delivery option

        if delivery_opt == "Next Day Delivery (+£5)":
            new_price = price + 5  # Increases total price by £5 for selecting next day delivery
            totalprice_lbl["text"] = "Total Price : £ %s" % new_price
        elif delivery_opt == "Free Delivery":
            totalprice_lbl["text"] = "Total Price : £ %s" % price
        else:
            totalprice_lbl["text"] = "Total Price : £ %s" % price

    variable.trace('w', my_show)  # Follows the dropdown menu options with the chosen method

    bbt = Button(checkout_window, text="nextPage", command=lambda: details_page(discount_input))
    bbt.pack()


def details_page(discount_entry):  # Details function
    checkout_window = Toplevel()  # TopLevel opens new frame
    checkout_window.title("Payment")  # Continuation of Checkout window for payment
    checkout_window.geometry("700x400")  # Screen resolution
    discountcode_lbl = Label(checkout_window, text=discount_entry.get())  # Captures written discount code
    discountcode_lbl.grid(row=0, column=2)
    discount_lbl = Label(checkout_window, text="Discount code entered:", width=25)  # Displays written discount code
    discount_lbl.grid(row=0, column=1)

    name_card = tk.Label(checkout_window, text='Card Name:', width=25)  # Label for card name
    name_card.grid(row=1, column=1)

    namestring = StringVar()  # Holds a string entered
    name_entry = tk.Entry(checkout_window, textvariable=namestring)  # Textbox for card name
    name_entry.grid(row=1, column=2)

    card_num = tk.Label(checkout_window, text='Card Number:', width=25)  # Label for card number
    card_num.grid(row=2, column=1)

    cardnumstring = StringVar()  # Holds a string entered
    cardnum_enter = tk.Entry(checkout_window, textvariable=cardnumstring)  # Textbox for card number
    cardnum_enter.grid(row=2, column=2)

    card_secdisplay = tk.Label(checkout_window, text='Security Code(CVC):', width=25)  # Label for card CVC
    card_secdisplay.grid(row=3, column=1)

    cardCVCstring = StringVar()  # Holds a string entered
    cardsec_enter = tk.Entry(checkout_window, textvariable=cardCVCstring)  # Textbox for Card CVC
    cardsec_enter.grid(row=3, column=2)

    cardexp_display = tk.Label(checkout_window, text='Card expiry date:', width=25)  # Label for card expiry
    cardexp_display.grid(row=4, column=1)

    cardExpString = StringVar()  # Holds a string entered
    cardexp_enter = tk.Entry(checkout_window, textvariable=cardExpString)  # Textbox for card expiry
    cardexp_enter.grid(row=4, column=2)

    payment_btn = tk.Button(checkout_window, text="Receipt", font=("Verdana", 15, "bold"), fg="red", bg="white",
                            command=lambda: receipt(namestring, cardnumstring, cardCVCstring, cardExpString))
    payment_btn.grid(row=5, column=2)  # Button which takes user to receipt section


def receipt(nameoncard, cardnum, cardcvc, cardexp):
    receipt_window = Toplevel()  # TopLevel opens new frame
    receipt_window.title("Receipt")  # Receipt windows title
    receipt_window.geometry("400x500")  # Receipt windows screen resolution

    name = Label(receipt_window, text=nameoncard.get())  # Captures written discount code
    name.pack()

    cardnumber = Label(receipt_window, text=cardnum.get())  # Captures written discount code
    cardnumber.pack()

    cardsec = Label(receipt_window, text=cardcvc.get())  # Captures written discount code
    cardsec.pack()

    carddate = Label(receipt_window, text=cardexp.get())  # Captures written discount code
    carddate.pack()
    conn = _sqlite3.connect('transaction.db')  # Connect to database
    # c = conn.cursor()  # Creates database
    # c.execute(""" CREATE TABLE receipt (cardName text,
    #                                     cardNumber  integer,
    #                                     cardCVC integer,
    #                                     cardEXP text)""")  # Creates a table called Receipt

    c.executemany("""INSERT INTO receipt VALUES (:cardname, :cardnumber, :cardcvc, :cardexp)""",
                  {'cardname': nameoncard.get(),
                   'cardnumber': cardnum.get(),
                   'cardcvc': cardcvc.get(),
                   'cardexp': cardexp.get()})

    conn.commit()  # End connection
    conn.close()  # Close connection


def includecart(item=None):  # Append to cart function
    global cart_function
    cart_function.itemtocart(item)
    messagebox.showinfo(title="Done", message="Product %s has been included in cart !!" % item)


def deletecart(item_directory=None, cart_window=None):  # Remove from cart function
    global cart_function
    cart_function.itemfromcart(item_directory)
    messagebox.showinfo(title="success", message="Product has been removed from cart")
    cart_window.destroy()
    cart()


class Shopping:  # Shopping Cart class
    def __init__(self):
        self.items = []

    def itemtocart(self, item):  # Append to cart code
        self.items.append(item)
        print(self.items)

    def itemfromcart(self, item_directory):  # Remove from cart code
        self.items.pop(item_directory)

    def getcart_products(self):
        return self.items


conn = _sqlite3.connect('delivery.db')  # Connect to database
c = conn.cursor()  # Creates database
#  c.execute(""" CREATE TABLE deliveries (
#                                       delivery text,
#                                       price text)""")

many_delivery_options = [('Free Delivery', '0.00'),
                         ('Next-Day Delivery', '+5.00'),
                         ('Collect in Store', '0.00')
                         ]
# c.executemany("INSERT INTO deliveries VALUES (?,?)", many_delivery_options)

conn.commit()  # End connection
conn.close()  # Close connection

cart_function = Shopping()  # Cart Function equals to Shopping class
find = MainStore()
find.show_store()

storeWindow.mainloop()  # Ends program
