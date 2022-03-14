import tkinter as tk
import os
import math

class MainScreen:
    def __init__(self):
        
        # Sensitive data
        MANAGER_MAIL="pierreemmanueldumont@gmail.com"
        MANAGER_MAIL_APP_PASSWORD="yuusjrpteqiglfog"
        
        
        # Constants
        self.LENGTH = self.Window.winfo_screenwidth()
        self.HEIGHT = self.Window.winfo_screenheight()-70
        self.ERROR='#ffefd8'
        self.OK='#ffefd8'
        self.BUTTON='#ff7f50'
        self.CLICK='#7986CB'
        self.BACKGROUND='#ffefd8'
        self.TITLE_FONT='Rockwell  90'
        self.FONT='Rockwell'
        self.FONTSIZE=float(self.LENGTH)*float(self.HEIGHT)/(1920*1080)
        
        
        # Variables
        self.Window=tk.Tk()
        self.Window.title("TOMBOLA")
        self.Window.resizable(width=True, height=True)
        self.Window.state("zoomed")
        self.canvas = tk.Canvas(self.Window, width= self.LENGTH, height= self.HEIGHT, bg=self.BACKGROUND)
        self.canvas.pack()
        self.state='Menu'
        
        ## Lists
        self.reg=[]
        self.listenom=[]
        self.listelot=[]
        self.listemail=[]
        self.listeinfo=[] 
        self.registreattente=[]
        self.registrepermanent=[]
        self.listecase=[]
        
        kL=L/1536
        kH=H/864
        nbcase=0
        
        # Tkinter variables
        txtnbcase=tk.StringVar()
        txtnom=tk.StringVar()
        txtprenom=tk.StringVar()
        txtmail=tk.StringVar()
        txtprix=tk.StringVar()
        optionmail=tk.StringVar()
        optionmdp=tk.StringVar()
        optioncodevalidation=tk.StringVar()
        txtcase=tk.StringVar()
        txtquantite=tk.StringVar()
        txtnomlot=tk.StringVar()
        
        cursor='rien'



        carre=math.ceil(math.sqrt(nbcase))




    def folderInitialisation(self):
        if not os.path.exists('TIPE'):
            os.mkdir('TIPE')
            open("TIPE/informations.txt", "w")
            open("TIPE/lot.txt", "w")
            open("TIPE/resultats.txt", "w")
            open("TIPE/sauvegarde.txt", "w")
            open("TIPE/grille.txt", "w")
            
            
            
    def Option(self):
        if self.state!='MenuOption':
            self.etatbeforeoption=self.state
            self.state='MenuOption'
        
def Continuer(self):
    if self.state=='Menu3':
        self.state='Menu4'

def Quitter(self):
    self.canvas.destroy()
    self.Fenetre.destroy()
    
def Retour(self):
    if self.state=='MenuConfirmation':
        self.state='Menu'
    if self.state=='Menu3':
        self.state='Menu2'
    if self.state=='Menu4':
        self.state='Menu3'
    if self.state=='MenuConfirmation2':
        listelot=[]
        listenom=[]
        self.state='Menu4'
    if self.state=='MenuOption':
        self.state=etatbeforeoption
        
        
        
def Valider(self):

    if self.state == 'Menu2' and txtnbcase.get() != '' and txtprix.get() != '':
        nbcase=int(txtnbcase.get())
        prix=int(txtprix.get())
        etat='Menu3'
    if (
        self.state == 'Menu3'
        and txtquantite.get() != ''
        and txtnomlot.get() != ''
    ):
        Enregistrerlot()
        Lecturedeslots()
        Enregistrertombola()
    if self.state == 'Menu4' and txtnom.get() != '' and txtprenom.get() != '':
        nom=txtnom.get()
        prenom=txtprenom.get()
        mail=txtmail.get()
        Enregistrement()
        txtnom.set('')
        txtprenom.set('')
        txtmail.set('')
        nbticket=0
        for i in registreattente:
            reg.append(i)
        registreattente=[]
        Enregistrertombola()
    if self.state=='MenuConfirmation':
            SupprimerTombola()
            Creer()
    if self.state=='MenuConfirmation2':
        Creer()
        f = open("TIPE/resultats.txt", 'r+')
        if f.read()=='':
            effectuertirage()
    if self.state=='MenuOption':
        if EntreOptioncodevalidation.get()=='1234':
            mailorganisateur=EntreOptionmail.get()
            mdporganisateur=EntreOptionmdp.get()
            optioncodevalidation.set("Le compte mail a été modifié")
        else:
            optioncodevalidation.set("Mauvais mot de passe")
            
