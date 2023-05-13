# This program uses a linked list to create polynomials and find the summation and product
# Takes input of integer n1 of the number of lines for polynomial 1
# Next n1 lines are the coeffecient value and the exponent attached to the x value for polynomial 1
# Takes input of integer n2 of the number of lines for polynomial 2
# Next n2 lines are the coeffecient value and the exponent attached to the x value for polynomial 2

import sys

class Link (object):
    def __init__ (self, coeff = 1, exp = 1, next = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__ (self):
        return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
    def __init__ (self):
         self.first = None

    # Inserts links in descending order of exponents
    def insert_in_order (self, coeff, exp):
        new_poly = Link(coeff, exp)
        prev = None
        current = self.first
        stop = False

        while (current != None and not stop):
            if current.exp < exp:
                stop = True
            else:
                prev = current
                current = current.next
        
        # If list is empty
        if (prev == None):

            new_poly.next = self.first
            self.first = new_poly
        else:
            new_poly.next = current
            prev.next = new_poly
    
    # Removes duplicate
    def remove_duplicates (self):
        removed_list = LinkedList()
        current = self.first
        if (current.next != None):
            while (current != None):
                sum_of_coeff = 0
                amt_to_move = 0
                tmp = current
                while (tmp != None and tmp.exp == current.exp):
                    amt_to_move += 1
                    sum_of_coeff += tmp.coeff
                    tmp = tmp.next
                if (sum_of_coeff != 0):
                    removed_list.insert_in_order(sum_of_coeff, current.exp)
                for i in range(amt_to_move):
                    current = current.next
            return removed_list

        else:
            return self

    # Add polynomial p to this polynomial and return the sum
    def add (self, p):
        sum_poly = LinkedList()
        currentP = self.first
        currentQ = p.first
        while (currentP != None or currentQ != None):
            if (currentP == None):
                sum_poly.insert_in_order(currentQ.coeff, currentQ.exp)
                currentQ = currentQ.next

            elif (currentQ == None):
                sum_poly.insert_in_order(currentP.coeff, currentP.exp)
                currentP = currentP.next

            elif (currentP.exp > currentQ.exp):
                sum_poly.insert_in_order(currentP.coeff, currentP.exp)
                currentP = currentP.next

            elif (currentP.exp < currentQ.exp):
                sum_poly.insert_in_order(currentQ.coeff, currentQ.exp)
                currentQ = currentQ.next

            elif (currentP.exp == currentQ.exp):
                coeffSum = currentP.coeff + currentQ.coeff
                sum_poly.insert_in_order(coeffSum, currentP.exp)
                currentP = currentP.next
                currentQ = currentQ.next
                
        return sum_poly.remove_duplicates()

    # Multiply polynomial p to this polynomial and return the product
    def mult (self, p):
        mult_list = LinkedList()
        if self.first == None:
            return p
        if p.first == None:
            return self
        poly_self = self.first
        while (poly_self != None):
            poly_p = p.first
            #multiply term in self by each term in p, then go to next term in self until no more
            while (poly_p != None):
                new_coeff = int(poly_self.coeff) * int(poly_p.coeff)
                new_exp = int(poly_self.exp) + int(poly_p.exp)
                mult_list.insert_in_order(new_coeff, new_exp)
                poly_p = poly_p.next
            poly_self = poly_self.next
        mult_list = mult_list.remove_duplicates()
        return (mult_list)

    # Create a string representation of the polynomial
    def __str__ (self):
        current = self.first
        full_poly_str = ''
        while (current.next != None):
            poly_str = '(' + str (current.coeff) + ', ' + str (current.exp) + ')' + ' + '
            full_poly_str += poly_str
            current = current.next
        poly_str = '(' + str (current.coeff) + ', ' + str (current.exp) + ')'
        full_poly_str += poly_str
        return full_poly_str

def main():
    # Read data from file poly.in from stdin
    num = sys.stdin.readline()
    num = int(num)
    poly1_list = []
    for i in range(num):
        poly = sys.stdin.readline().split()
        poly[0] = int(poly[0])
        poly[1] = int(poly[1])
        poly1_list.append(poly)

    space = sys.stdin.readline()

    num = sys.stdin.readline()
    num = int(num)
    poly2_list = []
    for i in range(num):
        poly = sys.stdin.readline().split()
        poly[0] = int(poly[0])
        poly[1] = int(poly[1])
        poly2_list.append(poly)
        
    # Create polynomial p
    p = LinkedList()
    for poly in poly1_list:
        p.insert_in_order(poly[0], poly[1])

    print('Polynomial 1: ', end= ' ')
    print(p)

    # Create polynomial q
    q = LinkedList()
    for poly in poly2_list:
        q.insert_in_order(poly[0], poly[1])

    print('Polynomial 2: ', end= ' ')
    print(q)

    # Get sum of p and q and print sum
    sum_poly = p.add(q)
    print()
    print('Summation of polynomials 1 and 2:', end=' ')
    print(sum_poly)

    # Get product of p and q and print product
    mult_poly = p.mult(q)
    print()
    print('Product of polynomials 1 and 2:', end=' ')
    print(mult_poly)

if __name__ == "__main__":
    main()