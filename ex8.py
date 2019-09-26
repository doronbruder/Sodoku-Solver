EMPTY_SET=[] # According to math rules an empty set is a set that is not possible to exist for some reasons
#In that exercise I'll represent an empty set as empty list "[]"

def is_empty_cell(board, lst):
    """This function finds the next empty-non zero place in the board"""
    BOARD_SIZE=len(board)

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if (board[row][col] == 0):
                lst[0] = row
                lst[1] = col
                return True
    return False


def used_in_row(board, row, num):
    """This function cahecks if the number in the current place exists twice or more in the same row"""
    BOARD_SIZE=len(board)

    for i in range(BOARD_SIZE):
        if (board[row][i] == num):
            return True
    return False


def used_in_col(board, col, num):
    """This function cahecks if the number in the current place exists twice or more in the same column"""

    BOARD_SIZE=len(board)

    for i in range(BOARD_SIZE):
        if (board[i][col] == num):
            return True
    return False



def used_in_sub_board(board, row, col, num):
    """This function cahecks if the current place is passed sub-borad rule"""

    SUB_BOARD_SIZE = int(len(board) ** 0.5)

    for i in range(SUB_BOARD_SIZE):
        # within the specified root(N)xroot(N) box matches the given number
        for j in range(SUB_BOARD_SIZE):
            if (board[i + row][j + col] == num):
                return True
    return False


def is_valid(board, row, col, num):
    """This function checks if the current place in the board is valid according sudoku rules"""
    # Check if 'num' is not already placed in current row,
    # current column and current root(N)*root(N) sub-board
    SUB_BOARD_SIZE = int(len(board) ** 0.5)

    return not used_in_row(board, row, num) and not used_in_col(board, col, num) and not\
        used_in_sub_board(board, row - row % SUB_BOARD_SIZE, col - col % SUB_BOARD_SIZE, num)
    # for Sudoku solution (non-duplication across rows, columns, and sub-boards)


def solve_sudoku(board):
    """This boolean function checks if a general N*N board sudoku game is solvable and if it is ,it solves it"""
    # 'lst' is a list that keeps the record of row and col in find_next_cell function
    lst = [0, 0]

    # If there is no empty(zero) location, we are done
    if (not is_empty_cell(board, lst)):
        return True

    # Assigning list values to row and col that we got from the above Function
    row = lst[0]
    col = lst[1]
    BOARD_SIZE=len(board)

    # consider digits 1 to N
    for num in range(1, BOARD_SIZE+1):

        # if it's valid so far
        if is_valid(board, row, col, num):

            # make tentative assignment
            board[row][col] = num

            # return, if everything is ok
            if (solve_sudoku(board)):
                return True

            # failure, try again
            board[row][col] = 0

    # if we got here so we'll backtrack
    return False



def print_k_subsets_helper(items, n, k, index, temp_lst, i):
    """This main recursive function to print all subsets with size k of the group 0...,n-1 """

    if (index == k):
        # We got a right size subset so we print it
        print(temp_lst)
        return


    if (i >= n):
        # Base case when no more elements left
        return

    # current is included
    temp_lst[index] = items[i]
    print_k_subsets_helper(items, n, k, index + 1, temp_lst, i + 1)

    # current is excluded
    print_k_subsets_helper(items, n, k, index, temp_lst, i + 1)



def print_k_subsets(n, k):
    """This function prints all subsets with size k of the group 0...,n-1"""

    if k==0:
        print(EMPTY_SET)
        return

    elif(n==0):
        return

    items=list(range(n)) # Set our main itmes list

    temp_lst = [0]*k # set our subset list

    print_k_subsets_helper(items, n, k, 0, temp_lst, 0) # Call the recursive helper function



def fill_k_subsets_helper(items, n, k, index, temp_lst, i,lst):
    """The main recursive function to fill an empty list with all subsets with size k of the group 0...,n-1 as lists"""

    if (index == k):
        # We got a subset so we add it to our list
        lst.append(temp_lst[:])
        return


    if (i >= n):
        # Base case when  no more elements left
        return

    # current is included
    temp_lst[index] = items[i]
    fill_k_subsets_helper(items, n, k, index + 1, temp_lst, i + 1,lst)

    # current is excluded,
    fill_k_subsets_helper(items, n, k, index, temp_lst, i + 1,lst)



def fill_k_subsets(n, k,lst):
    """This function fills an empty list with all subsets with size k of the group 0...,n-1 as lists"""
    if  n>=k:

        items=list(range(n)) # Set our main itmes list

        temp_lst = [0]*k # Set our subset list

        fill_k_subsets_helper(items, n, k, 0, temp_lst, 0,lst) # Call the recursive helper function

    elif(k==0):
        lst.append(EMPTY_SET)


def return_k_subsets_rec(n):
    """The main recursive function to return a list with all subsets with size 1 to n of the group 0...,n-1 as lists"""
    if n==0: # Base case when we delivered all possible subsets
        return [[]]
    lst1=return_k_subsets_rec(n-1)
    lst2=list()
    for subset in lst1:
        lst2.append(subset+[n-1])

    final_list=lst1 +lst2

    return  final_list


def return_k_subsets(n, k):
    """This function return list with all subsets with size k of the group 0...,n-1 as lists"""
    if k==0:
        return [EMPTY_SET]
    if k>n:
        return EMPTY_SET
    all_sizes_lst=return_k_subsets_rec(n)
    filtered_lst = filter_lst(all_sizes_lst, k)
    return filtered_lst


def filter_lst(all_sizes_lst, k):
    """This function filter the all sizes list and send the right sized sets to filtered final list"""
    filtered_lst = list()
    for subset in all_sizes_lst:
        if len(subset) == k:
            filtered_lst.append(subset)
    return filtered_lst