def choose():
    regcompte=int(txtcase.get())
    if regcompte not in reg: #Verifie que l'on n'a pas deja coché la case
        reg.append(int(txtcase.get()))
        nbticket+=1
        txtcase.set('')
        Enregistrertombola()
        colorerror='#ffefd8'
    else:
        colorerror='red'
        txtcase.set('')

def back_main_menu():
    global etat
    etat='Menu'

def list_filter(self,liste, lot):
    return [i for i in liste if i != lot]
    
def supprimerlot(self):
    supprlot=[]
    fichier = open("TIPE/lot.txt", "r")           #lit tous les lots dans le fichier texte 
    ligne = fichier.readline()                                        #et les ajoute dans une liste
    fichier.close                                                     
    while ligne:
        supprlot.append (ligne)
        ligne = fichier.readline()
    supprlot=suppassageligne(supprlot)
    supprlot=list_filter(supprlot,supprlot[len(supprlot)-1])
    f = open("TIPE/lot.txt", 'r+')
    f.truncate(0)
    fichier = open("TIPE/lot.txt", "a")       #écrit les lots dans un fichier texte
    for i in range (len(supprlot)):
        fichier.write(supprlot[i] + '\n')
    fichier.close
    fichier = open("TIPE/lot.txt", "r")
    ligne = fichier.readline()                                        #et les ajoute dans une liste
    fichier.close
    registre=[]
    quantite=0
    registre=retirersautligne(ligne)
    textresumelot.delete(0.0, tk.END)
    while ligne:
        if registre==retirersautligne(ligne):
            quantite+=1
            ligne = fichier.readline()
        else :
            textresumelot.insert(tk.END,str(quantite)+retirersautligne(registre)+'\n')
            registre=ligne
            quantite=0
    if quantite!=0:
        textresumelot.insert(tk.END,str(quantite)+retirersautligne(registre)+'\n')
    else :
        textresumelot.insert(tk.END,retirersautligne(registre))
        
        
def commandboutoneffectuertirage():
    global etat
    etat='MenuConfirmation2'

def envoiemail():
    global colorok
    print(listelot)
    print(listecase)
    print(listemail)
    mail_a_envoyer={}
    mail_pas_de_cadeau=[]
    for i, destinataire in enumerate(listemail):
        if destinataire !=None and i<len(listelot):
            if destinataire in mail_a_envoyer:
                mail_a_envoyer[destinataire]+= '\n    1 ' + listelot[i] +' (grâce à la case numéro '+ listecase[i]+')'
            else:
                mail_a_envoyer[destinataire]='Madame, Monsieur\n\nNous sommes ravis de vous annoncer que vous avez gagné à la tombola:\n    1 '+ listelot[i] +' (grâce à la case numéro '+ listecase[i]+')'
    print(mail_a_envoyer)
    yag_smtp_connection = yagmail.SMTP( user=mailorganisateur, password=mdporganisateur, host='smtp.gmail.com')
    subject = 'APEL Ecole Jeanne d''Arc : Tombola'
    for cle, valeur in mail_a_envoyer.items():        
        # email CONTENU
        # ENVOIE de email
        contenu=valeur+"\n\n Vous pouvez venir retirer votre lot (quand il n'y aura pas trop de monde!).\nEn vous remerciant d'avoir joué.\nCordialement,\n\nL'APEL de l'école Jeanne d'Arc"
        yag_smtp_connection.send(cle, subject, [contenu])

    for i in range (len(listelot),len(listemail)):
        if ((listemail[i] !=None) and (listemail[i] not in mail_a_envoyer.keys()) and (listemail[i] not in mail_pas_de_cadeau)):
                mail_pas_de_cadeau.append(listemail[i])
    contenu="Madame, Monsieur\n\nNous sommes au regret de vous annoncer que vous n'avez pas gagné à la tombola.\n\nEn vous remerciant tout de même d'avoir joué.\nCordialement,\n\nL'APEL de l'école Jeanne d'Arc"
    for i in mail_pas_de_cadeau:
        yag_smtp_connection.send(i, subject, [contenu])
    colorok='green'

    
def on_entry_click(event):
    if EntreOptionmail.get() == 'Entrez votre adresse mail':
       EntreOptionmail.delete(0, "end") # delete all the text in the entry
       EntreOptionmail.insert(0, '') #Insert blank for user input
       EntreOptionmail.config(fg = 'black')
       
