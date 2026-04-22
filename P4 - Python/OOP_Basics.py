class Player:
    # Constructor: Note the double underscore for PRIVATE attributes 
    def __init__(self, InputPlayerID):
        self.__PlayerID = InputPlayerID # PRIVATE STRING 
        self.__Score = 0                # PRIVATE INTEGER 
        self.__Category = "Not Qualified" # PRIVATE STRING 

    # --- GETTERS (Accessor Methods) --- 
    def GetScore(self):
        return self.__Score
    
    def GetCategory(self):
       return self.__Category
    
    def GetPlayerID(self):
       return self.__PlayerID

    # --- SETTERS (Mutator Methods) with Validation --- 
    def SetPlayerID(self):
       valid = False
       InputID = input("Enter the new Player ID: ")

       while not valid:
          # Validation: Length check is a frequent exam task 
          if 4 <= len(InputID) <= 15:
             valid = True
             self.__PlayerID = InputID
          else:
             InputID = input("Invalid! Must be 4-15 chars. Re-enter: ")

    def SetScore(self, ScoreInput):
       # Range check validation 
       if 0 <= ScoreInput <= 150:
          self.__Score = ScoreInput
          self.UpdateCategory() # Update category whenever score changes 
          return True
       else:
          print("Invalid Score!")
          return False
       
    def UpdateCategory(self):
       # Logic based on attributes 
       if self.__Score > 120:
          self.__Category = "Advanced"
       elif self.__Score > 80:
          self.__Category = "Intermediate"
       elif self.__Score >= 50:
          self.__Category = "Beginner"
       else:
          self.__Category = "Not Qualified"

# --- Main Program / Practical Application --- 
def RunGame():
   ID = input("Enter Player ID: ")
   Score = int(input("Enter Score: "))

   # Instantiation: Creating an Object 
   NewPlayer = Player(ID)
   if NewPlayer.SetScore(Score):
       print(f"Player {NewPlayer.GetPlayerID()} is {NewPlayer.GetCategory()}")

RunGame()