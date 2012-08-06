#mainmenu
from time import gmtime, strftime

#cashier
def cashier():
	from time import gmtime, strftime

	while True: 
		response = raw_input('Start Transaction? Enter Y or N > ')
		if (response == 'Y' or response == 'y'):
			print '\nSerendipity Booksellers: '
			print '     Cashier module\n'
			print 'Date: ', strftime("%Y-%m-%d %H:%M:%S", gmtime())

			num_book = int(raw_input('Quantity of Book: '))
			isbn_book = raw_input('ISBN: ')
			title_book = raw_input('Title: ')
			price_book = float(raw_input('Price: '))
			total = num_book * price_book
			subtoral = total
			tax = total * 0.06
			amount = total - tax

			print '\nSerendipity Booksellers\n\nDate:', strftime("%Y-%m-%d %H:%M:%S", gmtime()),
			print '''
			\n\n
			Qty:   %d\t\n
			ISBN:  %s\t\n
			Title: %s\t\n
			Price: %6.2f\t\n
			Total: %6.2f
			'''%(num_book, isbn_book, title_book, price_book, total)
			print'''
				\tSubtoral: %6.2f
				Tax:      %6.2f
				Pay:      %6.2f
				\n
				''' %(total, tax, amount)
		
		elif (response == 'N' or response == 'n'):
			print 'You exit Cashier Module. Bye!\n'
			main()
			break
		else: 
			print 'Please enter Y or N'

#invmenu
def lookupBook():
	pass

def addBook():
	pass

def editBook():
	pass
	
def deleteBook():
	pass

def invMenu():
	print'''		
			Serendipity Booksellers
			Inventory Database\n
		       1. Look up a Book
		       2. Add a Book
		       3. Edit a book's Record
		       4. Delete a Book
		       5. Return to the Main Menu\n'''
		
	while True:
		n = raw_input('Enter your choice: ')
		if n == '1':
			print '\nLook Up a Book selected\n'
			lookupBook()
		elif n == '2':
			print '\nAdd a Book selected\n'
			addBook()
		elif n == '3':
			print '\nEdit a Book selected\n'	
			editBook()
		elif n == '4':
			print '\nDelete a book selected\n'
			deleteBook()
		elif n == '5':
			main()
			break
		else:
			print 'Please enter a number in the range 1-5\n'
			
#bookinfo
def bookInfo():
	print'''		
				Serendipity Booksellers
				   Book Information\n
	ISBN:
	Title:
	Author:
	Publisher:
	Date Added:
	Quantity-on-Hand:
	Wholesale Cost:
	Retail Price:'''
	
#reports
def repListing():
	pass

def repWholesale():
	pass
	
def repRetail():
	pass

def repQty():
	pass
	
def repCost():
	pass

def repAge():
	pass

def reports():
	print'''		
				Serendipity Booksellers
					   Reports\n
				1. Inventory Listing
				2. Inventory Wholesale Value
				3. Inventory Retail Value
				4. Listing by Quantity
				5. Listing by Cost
				6. Listing by Age
				7. Return to the main menu\n'''
			
	while True:
		n = raw_input('Enter your choice: ')
		if n == '1':
			print '\nInventory Listing selected\n'
			repListing()
		elif n == '2':
			print '\nInventory Wholesale Value selected\n'
			repWholesale()
		elif n == '3':
			print '\nInventory Retail Value selected\n'	
			repRetail()
		elif n == '4':
			print '\nListing by Quantity selected\n'
			repQty()
		elif n == '5':
			print '\nListing by Cost selected\n'
			repCost()
		elif n == '6':
			print '\nListing by Age selected\n'
			repAge()
		elif n == '7':
			main()
			break
		else:
			print 'Please enter a number in the range 1-7\n'
	
def main():
	print '''\nSerendipity Booksellers\n
	MAIN MENU\n
	1. Cashier Module
	2. Inventory Database Module
	3. Report Module
	4. Exit\n'''

	while True:
		n = raw_input('Enter your choice: ')
		if n == '1':
			print '\nCASHIER MENU\n'
			cashier()
		elif n == '2':
			print '\nINVENTORY MENU\n'
			invMenu()
		elif n == '3':
			print '\nREPORTS MENU\n'
			reports()
		elif n == '4':
			print '\nYou exit the program. Bye!\n'
			exit()
		else: 
			print 'Please enter a number in the range 1-4\n'
			
if __name__ == "__main__":
    main()