def on_entry_click2(event):
    if EntreOptionmdp.get() == 'Entrez votre mot de passe':
       EntreOptionmdp.delete(0, "end") # delete all the text in the entry
       EntreOptionmdp.insert(0, '') #Insert blank for user input
       EntreOptionmdp.config(fg = 'black')
       
def on_entry_click3(event):
    if EntreOptioncodevalidation.get() == 'clé de validation':
       EntreOptioncodevalidation.delete(0, "end") # delete all the text in the entry
       EntreOptioncodevalidation.insert(0, '') #Insert blank for user input
       EntreOptioncodevalidation.config(fg = 'black')
       
def on_focusout(event):
    if EntreOptionmail.get() == '':
        EntreOptionmail.insert(0, 'Entrez votre adresse mail')
        EntreOptionmail.config(fg = 'grey')
        
def on_focusout2(event):
    if EntreOptionmdp.get() == '':
        EntreOptionmdp.insert(0, 'Entrez votre mot de passe')
        EntreOptionmdp.config(fg = 'grey')
        
def on_focusout3(event):
    if EntreOptioncodevalidation.get() == '':
        EntreOptioncodevalidation.insert(0, 'clé de validation')
        EntreOptioncodevalidation.config(fg = 'grey')
         
#Creation du texte
textresumelot=tk.Text(canvas,width=str(int(35*fontsize)),height='10', font=(self.FONT, int(15*fontsize)))
texteresultat=tk.Text(canvas,width=str(int(100*fontsize)),height='10', font=(self.FONT, int(15*fontsize)))
#Creation des boutons :
BoutonQuitter=tk.Button(canvas,text='Quitter',font=(self.FONT, int(15*fontsize)),bg=colorbutton,command=Quitter)
BoutonRetour=tk.Button(canvas,text='Retour',font=(self.FONT, int(15*fontsize)),bg=colorbutton,command=Retour)
BoutonValider=tk.Button(canvas,text='Valider',font=(self.FONT, int(15*fontsize)),bg=colorbutton,command=Valider)
BoutonOption=tk.Button(canvas,text='Options',font=(self.FONT, int(15*fontsize)),bg=colorbutton,command=Option)
Boutonback_main_menu=tk.Button(canvas,text='Retour au Menu Principal',font=(self.FONT, int(15*fontsize)),bg=colorbutton,command=back_main_menu)
BoutonContinuer=tk.Button(canvas,text='Continuer',font=(self.FONT, int(15*fontsize)),bg=colorbutton,command=Continuer)
BoutonSupprimerLot=tk.Button(canvas,text='Supprimer le dernier lot',font=(self.FONT,int(15*fontsize)),bg=colorbutton,command=supprimerlot)
BoutonEffectuerTirage=tk.Button(canvas,text='Effectuer le tirage',font=(self.FONT,int(15*fontsize)),bg=colorbutton,command=commandboutoneffectuertirage)
BoutonValiderLot=tk.Button(canvas,text='Valider le lot',font=(self.FONT, int(15*fontsize)),bg=colorbutton,command=Valider)
BoutonEnvoieMail=tk.Button(canvas,text='Envoyer un mail aux gagnants',font=(self.FONT, int(15*fontsize)),bg=colorbutton,command=envoiemail)

#Création d'entrées
Entrequantite= tk.Entry(Fenetre,bg=colorbg,textvariable=txtquantite,width=5,bd=3,font=(self.FONT, int(45*fontsize)))
Entrenomlot= tk.Entry(Fenetre,bg=colorbg,bd=3,textvariable=txtnomlot,font=(self.FONT, int(45*fontsize)))
Entrenbcase=tk.Entry(Fenetre,bg=colorbg,textvariable=txtnbcase,width=5,bd=3,font=(self.FONT, int(45*fontsize)))
Entreprixcase=tk.Entry(Fenetre,bg=colorbg,textvariable=txtprix,width=5,bd=3,font=(self.FONT, int(45*fontsize)))
Entrenom=tk.Entry(Fenetre,bg=colorbg,textvariable=txtnom,width=30,bd=3,font=(self.FONT, int(20*fontsize)))
Entreprenom=tk.Entry(Fenetre,bg=colorbg,textvariable=txtprenom,width=30,bd=3,font=(self.FONT, int(20*fontsize)))
Entremail=tk.Entry(Fenetre,bg=colorbg,textvariable=txtmail,width=30,bd=3,font=(self.FONT, int(20*fontsize)))
EntreOptionmail=tk.Entry(Fenetre,bg=colorbg,textvariable=optionmail,width=30,bd=3,font=(self.FONT, int(20*fontsize)))
EntreOptionmdp=tk.Entry(Fenetre,bg=colorbg,textvariable=optionmdp,width=30,bd=3,font=(self.FONT, int(20*fontsize)),show='*')
EntreOptioncodevalidation=tk.Entry(Fenetre,bg=colorbg,textvariable=optioncodevalidation,width=30,bd=3,font=(self.FONT, int(20*fontsize)))

