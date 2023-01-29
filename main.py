import os 


# Potential Update 1: will include dynamically deleting any folder the user puts in - Add a function + user input
# Potentai lupdate 2: Update 2 deleting the entire folder selected - Add a function 


# Delete a selected folder in the Downloads folder 
file_path = 'Insert path to folder here' # Paste the URL to the folder here

Question1 = input('Do you want to delete 1 specific folder? Yes or No? ')

if Question1 == 'yes':

    print(file_path)

    if os.path.isfile(file_path):
        os.remove(file_path)
        print('File has successfully been deleted')
    else:
        print('This file does not exist')

elif Question1 == 'no':

    Question2 = input('Do you want to delete several selected files? Yes or No? ')

    if Question2 == 'yes':

         print('Do the deleting of specific files') 
         
    elif Question2 == 'no':
        
        Question3 = input('Do you want to delete all the files in the folder? Yes or No? ')

        if Question3 == 'yes':

            print('Delete the entire folder') 
        else:

            print('do something')


    

    
    








