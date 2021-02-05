import pygame

class MacGyver(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.ligne = x
        self.colonne = y 
        self.tuplemacgyver = (self.ligne, self.colonne)
        self.listedobjet = []
        self.image = pygame.image.load("MacGyver.png")
        


    """ def okinput(self, userchoice):
        inputok = False
        if len(userchoice) == 1 and userchoice == "d" or userchoice =="l"  or userchoice == "u" or userchoice == "r":
            inputok = True
        return True """

    def lecturedelinput(self, userchoice):
        for event in userchoice:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    return (self.ligne + 1, self.colonne)
                elif event.key == pygame.K_RIGHT:
                    return (self.ligne, self.colonne +1)
                elif event.key == pygame.K_LEFT:
                    return (self.ligne, self.colonne -1)
                elif event.key == pygame.K_UP:
                    return (self.ligne -1, self.colonne)

    def chekmove(self, variable, passage, listedobjetlabyrinthe, gardien):
        move = False
        
        for element in listedobjetlabyrinthe:
            if element.tupleposition == variable:
                objettrouver = element
                self.attrapelobjet(passage, objettrouver, listedobjetlabyrinthe) 
        if variable in passage or variable == gardien:
            move = True
        else: #on aime pas les exceptions seul 
            print("merci de recommencer")
        return move

    def movemacgyver(self, userchoice, passage, gardien, listedobjetlabyrinthe, boleen, listegardien):
  
        
        positionaregarder = self.lecturedelinput(userchoice)
        if self.chekmove( positionaregarder, passage, listedobjetlabyrinthe, gardien):
            passage.append((self.ligne, self.colonne))
            self.ligne = positionaregarder[0]
            self.colonne = positionaregarder[1] 
            if not self.findepartie(gardien, listegardien, passage):
                passage.remove((self.ligne, self.colonne))
            else:
                boleen = True
            
        else:
            print("merci de recommencer")
   
        return boleen

    def findepartie(self, gardien, listegardien, passage):
        findepartie = False
        if (self.ligne, self.colonne) == (gardien):
            if len(self.listedobjet) == 3:
                print("Macgyver endort le gardien avec l'Ether")
                print("Bravo Macgyver a réussi à s'échapper")
            else:
                print("Il manque des objets, le gardien s'en prend à Macgyver. Fin de partie.")
            findepartie = True 
        return findepartie
        
    def attrapelobjet(self, passage, objettrouver, listedobjetlabyrinthe):
        passage.append(objettrouver.tupleposition)
        self.listedobjet.append(objettrouver)
        listedobjetlabyrinthe.remove(objettrouver) #un paramètre n'est qu'une copie
        print("Macgyver a ramassé", objettrouver.nomdelobjet, ".") 
    
    def compteurdobjet(self):
        if len(self.listedobjet) == 1:
            print("Macgyver a", len(self.listedobjet), "objet.")
        else: 
            print("Macgyver a",  len(self.listedobjet), "objets.")

        

        


            

      

        