#Paramètre des entrées
EntreOptionmail.bind('<FocusIn>', on_entry_click)
EntreOptionmail.bind('<FocusOut>', on_focusout)
EntreOptionmail.insert(0, 'Entrez votre adresse mail')
EntreOptionmdp.bind('<FocusIn>', on_entry_click2)
EntreOptionmdp.bind('<FocusOut>', on_focusout2)
EntreOptionmdp.insert(0, 'Entrez votre mot de passe')

EntreOptioncodevalidation.bind('<FocusIn>', on_entry_click3)
EntreOptioncodevalidation.bind('<FocusOut>', on_focusout3)
EntreOptioncodevalidation.insert(0, 'clé de validation')

def Grille(x):
    carreau=[[canvas.create_rectangle(i*H/x,j*H/x,(i+1)*H/x,(j+1)*H/x,fill=colorbg) for i in range(x)] for j in range(x)]
    Framecoche(carre)
    chiffres=[[canvas.create_text((2*i+1)*(H/(x*2)),H/(x*2)*(2*j+1),text=(i+1)+(x*j),font=(self.FONT, int((15*fontsize)*0.1/nbcase)))for i in range(x)]for j in range(x)]

def AffichageMenu():
    titre=canvas.create_text(L/2,H*(1/4),text='TOMBOLA',font=police)
    creer=canvas.create_text(L*(1/2),H*(3/7),text='Créer une Tombola', font=(self.FONT, int(30*fontsize)))
    ouvrir=canvas.create_text(L*(1/2),H*(4/7),text='Ouvrir une Tombola', font=(self.FONT, int(30*fontsize)))
    afficheresult=canvas.create_text(L*(1/2),H*(5/7),text='Afficher les résultats', font=(self.FONT, int(30*fontsize)))
    
    #Boutons à ajouter
    BoutonQuitter.place(x=L*(9/10),y=H*(7/8))
    BoutonOption.place(x=L*(9/10),y=H*(1/20))
    #Boutons à supprimer

    BoutonRetour.place_forget()
    BoutonValider.place_forget()
    Boutonback_main_menu.place_forget()
    BoutonEnvoieMail.place_forget()
    #Entrées à supprimer
    Entrenbcase.place_forget()
    Entreprixcase.place_forget()
    texteresultat.place_forget()
    EntreOptionmail.place_forget()
    EntreOptionmdp.place_forget()
    EntreOptioncodevalidation.place_forget()
def AffichageMenu2():
    titrenbcase=canvas.create_text(L*(1/4),H*(3/7), text='Entrer nombre de cases',font=(self.FONT,int(45*fontsize)))
    titrenbcase=canvas.create_text(L*(1/4),H*(10/21), text='(nombre minimum de cases pour la tombola)',font=(self.FONT,int(15*fontsize)))
    titreprix=canvas.create_text(L*(3/4),H*(3/7), text='Prix de la case (unitaire)',font=(self.FONT,int(40*fontsize)))
    

    #Boutons à ajouter
    BoutonValider.place(x=L*(5/10),y=H*(7/8))
    BoutonOption.place(x=L*(9/10),y=H*(1/20))
    #Boutons à supprimer
    Boutonback_main_menu.place_forget()
    BoutonContinuer.place_forget()
    BoutonSupprimerLot.place_forget()
    BoutonValiderLot.place_forget()
    BoutonRetour.place_forget()
    #Entrées à ajouter
    Entreprixcase.place(x=L*(70/100),y= H*(55/100))
    Entrenbcase.place(x=L*(20/100),y=H*(55/100))
    #Entrées à supprimer
    Entrenomlot.place_forget()
    Entrequantite.place_forget()
    textresumelot.place_forget()
    EntreOptionmail.place_forget()
    EntreOptionmdp.place_forget()
    EntreOptioncodevalidation.place_forget()
    
