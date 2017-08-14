from sets import Set

sudoku_table2 = [
' ',' ','8',' ',' ',' ',' ',' ','4',
' ',' ',' ','9','4',' ','3',' ',' ',
'5',' ',' ','1','3',' ',' ','9',' ',
' ','1','2',' ',' ',' ',' ',' ',' ',
' ','5','9',' ',' ',' ','4','8',' ',
' ',' ',' ',' ',' ',' ','5','3',' ',
' ','7',' ',' ','9','2',' ',' ','5',
' ',' ','1',' ','6','3',' ',' ',' ',
'8',' ',' ',' ',' ',' ','6',' ',' ',
]

sudoku_table = [
'9','3','8',' ',' ',' ',' ','1','4',
'1',' ','7','9','4',' ','3','5',' ',
'5',' ','4','1','3',' ',' ','9',' ',
' ','1','2',' ','8',' ',' ','6',' ',
' ','5','9',' ',' ',' ','4','8',' ',
' ','8','6',' ',' ','9','5','3',' ',
'6','7','3','8','9','2','1','4','5',
'2','4','1','5','6','3',' ','7',' ',
'8','9','5',' ',' ',' ','6','2','3',
]

def get_index (line, column):
  return (line-1)*9+(column-1)
  

def check_line(line, column, s):
  for i in xrange (1,9+1):
    remove_element(line, i, s)

def check_column(line, column, s):
  for i in xrange (1,9+1):
    remove_element(i, column, s)
  
def check_block(line, column, s):
  for (i,j) in mount_block(get_block(line, column)):
    remove_element(i, j, s)
  
def remove_element(line, column, s):
  element = sudoku_table[get_index(line, column)]
  if element.isdigit() and int(element) in s:
    s.remove(int(element))
  
def print_table(table):
  print '------------------'
  for i in xrange(1,9+1):
    line = '|'
    for j in xrange(1,9+1):
      line += table[get_index(i,j)] + ('|' if j%3 == 0 else ' ')
    print line
    if i%3 == 0:
      print ' -----+-----+----- '
      
def get_block(line, column):
  return (3*((line-1)//3) + ((column-1)//3)) + 1
def mount_block(block_index):
  block = []
  line = 3*((block_index-1)//3) + 1
  column = 3*((block_index-1)%3) + 1
  for i in xrange(0,3):
    for j in xrange(0,3):
      block += [(line+i, column+j)]
  return block
  
l = []
for i in xrange(1,9+1):
  for j in xrange(1,9+1):
    if sudoku_table[get_index(i, j)] == ' ':
      s = Set(xrange(1,9+1))
      check_line  (i, j, s)
      check_column(i, j, s)
      check_block (i, j, s)
      l += [ (i, j, s), ]
print l
for x in l:
  print x
for x in l:
  

