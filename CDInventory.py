#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# MYokus, 2021-Aug-29, Added Code to work with classes and objects
#------------------------------------------#

import pickle # module for handling binary files
import os.path # module for common pathname manipulation

# -- DATA -- #
strFileName = ''
lstOfCDObjects = []
save_FileName = 'CDInventory.dat'  # data storage file to save the data to

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        __str__(): Creates a string for CD attributes

    """
    # --Fields --#
    # -- Constructor -- #
    def __init__(self,ID, title, artist):
        # --Attributes -- #
        self.__cd_id = ID
        self.__cd_title = title
        self.__cd_artist = artist
    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, value):
        if type(value) == int:
            self.__cd_id = value
        else:
            raise Exception('Position needs to be integer!')

    @property
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, value):
        if type(value) == str:
            self.__cd_title = value
        else:
            raise Exception('Title needs to be string')

    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, value):
        if type(value) == str:
            self.__cd_artist = value
        else:
            raise Exception('Length needs to be string')
    # -- Methods -- #
    def __str__(self):
        return (str(self.cd_id) + ',' + self.cd_title + ',' + '(by: ' + self.cd_artist + ')')


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        read_Textfile(file_name, table): -> A list of CD objects
        read_file(file_name): -> A list of CD objects
        write_file(file_name, table): -> None
    """
    # --Fields --#
    # -- Constructor -- #
            # --Attributes -- #
    # -- Properties -- #
    # -- Methods -- #

    @staticmethod
    def read_Textfile(file_name, table):
        """Function to manage data ingestion from a text file to a list of objects

        Reads the data from a text file identified by file_name into a 2D table
        (list of objects) table one line in the file represents one object row in table.

        Args:
            file_name (string): name of the text file used to read the data from
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime

        Returns:
            None.
        """

        try:
            table.clear()  # this clears existing data and allows to load data from file
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',') # data type: list
                cdRow = CD(int(data[0]), data[1], data[2]) # data type: object
                table.append(cdRow) # list of objects
            objFile.close()
        except FileNotFoundError as e:
            print('Text file does not exist!')
            print('Build in error info:')
            print(type(e), e, e.__doc__, sep='\n')

    @staticmethod
    def read_file(file_name):
        """Function to manage data ingestion from a binary file to a list of objects

        Reads the data from a binary file identified by file_name into a 2D table
        (list of objects) table one line in the file represents one object row in table.

        Args:
            file_name (string): name of the binary file used to read the data from

        Returns:
            data (list of objects): 2D data structure (list of objects)
        """

        try:
            data = []
            with open(file_name, 'rb') as fileObj:
                data = pickle.load(fileObj)
            return data
        except FileNotFoundError as e:
            print('Binary file does not exist!')
            print('Build in error info:')
            print(type(e), e, e.__doc__, sep='\n')

    @staticmethod
    def write_file(file_name, table):
        """Function to save a 2D table (a list of objects) to file via pickle

        Saves the data in a file identified by file_name into a .dat file

        Args:
            file_name (string): name of binary file used to save the data to
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime

        Returns:
            None.
        """
        try:
            with open(file_name, 'wb') as fileObj:
                pickle.dump(table, fileObj)
        except FileNotFoundError as e:
            print('Binary file does not exist!')
            print('Build in error info:')
            print(type(e), e, e.__doc__, sep='\n')


# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output (User Interaction)

    properties:

    methods:
        print_menu(): -> Displays a menu of choices to the user
        menu_choice(): -> Gets user input for menu selection
        show_inventory(table): -> Displays current inventory table
        user_input(table): -> Ask user for new ID, CD Title, and Artist and creates a new object

    """

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('\nMenu\n\n[i] Display Current Inventory\n[a] Add CD\n[s] Save Inventory to file')
        print('[l] load Inventory from file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices i, a, s, l, or x

        """
        choice = ' '
        while choice not in ['i', 'a', 's', 'l', 'x']: # 'While not loop: executes the body of the loop until the condition for loop termination is met'
            choice = input('Which operation would you like to perform? [i, a, s, l or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row.__str__())
        print('======================================')

    @staticmethod
    def user_input(table):
        """ Ask user for new ID, CD Title, and Artist and creates a new object that contains CD record info

        Args:
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime.

        Returns:
            a list of CD objects
        """

        try:
            strID = input('Enter ID: ').strip()
            strTitle = input('What is the CD\'s title? ').strip()
            stArtist = input('What is the Artist\'s name? ').strip()
            cdInput = CD(int(strID), strTitle, stArtist) # data type: object
            table.append(cdInput) # data type: a list of objects
            return table
        except ValueError as e:
            print('That is not an integer!')
            print('Build in error info:')
            print(type(e), e, e.__doc__, sep='\n')


# -- Main Body of Script -- #

# 1. When program starts, read in the currently saved Inventory from the .dat file or .txt file
# Load data from file into a list of CD objects on script start
if os.path.isfile('CDInventory.dat'): # if "CDInventory.dat" exits, use function "read_file()"
    strFileName = 'CDInventory.dat' # binary file to read the data from
    lstOfCDObjects = FileIO.read_file(strFileName)
else:                                 # Else, use function "read_Textfile()"
    strFileName = 'CDInventory.txt' # text file to read the data from
    FileIO.read_Textfile(strFileName,lstOfCDObjects)


# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process display current inventory
    if strChoice == 'i':
        IO.show_inventory(lstOfCDObjects) # displays the current CD inventory
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        IO.user_input(lstOfCDObjects) # returns a list of CD objects
        print() # add a space
        IO.show_inventory(lstOfCDObjects) # displays the current CD inventory
    # 3.4 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects) # displays the current CD inventory
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.write_file(save_FileName, lstOfCDObjects) # saves the current CD inventory to binary file
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.5 process load inventory
    elif strChoice == 'l':
        if os.path.isfile('CDInventory.dat'): # if "CDInventory.dat" exits, use function "read_file()"
            strFileName = 'CDInventory.dat'
            lstOfCDObjects = FileIO.read_file(strFileName) # reads from binary file
            IO.show_inventory(lstOfCDObjects) # displays the current CD inventory
        else:                                 # Else, use function "read_Textfile()"
            strFileName = 'CDInventory.txt'
            FileIO.read_Textfile(strFileName,lstOfCDObjects) # reads from text file
    # 3.6 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')