def AffichageMenu3():
    Titreaffichage3=canvas.create_text(L*(1/2),H*(5/20), text='Enregistrement des lots',font=(self.FONT,int(50*fontsize)))
    
    Textenomlot=canvas.create_text(L*(22/40),H*(21/40),text='Nom du lot', font=(self.FONT,int(20*fontsize)))
   
    Textequantite=canvas.create_text(L*(12/40),H*(21/40),text='Quantité', font=(self.FONT,int(20*fontsize)))
   
    Titrerecapitulatif=canvas.create_text(L*(3/20),H*(2/20),text='RECAPITULATIF DES LOTS', font=(self.FONT,int(20*fontsize)))

    textresumelot.place(x=L*(5/100),y=H*(3/20))
    #Entrées à ajouter
    Entrenomlot.place(x=L*(8/20),y=H*(23/40))
    Entrequantite.place(x=L*(5/20),y=H*(23/40))
    #Boutons à ajouter
    BoutonValiderLot.place(x=L*(82/100),y=H*(55/100))
    BoutonContinuer.place(x=L*(5/10),y=H*(7/8))
    BoutonSupprimerLot.place(x=L*(16/20),y=H*(65/100))
    BoutonOption.place(x=L*(9/10),y=H*(1/20))
    #Boutons à supprimer
    Boutonback_main_menu.place_forget()
    BoutonEffectuerTirage.place_forget()
    BoutonValider.place_forget()
    BoutonRetour.place_forget()
    #Entrées à supprimer
    Entrenbcase.place_forget()
    Entreprixcase.place_forget()
    Entrenom.place_forget()
    Entreprenom.place_forget()
    Entremail.place_forget()
    EntreOptionmail.place_forget()
    EntreOptionmdp.place_forget()
    EntreOptioncodevalidation.place_forget()
    
def AffichageMenu4():
    global carre
    carre=math.ceil(math.sqrt(nbcase))
    Grille(carre)
    nom=canvas.create_text(L*(8/10),H*(4/16),text='Nom', font=(self.FONT,int(30*fontsize)))
    prenom=canvas.create_text(L*(8/10),H*(6/16),text='Prénom', font=(self.FONT,int(30*fontsize)))
    prixtotal=canvas.create_text(L*(8/10),H*(1/8),text='PRIX TOTAL', font=(self.FONT,int(30*fontsize)))
    calcprix=canvas.create_text(L*(8/10),H*(3/16),text=str((nbticket)*prix)+' €', font=(self.FONT,int(30*fontsize)))
    adresse=canvas.create_text(L*(8/10),H*(8/16),text='Mail', font=(self.FONT,int(30*fontsize)))
    cocheimpossible=canvas.create_text(L*(16/20) ,H*(5/32) ,text='Déjà coché', font=(self.FONT,int(20*fontsize)), fill=colorerror)
    #Boutons à ajouter
    BoutonRetour.place(x=L*(70/100),y=H*(7/8))
    BoutonValider.place(x=L*(31/40),y=H*(60/100))
    BoutonEffectuerTirage.place(x=L*(31/40),y=H*(7/8))
    BoutonOption.place(x=L*(9/10),y=H*(1/20))
    #Boutons à supprimer
    Boutonback_main_menu.place_forget()
    BoutonContinuer.place_forget()
    BoutonSupprimerLot.place_forget()
    BoutonValiderLot.place_forget()
    BoutonEnvoieMail.place_forget()
    #Entrées à ajouter
    Entrenom.place(x=L*(70/100),y=H*(28/100))
    Entreprenom.place(x=L*(70/100),y=H*(40/100))
    Entremail.place(x=L*(70/100),y=H*(53/100))
    #Entrées à supprimer
    Entrenomlot.place_forget()
    Entrequantite.place_forget()
    textresumelot.place_forget()
    texteresultat.place_forget()
    EntreOptionmail.place_forget()
    EntreOptionmdp.place_forget()
    EntreOptioncodevalidation.place_forget()
    
def AffichageMenu5():
    emailconfirmation=canvas.create_text((L*(35/40)),H*(9/16),text='Emails envoyés', font=(self.FONT,int(15*fontsize)), fill=colorok)
    #Label à ajouter
    texteresultat.place(x=L*(2/10),y=H*(4/10))
    #Boutons à ajouter
    Boutonback_main_menu.place(x=L*(8/10),y=H*(1/8))
    BoutonEnvoieMail.place(x=(L*(8/10)),y=H*(5/8))
    BoutonOption.place(x=L*(9/10),y=H*(1/20))
    #Boutons à supprimer
    BoutonRetour.place_forget()
    BoutonValider.place_forget()
    BoutonEffectuerTirage.place_forget()
    #Entrées à supprimer
    Entrenom.place_forget()
    Entreprenom.place_forget()
    Entremail.place_forget()
    EntreOptionmail.place_forget()
    EntreOptionmdp.place_forget()
    EntreOptioncodevalidation.place_forget()
    
