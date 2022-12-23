# laboratorio 7 : FORZA 4
# creazione del gioco forza 4
# utente vs utente

"""
Gettoni per un copia-incolla veloce
○ vuoto
● giocatore 1
◍ giocatore 2
Creazione di
"""

# creazione classe giocatore
# @parametri : nome e tipo di pallino
class Giocatore:
    def __init__(self,nome,pallino):
        self.nome=nome
        self.pallino=pallino
    def __repr__(self):
        return f'{self.pallino} {self.nome} {self.pallino}' #formattazione di stampa
    
#Creazione di una matrice 6x8 con inizializzazione di tutti gli elementi:
def inizializzazione_board(cells):
    for row in range (6): #ciclo tutte le righe
        cells.append([]) #aggiungo una riga. Una riga è una lista di elementi
        for col in range (8):
            cells[row].append("○") #aggiungo un elemento alla riga

#Visualizza la plancia di gioco aggioranta
# @input matrice 6x8 della plancia di gioco
def visualizzazione_board(board):
    print("\n")
    for i in range(6):
        print("  ".join(board[i]))
    print("0  1  2  3  4  5  6  7") # numero delle colonne
    print("\n")

# inizializzazione gioco e
# creazione giocatore 1 e giocatore 2 di classe Giocatore
# @output: lista: [giocatore 1,giocatore 2]
def inizio_gioco():
    print("Dimensione della board:\n\tRighe: 6\n\tColonne:8\nDati dei giocatori:") # inizializzazione gioco
    nome1=input("Inserire il nome del giocatore 1: ")
    pallino1=input(f'Scegliere con che pallino vuole giocare {nome1}:\n0. pieno: ●\n1. strisce: ◍\n')
    controllo=False
    while(not controllo): # assegno il pallino al giocatore (controllando che l'input sia valido)
        controllo=True
        if(pallino1=="0" or pallino1=="pieno"):
            pallino1="●"
            pallino2="◍"
        elif(pallino1=="1" or pallino1=="strisce"):
            pallino1="◍"
            pallino2="●"
        else:
            controllo=False
            pallino1=input("Inserimento non valido, riprova: ")
    nome2=input("Inserire il nome del giocatore 2: ")
    giocatore1=Giocatore(nome1,pallino1)
    giocatore2=Giocatore(nome2,pallino2)
    print(f'giocatore 1: {str(giocatore1)}\ngiocatore 2: {str(giocatore2)}') # visualizzo i 2 giocatori
    return [giocatore1,giocatore2]

# trovo la prima (dal basso verso l'alto) riga libera in cui inserire il pallino
# @input plancia attuale e colonna di inserimento
def ricerca_riga(plancia,colonna):
    riga=5
    while(plancia[riga][colonna]!="○"):
        riga-=1
    return riga

# turno di gioco
# @input plancia, giocatore
# @output plancia aggiornata e cella cambiata
def turno(plancia,giocatore):
    colonna=input(f'{str(giocatore)} è il tuo turno\nIn che colonna vuoi inserire il gettone? ') #inserimento della colonna
    controllo= False
    while(not controllo): # controllo input valido
        if(colonna.isnumeric()): # controllo che sia numerico
            colonna=int(colonna)
            if(colonna>=0 and colonna<=7): # controllo che sia sensato per la plancia
                controllo=True
        else:
            input("Inserimento non valido, riprova: ")       
    if(plancia[0][colonna] != "○"): # controllo che la colonna non sia piena
        colonna=input("Colonna piena, cambia colonna: ")
        controllo= False
        while(not controllo): # controllo input valido
                if(colonna.isnumeric()): # controllo che sia numerico
                    colonna=int(colonna)
                    if(colonna>=0 and colonna<=7): # controllo che sia sensato per la plancia
                        controllo=True
                else:
                    input("Inserimento non valido, riprova: ") 
    riga=ricerca_riga(plancia,colonna) # cerco la riga vuota
    plancia[riga][colonna]=giocatore.pallino # inserisco il pallino
    return plancia,[riga,colonna]

