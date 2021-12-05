# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 11:40:15 2021

@author: Sahana Sreedhar
"""

def row_unused_digit(grid, valid_digit, i):
    for k in range(9):
        if grid[i][k] > 0:
            valid_digit[grid[i][k] - 1] = 0
            
def column_unused_digit(grid, valid_digit, j):
    for k in range(9):
        if grid[k][j] > 0:
            valid_digit[grid[k][j] - 1] = 0
            

def block_unused_digit(grid, valid_digit, i, j):
    if i<=2:
        if j<=2:
            
            for k in range(3):
                for l in range(3):
                    
                    if grid[k][l] > 0 :
                        valid_digit[grid[k][l] - 1] = 0
                    
            
        elif j<=5:
            
            for k in range(3):
                for l in range(3,6):
                    
                    if grid[k][l] > 0 :
                        valid_digit[grid[k][l] - 1] = 0
        else:
            for k in range(3):
                for l in range(6,9):
                    
                    if grid[k][l] > 0 :
                        valid_digit[grid[k][l] - 1] = 0
        
            
        
    
    elif i<=5:
        if j<=2:
            for k in range(3,6):
                for l in range(3):
                    
                    if grid[k][l] > 0 :
                        valid_digit[grid[k][l] - 1] = 0
                    
            
        elif j<=5:
            for k in range(3,6):
                for l in range(3,6):
                    
                    if grid[k][l] > 0 :
                        valid_digit[grid[k][l] - 1] = 0
        else:
            for k in range(3,6):
                for l in range(6,9):
                    
                    if grid[k][l] > 0 :
                        valid_digit[grid[k][l] - 1] = 0
        
            

    
    else:
        if j<=2:
            for k in range(6,9):
                for l in range(3):
                    
                    if grid[k][l] > 0 :
                        valid_digit[grid[k][l] - 1] = 0
                    
            
        elif j<=5:
            for k in range(6,9):
                for l in range(3,6):
                    
                    if grid[k][l] > 0 :
                        valid_digit[grid[k][l] - 1] = 0
        else:
            for k in range(6,9):
                for l in range(6,9):
                    
                    if grid[k][l] > 0 :
                        valid_digit[grid[k][l] - 1] = 0
                
       
            
    return valid_digit    
            


def possible_number(grid, i, j):
    
    valid_digit=[1,1,1,1,1,1,1,1,1]
    
    row_unused_digit(grid, valid_digit, i)
    column_unused_digit(grid, valid_digit, j)
    block_unused_digit(grid, valid_digit, i, j)
    ListToReturn = []
    
    for i in range(9):
        
        if valid_digit[i] == 1:
            
            ListToReturn.append(i+1)
    
    
    return ListToReturn


    
def best_cell(grid):
    
    counterVariable = 10
    ListToReturn = []
    
    for row in range(9):
        
        for col in range(9):
            
            if grid[row][col] == 0:
                
                valid_digit=[1,1,1,1,1,1,1,1,1]
                
                row_unused_digit(grid, valid_digit, row)
                column_unused_digit(grid, valid_digit, col)
                block_unused_digit(grid, valid_digit, row, col)
                
                numberOfOnes = valid_digit.count(1)
                
                
                
                if valid_digit.count(1) == 1:
                    
                    return [row,col,valid_digit]
                
                else:
                    
                    if counterVariable > numberOfOnes:
                        
                        counterVariable = numberOfOnes
                        
                        ListToReturn = [row,col,valid_digit]
                        
    return ListToReturn
    
def solve_sudoku(grid):
    
    bestCellInTheGrid = best_cell(grid)
    
    if len(bestCellInTheGrid) != 0:
        
        for i in range(9):
            
            if bestCellInTheGrid[2][i] == 1:
                
                grid[bestCellInTheGrid[0]][bestCellInTheGrid[1]] = i+1
                
                solve_sudoku(grid)         
    return grid

                
def sudoku2str(printGrid):
    
      print('Solution For Your Sudoku is')
      print('-------------------------------------------------')   
      spacing = ' '
      
      for row in range(len(printGrid)):  
          convertToString = '' 
          if row == 3 : 
              print('-------------------------------------------------') 
          elif row == 6:
              print('-------------------------------------------------')
              
          for col in range(len(printGrid[row])):
              if col ==0 :  
                  if printGrid[row][col] == 0:     
                      convertToString = convertToString + '|'  + spacing * 3  + '_'    
                  else:   
                      convertToString = convertToString + '|'  + spacing * 3  + str(printGrid[row][col])  
                      
              elif  col ==3 or col == 6:
                    if printGrid[row][col] == 0: 
                      convertToString = convertToString + spacing * 3 + '|'  + spacing * 3  + '_'
                    else:   
                        convertToString = convertToString + spacing * 3 + '|'  + spacing * 3  + str(printGrid[row][col])
                    
              elif col == 8:
                  if printGrid[row][col] == 0:
                      convertToString = convertToString + spacing * 3 + '_' +  spacing * 3 + '|'
                  else:
                      convertToString = convertToString + spacing * 3 + str(printGrid[row][col]) +  spacing * 3 + '|'

              else:    
                  if printGrid[row][col] == 0:
                      convertToString = convertToString + spacing * 3 + '_'
                  else:
                      convertToString = convertToString + spacing * 3 + str(printGrid[row][col])
          print(convertToString)
          
      print('-------------------------------------------------')                
                

valid_digit=[1,1,1,1,1,1,1,1,1]

           
grid_wiki =   [[5, 3, 0, 0, 7, 0, 0, 0, 0],
               [6, 0, 0, 1, 9, 5, 0, 0, 0],
               [0, 9, 8, 0, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 6, 0, 0, 0, 3],
               [4, 0, 0, 8, 0, 3, 0, 0, 1],
               [7, 0, 0, 0, 2, 0, 0, 0, 6],
               [0, 6, 0, 0, 0, 0, 2, 8, 0],
               [0, 0, 0, 4, 1, 9, 0, 0, 5],
               [0, 0, 0, 0, 8, 0, 0, 7, 9]]

finalGrid = solve_sudoku(grid_wiki)

sudoku2str(finalGrid)


#best_cell(grid_wiki)
#possible_number(grid_wiki, 0, 2)
#block_unused_digit(grid_wiki,valid_digit,0,0) 