def AffichageMenuConfirmation():
    texteconfirmation=canvas.create_text((L*(20/40)),H*(40/100),text='Confirmation', font=(self.FONT,int(40*fontsize)))
    confenvoie=canvas.create_text((L*(20/40)),H*(45/100),text='Si une tombola a déjà été créée, celle-ci sera supprimée', font=(self.FONT,int(15*fontsize)))
    BoutonValider.place(x=6*L/10,y=H/2)
    BoutonRetour.place(x=4*L/10,y=H/2)
    EntreOptionmail.place_forget()
    EntreOptionmdp.place_forget()
    EntreOptioncodevalidation.place_forget()
    BoutonOption.place(x=L*(9/10),y=H*(1/20))
def AffichageMenuConfirmation2():
    texteconfirmation2=canvas.create_text((L*(20/40)),H*(40/100),text='Confirmation', font=(self.FONT,int(40*fontsize)))
    #Bouton à ajouter
    BoutonValider.place(x=6*L/10,y=H/2)
    BoutonRetour.place(x=4*L/10,y=H/2)
    BoutonOption.place(x=L*(9/10),y=H*(1/20))
    #Entrées à supprimer
    Entrenom.place_forget()
    Entreprenom.place_forget()
    Entremail.place_forget()
    BoutonEffectuerTirage.place_forget()
    EntreOptionmail.place_forget()
    EntreOptionmdp.place_forget()
    EntreOptioncodevalidation.place_forget()
    
def AffichageOption():
    Texteoption=canvas.create_text((L*(20/40)),H*(30/100),text='Options', font=(self.FONT,int(40*fontsize)))
    
    #Bouton à ajouter
    BoutonRetour.place(x=4*L/10,y=2*H/3)
    BoutonValider.place(x=6*L/10,y=2*H/3)
    #Entrées à ajouter
    EntreOptionmail.place(x=L*(40/100),y=H*(40/100))
    EntreOptionmdp.place(x=L*(40/100),y=H*(45/100))
    EntreOptioncodevalidation.place(x=L*(40/100),y=H*(50/100))
    
    
    BoutonOption.place_forget()
    Boutonback_main_menu.place_forget()
    BoutonContinuer.place_forget()
    BoutonSupprimerLot.place_forget()
    BoutonEffectuerTirage.place_forget()
    BoutonValiderLot.place_forget()
    BoutonEnvoieMail.place_forget()
    Entrequantite.place_forget()
    Entrenomlot.place_forget()
    Entrenbcase.place_forget()
    Entreprixcase.place_forget()
    Entrenom.place_forget()
    Entreprenom.place_forget()
    Entremail.place_forget()
    textresumelot.place_forget()
    texteresultat.place_forget()
def Lecturedeslots():
    if txtnomlot.get()!='':
        leclot=txtnomlot.get()
        quantlot=txtquantite.get()
        textresumelot.insert(tk.END,quantlot+leclot+'\n')
        txtnomlot.set('')
        txtquantite.set('')

def suppassageligne(L):                                     # enlève les \n d'une liste pour ne pas sauter une           
    return [i.replace('\n','') for i in L]

def Affichage():
    if etat=='Menu' :
        AffichageMenu()
    if etat=='Menu2':
        AffichageMenu2()
    if etat=='Menu3':
        AffichageMenu3()
    if etat=='Menu4':
        AffichageMenu4()
    if etat=='Menu5':
        AffichageMenu5()
    if etat=='MenuConfirmation':
        AffichageMenuConfirmation()
    if etat=='MenuConfirmation2':
        AffichageMenuConfirmation2()
    if etat=='MenuOption':
        AffichageOption()
def Creer():
    global etat
    if etat=='MenuConfirmation':
        etat='Menu2'
    if etat=='MenuConfirmation2':
        etat='Menu5'

def Framecoche(x):
    global nbticket
    for w in reg:
        for j in range (x):
            for i in range (x):
                compteur=(1+i)+(x*j)
                if compteur==w: #Localise la case à cocher
                        cochage=((canvas.create_rectangle((i*H/x),j*H/x,(i+1)*H/x,(j+1)*H/x ,fill='black')))
    for w in registreattente :
        for j in range (x):
            for i in range (x):
                compteur=(1+i)+(x*j)
                if compteur==w: #Localise la case à cocher
                        cochage=((canvas.create_rectangle((i*H/x),j*H/x,(i+1)*H/x,(j+1)*H/x ,fill='#6ab04c')))