#cambia una cella della plancia con delle "X"
# @input plancia e posizione (lista [riga,colonna]) della cella da cambiare
def inserimento_X(plancia,posizione):
    plancia[posizione[0]][posizione[1]]="X"
    
# controllo se il giocatore ha fatto 4 palline di fila (in veritcale, orizzontale o diagonale)
# @input plancia, cella cambiata nell'ultime inserimento e che giocatore l'ha fatto
# @output se il giocatore ha vinto (True) o no (False)
# @output inoltre se qualcuno ha vinto la plancia è cambiata inserendo delle "X" dove ci sono i 4 consecutivi
def controllo_vittoria(lista,cella_cambiata,giocatore):
    contatore=1 # quante palline di fila
    i=0
    posizione=cella_cambiata.copy() # lista [riga,colonna]
    if(posizione[0]<=2): # controllo in verticale
        posizione[0]+=1 #inizio a controllare da quello sotto 
        while(contatore<4 and lista[posizione[0]][posizione[1]]==giocatore.pallino):
            posizione[0]+=1
            contatore+=1
        if contatore==4: # se c'è sono 4 in totale  
            while(i<=3):
                posizione[0]-=1
                inserimento_X(lista,posizione)
                i+=1
            return True  
    contatore=1 # controllo orizzontale
    posizione=cella_cambiata.copy() # ristabilisco la posizione iniziale
    if(cella_cambiata[1]>=1 and lista[cella_cambiata[0]][cella_cambiata[1]-1]!=giocatore.pallino): # parto da sx della pallina
        if(posizione[1]<=4): # se a sx non c'è il pallino giusto vado tutto a dx
            posizione[1]+=1
            while(contatore<4 and lista[posizione[0]][posizione[1]]==giocatore.pallino):
                posizione[1]+=1
                contatore+=1
            if contatore==4: # se c'è sono 4 in totale  
                while(i<=3):
                    posizione[1]-=1
                    inserimento_X(lista,posizione)
                    i+=1                
                return True
    elif(cella_cambiata[1]<=6 and lista[cella_cambiata[0]][cella_cambiata[1]+1]!=giocatore.pallino): # a sx c'è il pallino giusto controllo a dx
        if(posizione[1]>=3): # se a dx non c'è il pallino giusto vado tutto a sx sapendo già l'informazione del primo if
            posizione[1]=cella_cambiata[1]-2 # ristabilisco colonna iniziale
            contatore=2 # ho già 1 a sx
            while(contatore<4 and lista[posizione[0]][posizione[1]]==giocatore.pallino):
                posizione[1]-=1
                contatore+=1
            if contatore==4: # se c'è sono 4 in totale  
                while(i<=3):
                    posizione[1]+=1
                    inserimento_X(lista,posizione)
                    i+=1                
                return True           
    else: # c'è sia a dx che a sx
        contatore=3 
        if(cella_cambiata[1]>=2 and lista[cella_cambiata[0]][cella_cambiata[1]-2]==giocatore.pallino): # controllo 2 a sx
            posizione[1]=cella_cambiata[1]+1 # ristabilisco colonna iniziale partendo da 1 a dx
            while(i<=3):
                inserimento_X(lista,posizione)
                posizione[1]-=1
                i+=1            
            return True #  ce ne sono 2 a sx ed 1 a dx
        elif(cella_cambiata[1]<=5 and lista[cella_cambiata[0]][cella_cambiata[1]+2]==giocatore.pallino): # se non c'è 2 a sx controllo 2 a dx
            posizione[1]=cella_cambiata[1]-1 # ristabilisco colonna iniziale partendo da 1 a sx
            while(i<=3):
                inserimento_X(lista,posizione)
                posizione[1]+=1
                i+=1             
            return True # ce ne sono 1 a sx e 2 a dx
    
    # nelle diagonali escludo gli angoli dai controlli
    if((5-cella_cambiata[0])+cella_cambiata[1]>=3 and (5-cella_cambiata[0])+cella_cambiata[1]<=9): # controllo diagonale alto sx basso dx
        contatore=1
        posizione=cella_cambiata.copy()
        if(cella_cambiata[0]>=1 and cella_cambiata[1]>=1 and lista[cella_cambiata[0]-1][cella_cambiata[1]-1]!=giocatore.pallino): # parto in alto a sx della pallina
            if(cella_cambiata[0]<=2 and cella_cambiata[1]<=4): # se in alto a sx non c'è il pallino giusto vado tutto in basso a dx
                posizione[0]+=1
                posizione[1]+=1
                while(contatore<4 and lista[posizione[0]][posizione[1]]==giocatore.pallino):
                    posizione[0]+=1
                    posizione[1]+=1
                    contatore+=1
                if contatore==4: # se c'è sono 4 in totale                   
                    while(i<=3):
                        posizione[0]-=1
                        posizione[1]-=1                        
                        inserimento_X(lista,posizione)
                        i+=1                    
                    return True
        elif(cella_cambiata[0]<=4 and cella_cambiata[1]<=6 and lista[cella_cambiata[0]+1][cella_cambiata[1]+1]!=giocatore.pallino): # in alto a sx c'è il pallino giusto controllo in basso a dx
            if(cella_cambiata[0]>=3 and cella_cambiata[1]>=3): # se in basso a dx non c'è il pallino giusto vado tutto in alto a sx sapendo già l'informazione del primo if
                posizione[0]=cella_cambiata[0]-2 # ristabilisco colonna iniziale
                posizione[1]=cella_cambiata[1]-2 
                contatore=2 # ho già 1 in alto a sx
                while(contatore<4 and lista[posizione[0]][posizione[1]]==giocatore.pallino):
                    posizione[0]-=1
                    posizione[1]-=1
                    contatore+=1
                if contatore==4: # se c'è sono 4 in totale  
                    while(i<=3):
                        posizione[0]+=1
                        posizione[1]+=1
                        inserimento_X(lista,posizione)
                        i+=1                
                    return True           
    else: # c'è sia in basso a dx che in alto a sx
        contatore=3 
        if(cella_cambiata[0]>=2 and cella_cambiata[1]>=2 and lista[cella_cambiata[0]-2][cella_cambiata[1]-2]==giocatore.pallino): # controllo 2 in alto a sx
            posizione[0]=cella_cambiata[0]+1 # ristabilisco colonna iniziale partendo da 1 in basso a dx
            posizione[1]=cella_cambiata[1]+1 
            while(i<=3):
                inserimento_X(lista,posizione)
                posizione[0]-=1
                posizione[1]-=1
                i+=1            
            return True #  ce ne sono 2 in alto a sx ed 1 in basso a dx
        elif(cella_cambiata[0]<=3 and cecella_cambiata[1]<=5 and lista[cella_cambiata[0]+2][cella_cambiata[1]+2]==giocatore.pallino): # se non c'è 2 in alto a sx controllo 2 in basso a dx
            posizione[0]=cecella_cambiata[0]-1
            posizione[1]=cella_cambiata[1]-1 # ristabilisco colonna iniziale partendo da 1 in alto a sx
            while(i<=3):
                inserimento_X(lista,posizione)
                posizione[0]+=1
                posizione[1]+=1
                i+=1             
            return True # ce ne sono 1 in alto a sx e 2 in basso a dx        
        
    if(cella_cambiata[0]+cella_cambiata[1]>=3 and cella_cambiata[0]+cella_cambiata[1]<=9): # controllo diagonale alto dx basso sx
        contatore=1
        posizione=cella_cambiata.copy()
        if(cella_cambiata[0]>=1 and cella_cambiata[1]<=6 and lista[cella_cambiata[0]-1][cella_cambiata[1]+1]!=giocatore.pallino): # parto in alto a dx della pallina
            if(cella_cambiata[0]<=2 and cella_cambiata[1]>=3): # se in alto a dx non c'è il pallino giusto vado tutto in basso a sx
                posizione[0]+=1
                posizione[1]-=1
                while(contatore<4 and lista[posizione[0]][posizione[1]]==giocatore.pallino):
                    posizione[0]+=1
                    posizione[1]-=1
                    contatore+=1
                if contatore==4: # se c'è sono 4 in totale                   
                    while(i<=3):
                        posizione[0]-=1
                        posizione[1]+=1                        
                        inserimento_X(lista,posizione)
                        i+=1                    
                    return True
        elif(cella_cambiata[0]<=4 and cella_cambiata[1]>=1 and lista[cella_cambiata[0]+1][cella_cambiata[1]-1]!=giocatore.pallino): # in alto a dx c'è il pallino giusto controllo in basso a sx
            if(cella_cambiata[0]>=3 and cella_cambiata[1]<=4): # se in basso a sx non c'è il pallino giusto vado tutto in alto a dx sapendo già l'informazione del primo if
                posizione[0]=cella_cambiata[0]-2 # ristabilisco colonna iniziale
                posizione[1]=cella_cambiata[1]+2 
                contatore=2 # ho già 1 in alto a dx
                while(contatore<4 and lista[posizione[0]][posizione[1]]==giocatore.pallino):
                    posizione[0]-=1
                    posizione[1]+=1
                    contatore+=1
                if contatore==4: # se c'è sono 4 in totale  
                    while(i<=3):
                        posizione[0]-=1
                        posizione[1]+=1
                        inserimento_X(lista,posizione)
                        i+=1                
                    return True           
        else: # c'è sia in alto a dx che in basso a sx
            if(cella_cambiata[0]>=2 and cella_cambiata[1]<=5 and lista[cella_cambiata[0]-2][cella_cambiata[1]+2]==giocatore.pallino): # controllo 2 in alto a dx
                posizione[0]=cella_cambiata[0]+1 # ristabilisco colonna iniziale partendo da 1 in basso a sx
                posizione[1]=cella_cambiata[1]-1 
                while(i<=3):
                    inserimento_X(lista,posizione)
                    posizione[0]-=1
                    posizione[1]+=1
                    i+=1            
                return True #  ce ne sono 2 a in alto a dx ed 1 in basso a sx
            elif(cella_cambiata[0]<=3 and cecella_cambiata[1]>=2 and lista[cella_cambiata[0]+2][cella_cambiata[1]-2]==giocatore.pallino): # se non c'è 2 in alto a sx controllo 2 in basso a dx
                posizione[0]=cecella_cambiata[0]-1
                posizione[1]=cella_cambiata[1]+1 # ristabilisco colonna iniziale partendo da 1 in alto a dx
                while(i<=3):
                    inserimento_X(lista,posizione)
                    posizione[0]+=1
                    posizione[1]-=1
                    i+=1             
                return True #  ce ne sono 1 a in alto a dx ed 2 in basso a sx
    return False # ritorno falso in caso non arrivi a nessuno degli altri return

# programma principale
def main():
    
    plancia=[]
    vittoria=False # controllo per la vittoria
    inizializzazione_board(plancia) # inizializzo plancia  
    lista_giocatori=inizio_gioco() # lista dei 2 giocatori di classe Giocatore
    print("ecco la plancia: ")
    visualizzazione_board(plancia)
    turno_corrente=0
    cambio=[] # cella cambiata
    while(not vittoria): # quando qualcuno vince dopo le apposite stampe si esce dal while ed il programma termina
        if turno_corrente%2==0: # se siamo in un turno pari è il turno di giocatore 1
            indice_giocatore=0
        else:
            indice_giocatore=1    
        plancia,cambio=turno(plancia,lista_giocatori[indice_giocatore]) # svolgo il turno (inserimento pallino)
        vittoria=controllo_vittoria(plancia,cambio,lista_giocatori[indice_giocatore]) # controllo se il giocatore ha vinto
        visualizzazione_board(plancia) # visualizzo la plancia (cambiata in caso di vittoria)
        if(vittoria):
            print(f'Complimenti, {lista_giocatori[indice_giocatore]} hai vinto!') # in caso di vittoria stampo il messaggio
        turno_corrente+=1
    
main()