def lectureresultat():
    global affichageresult
    texteresultat.delete(0.0,tk.END)
    affichageresult=''
    fichier = open("TIPE/resultats.txt", "r")        #lit tous les noms et prénoms dans le fichier
    ligne = fichier.readline()                                     # texte et les ajoute dans une liste
    fichier.close                                
    while ligne:
        affichageresult=affichageresult+ligne
        ligne = fichier.readline()
    texteresultat.insert(0.0,affichageresult)

def effectuertirage():
    global affichageresult
    texteresultat.delete(0.0,tk.END)
    affichageresult=''
    Tirageautomatique()
    fichier = open("TIPE/resultats.txt", "r")        #lit tous les noms et prénoms dans le fichier
    ligne = fichier.readline()                                     # texte et les ajoute dans une liste
    fichier.close                                
    while ligne:
        affichageresult=affichageresult+ligne
        ligne = fichier.readline()
    texteresultat.insert(0.0,affichageresult)
    
def Ouvrir():
    global etat
    if etat=='Menu':
        chargetombola()
        etat='Menu4'

def SupprimerTombola ():
    global reg
    reg=[]
    textresumelot.delete(0.0,tk.END)
    f = open("TIPE/lot.txt", 'r+')
    f.truncate(0)
    f = open("TIPE/informations.txt", 'r+')
    f.truncate(0)
    f = open("TIPE/resultats.txt", 'r+')
    f.truncate(0)
    f = open("TIPE/sauvegarde.txt", 'r+')
    f.truncate(0)
    f = open("TIPE/grille.txt", 'r+')
    f.truncate(0)

def Tirageautomatique():
    L_finale=[]
    associerlisteinfo()
    random.shuffle(listeinfo)
    associerlistenom()
    associerlistelot()
    random.shuffle(listelot)
    associerlistemail()
    associerlistecase()                                      #on associe un lot par personne
    if (len(listenom)) > (len(listelot)):
        L_finale.extend(
            f'{listenom[i]} a gagne {listelot[i]} grâce à la case numéro: '
            + listecase[i]
            + '\n'
            for i in range(len(listelot))
        )

    else:
        L_finale.extend(
            f'{listenom[i]} a gagne {listelot[i]} grâce à la case numéro: '
            + listecase[i]
            + '\n'
            for i in range(len(listenom))
        )

    L_finale.sort()
    for result in L_finale:                                       #on écrit le nom des personnes et leur lot dans
        with open("TIPE/resultats.txt", "a") as fichier:
            fichier.write(result)

def retirersautligne(ligne):
    ligne=suppassageligne(ligne)
    nouvelleligne=''
    for i in ligne :
        nouvelleligne=nouvelleligne+i
    return nouvelleligne
    
def chargetombola():
    global reg, nbcase,prix
    regtemp=[]
    fichier = open("TIPE/sauvegarde.txt", "r")           #lit tous les lots dans le fichier texte 
    ligne = fichier.readline()                                        #et les ajoute dans une liste
    fichier.close                                                     
    while ligne:
        regtemp.append (ligne)
        ligne = fichier.readline()
    regtemp=suppassageligne(regtemp)
    for i in regtemp:
        reg.append(int(i))
    fichier = open("TIPE/grille.txt", "r")
    ligne = fichier.readline()                                        #et les ajoute dans une liste
    fichier.close
    info=[]
    while ligne:
        info.append (ligne)
        ligne = fichier.readline()
    info=suppassageligne(info)
    nbcase=int(info[0])
    prix=int(info[1])
    fichier = open("TIPE/lot.txt", "r")
    ligne = fichier.readline()                                        #et les ajoute dans une liste
    fichier.close
    registre=retirersautligne(ligne)
    quantite=0
    textresumelot.delete(0.0, tk.END)
    while ligne:
        if registre==retirersautligne(ligne):
            quantite+=1
            ligne = fichier.readline()
        else :
            textresumelot.insert(tk.END,str(quantite)+retirersautligne(registre)+'\n')
            registre=retirersautligne(ligne)
            quantite=0
    textresumelot.insert(tk.END,str(quantite)+retirersautligne(registre)+'\n')

def associerlistenom():
    global listenom
    listenom = [cherchernoms(i) for i in listeinfo]

def trouvercase(str): 
    return re.findall(r'[0-9]+', str) 

def associerlisteinfo():
    global listeinfo, listecase
    fichier = open("TIPE/informations.txt", "r")        #lit tous les noms et prénoms dans le fichier
    ligne = fichier.readline()                                     # texte et les ajoute dans une liste
    fichier.close
    listeinfo = []
    listecase = []
    while ligne:
        if cherchernoms(ligne) is None:
            listecase.append(ligne)
        else:
            listeinfo.append (ligne)
        ligne = fichier.readline()
    listeinfo=suppassageligne(listeinfo)
    listecase=suppassageligne(listecase)
    lesnumero = [trouvercase(i) for i in listecase]
    lenumero = []
    for listenum in lesnumero:
        lenumero.extend(iter(listenum))
    for i in range (len(listeinfo)):
        listeinfo[i] += f' {lenumero[i]}'
        
def associerlistelot():
    global listelot
    listelot=[]
    fichier = open("TIPE/lot.txt", "r")           #lit tous les lots dans le fichier texte 
    ligne = fichier.readline()                                        #et les ajoute dans une liste
    fichier.close                                                     
    while ligne:
        listelot.append (ligne)
        ligne = fichier.readline()
    listelot=suppassageligne(listelot)

def Enregistrement():
    fichier = open("TIPE/informations.txt", "a")       #écrit les noms dans un fichier texte
    for numerocase in registreattente:
        fichier.write(f'{str(numerocase)} ')
    fichier.write('\n')
    for _ in range (nbticket):
        fichier.write(f'{txtnom.get()} ')
        fichier.write(f'{txtprenom.get()} ')
        fichier.write(txtmail.get()+'\n')
        fichier.close

def Enregistrerlot():
    fichier = open("TIPE/lot.txt", "a")       #écrit les lots dans un fichier texte
    for _ in range (int(txtquantite.get())):
        fichier.write(txtnomlot.get()+'\n')
    fichier.close

def Enregistrertombola():
    f = open("TIPE/sauvegarde.txt", 'r+')
    f.truncate(0)
    fichier = open("TIPE/sauvegarde.txt", "a")       #écrit les coches dans un fichier texte
    for i in range (len(reg)):
        fichier.write(str(reg[i])+ '\n')
    fichier.close
    f = open("TIPE/grille.txt", 'r+')
    f.truncate(0)
    fichier = open("TIPE/grille.txt", "a")       #écrit les infos de la grille dans un fichier
    fichier.write(str(nbcase)+ '\n')
    fichier.write(str(prix)+ '\n')
    fichier.close

def Clic(event):
    global etat,cursor, colorok, nbticket, registreattente, colorerror
    X=event.x
    Y=event.y
    if etat=='Menu':
        if X>L/2-50*kL and X<L/2+50*kL and Y>H*(3/7)-50*kH and Y<H*(3/7)+50*kH:
            etat='MenuConfirmation'
        if X>L*(1/2)-50*kL and X<L*(1/2)+50*kL and Y>H*(5/7)-50*kH and Y<H*(5/7)+50*kH:
            lectureresultat()
            etat='Menu5'

        if X>L*(1/2)-50*kL and X<L*(1/2)+50*kL and Y>H*(4/7)-50*kH and Y<H*(4/7)+50*kH:
            Ouvrir()
    elif etat=='Menu4':
        if X<H :
            i=X//(H/carre)
            j=Y//(H/carre)
            g=j*carre+i+1
            if int(g) in registreattente:
                    nbticket=nbticket-1
                    registreattente.remove(int(g))
            elif int(g) in reg:
                    colorerror='red'
            else :
                nbticket=nbticket+1
                registreattente.append(int(g))
                colorerror=colorbg
            Framecoche(carre)
            Enregistrertombola()

def cherchermail(expression):
    a=re.search(r"[-A-Za-z0-9._]+@[-A-Za-z0-9._]+",expression)
    if a is not None:
        return(a.group())

def cherchernumero(expression):
    a=re.search(r"[0-9]",expression)
    if a is not None:
        return(a.group())

def cherchernoms(expression):
    a=re.search(r"([-A-Za-zéàïë]+ )+", expression)
    if a is not None :
        return(a.group())

def associerlistemail():
    global listemail
    listemail = [cherchermail(i) for i in listeinfo]

def associerlistecase():
    global listecase
    listecase = [trouvercase(i)[0] for i in listeinfo]

canvas.bind('<Button-1>',Clic)
canvas.focus_set()

while start:
    canvas.delete(tk.ALL)
    Affichage()
    Fenetre.update()