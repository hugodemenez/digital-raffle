import tkinter as tk
import math
import random
import os
import time
import smtplib
import re
import yagmail
Fenetre=tk.Tk()
Fenetre.title("TOMBOLA")
#Fenetre.attributes('-fullscreen',1)
Lengh = Fenetre.winfo_screenwidth()
Height = Fenetre.winfo_screenheight()
colorerror='#ffefd8'
colorok='#ffefd8'
colorbutton='#ff7f50'
colorclic='#7986CB'
colorbg='#ffefd8'
L=Lengh
H=Height-70
fontsize=int(L)*int(H)/(1920*1080)
Fenetre.resizable(width=True, height=True)
canvas = tk.Canvas(Fenetre, width= L, height= H, bg=colorbg)
canvas.pack()
Fenetre.state("zoomed")

if not os.path.exists('TIPE'):
    os.mkdir('TIPE')
    fichier1 = open("TIPE/informations.txt", "w")
    fichier2 = open("TIPE/lot.txt", "w")
    fichier3 = open("TIPE/resultats.txt", "w")
    fichier4 = open("TIPE/sauvegarde.txt", "w")
    fichier5 = open("TIPE/grille.txt", "w")

start=True
police='Rockwell  90'
policeecriture='Rockwell'
etat='Menu'
kL=L/1536
kH=H/864
nbcase=0
txtnbcase=tk.StringVar()
nom=0
txtnom=tk.StringVar()
prenom=0
txtprenom=tk.StringVar()
mail=0
txtmail=tk.StringVar()
prix=0
txtprix=tk.StringVar()
cursor='rien'
nbticket=0
txtcase=tk.StringVar()
cochage=0
reg=[]
regcompte=0
listenom=[]
listelot=[]
listemail=[]
listeinfo=[]
affichageresult=''
txtquantite=tk.StringVar()
txtnomlot=tk.StringVar()
carre=math.ceil(math.sqrt(nbcase))
registreattente=[]
leclot=''
quantlot=''
registrepermanent=[]
listecase=[]
optionmail=tk.StringVar()
optionmdp=tk.StringVar()
optioncodevalidation=tk.StringVar()
etatbeforeoption=''
mailorganisateur="pierreemmanueldumont@gmail.com"
mdporganisateur="yuusjrpteqiglfog"

def Option():
    global etat,etatbeforeoption
    if etat!='MenuOption':
        etatbeforeoption=etat
        etat='MenuOption'
        
def Continuer():
    global etat
    if etat=='Menu3':
        etat='Menu4'

def Quitter():
    global start
    start=False
    canvas.destroy()
    Fenetre.destroy()
    
def Retour():
    global etat, affichageresult, listelot, listenom
    if etat=='MenuConfirmation':
        etat='Menu'
    if etat=='Menu3':
        etat='Menu2'
    if etat=='Menu4':
        etat='Menu3'
    if etat=='MenuConfirmation2':
        listelot=[]
        listenom=[]
        etat='Menu4'
    if etat=='MenuOption':
        etat=etatbeforeoption
def Valider():
    global etat, nbcase , prix , nom , prenom , mail, txtprenom , txtnom, txtmail , nbticket, txtquantite, txtnomlot, registreattente,reg,mailorganisateur,mdporganisateur
    if etat=='Menu2':
        if txtnbcase.get()!='' and txtprix.get()!='':
            nbcase=int(txtnbcase.get())
            prix=int(txtprix.get())
            etat='Menu3'
    if etat=='Menu3':
        if txtquantite.get()!='' and txtnomlot.get()!='':
            Enregistrerlot()
            Lecturedeslots()
            Enregistrertombola()
    if etat=='Menu4':
        if txtnom.get()!='' and txtprenom.get()!='':
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
    if etat=='MenuConfirmation':
            SupprimerTombola()
            Creer()
    if etat=='MenuConfirmation2':
        Creer()
        f = open("TIPE/resultats.txt", 'r+')
        if f.read()=='':
            effectuertirage()
    if etat=='MenuOption':
        if EntreOptioncodevalidation.get()=='1234':
            mailorganisateur=EntreOptionmail.get()
            mdporganisateur=EntreOptionmdp.get()
            optioncodevalidation.set("Le compte mail a été modifié")
        else:
            optioncodevalidation.set("Mauvais mot de passe")
            
def fcncocher():
    global cochage, nbticket, txtcase, reg, regcompte,colorerror
    regcompte=int(txtcase.get())
    if (regcompte in reg) == False: #Verifie que l'on n'a pas deja coché la case
        reg.append(int(txtcase.get()))
        nbticket+=1
        txtcase.set('')
        Enregistrertombola()
        colorerror='#ffefd8'
    else:
        colorerror='red'
        txtcase.set('')

def Retourmenuprincipal():
    global etat
    etat='Menu'

def filtredeliste(liste, lot):
    return [i for i in liste if i != lot]
    
def supprimerlot():
    supprlot=[]
    fichier = open("TIPE/lot.txt", "r")           #lit tous les lots dans le fichier texte 
    ligne = fichier.readline()                                        #et les ajoute dans une liste
    fichier.close                                                     
    while ligne:
        supprlot.append (ligne)
        ligne = fichier.readline()
    supprlot=suppassageligne(supprlot)
    supprlot=filtredeliste(supprlot,supprlot[len(supprlot)-1])
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
    i=0
    print(listelot)
    print(listecase)
    print(listemail)
    mail_a_envoyer={}
    mail_pas_de_cadeau=[]
    for destinataire in listemail:
        if destinataire !=None and i<len(listelot):
            if destinataire in mail_a_envoyer.keys():
                mail_a_envoyer[destinataire]+= '\n    1 ' + listelot[i] +' (grâce à la case numéro '+ listecase[i]+')'
            else:
                mail_a_envoyer[destinataire]='Madame, Monsieur\n\nNous sommes ravis de vous annoncer que vous avez gagné à la tombola:\n    1 '+ listelot[i] +' (grâce à la case numéro '+ listecase[i]+')'
        i+=1
    print(mail_a_envoyer)
    yag_smtp_connection = yagmail.SMTP( user=mailorganisateur, password=mdporganisateur, host='smtp.gmail.com')
        # email SUJET
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
textresumelot=tk.Text(canvas,width=str(int(35*fontsize)),height='10', font=(policeecriture, int(15*fontsize)))
texteresultat=tk.Text(canvas,width=str(int(100*fontsize)),height='10', font=(policeecriture, int(15*fontsize)))
#Creation des boutons :
BoutonQuitter=tk.Button(canvas,text='Quitter',font=(policeecriture, int(15*fontsize)),bg=colorbutton,command=Quitter)
BoutonRetour=tk.Button(canvas,text='Retour',font=(policeecriture, int(15*fontsize)),bg=colorbutton,command=Retour)
BoutonValider=tk.Button(canvas,text='Valider',font=(policeecriture, int(15*fontsize)),bg=colorbutton,command=Valider)
BoutonOption=tk.Button(canvas,text='Options',font=(policeecriture, int(15*fontsize)),bg=colorbutton,command=Option)
BoutonRetourMenuPrincipal=tk.Button(canvas,text='Retour au Menu Principal',font=(policeecriture, int(15*fontsize)),bg=colorbutton,command=Retourmenuprincipal)
BoutonContinuer=tk.Button(canvas,text='Continuer',font=(policeecriture, int(15*fontsize)),bg=colorbutton,command=Continuer)
BoutonSupprimerLot=tk.Button(canvas,text='Supprimer le dernier lot',font=(policeecriture,int(15*fontsize)),bg=colorbutton,command=supprimerlot)
BoutonEffectuerTirage=tk.Button(canvas,text='Effectuer le tirage',font=(policeecriture,int(15*fontsize)),bg=colorbutton,command=commandboutoneffectuertirage)
BoutonValiderLot=tk.Button(canvas,text='Valider le lot',font=(policeecriture, int(15*fontsize)),bg=colorbutton,command=Valider)
BoutonEnvoieMail=tk.Button(canvas,text='Envoyer un mail aux gagnants',font=(policeecriture, int(15*fontsize)),bg=colorbutton,command=envoiemail)

#Création d'entrées
Entrequantite= tk.Entry(Fenetre,bg=colorbg,textvariable=txtquantite,width=5,bd=3,font=(policeecriture, int(45*fontsize)))
Entrenomlot= tk.Entry(Fenetre,bg=colorbg,bd=3,textvariable=txtnomlot,font=(policeecriture, int(45*fontsize)))
Entrenbcase=tk.Entry(Fenetre,bg=colorbg,textvariable=txtnbcase,width=5,bd=3,font=(policeecriture, int(45*fontsize)))
Entreprixcase=tk.Entry(Fenetre,bg=colorbg,textvariable=txtprix,width=5,bd=3,font=(policeecriture, int(45*fontsize)))
Entrenom=tk.Entry(Fenetre,bg=colorbg,textvariable=txtnom,width=30,bd=3,font=(policeecriture, int(20*fontsize)))
Entreprenom=tk.Entry(Fenetre,bg=colorbg,textvariable=txtprenom,width=30,bd=3,font=(policeecriture, int(20*fontsize)))
Entremail=tk.Entry(Fenetre,bg=colorbg,textvariable=txtmail,width=30,bd=3,font=(policeecriture, int(20*fontsize)))
EntreOptionmail=tk.Entry(Fenetre,bg=colorbg,textvariable=optionmail,width=30,bd=3,font=(policeecriture, int(20*fontsize)))
EntreOptionmdp=tk.Entry(Fenetre,bg=colorbg,textvariable=optionmdp,width=30,bd=3,font=(policeecriture, int(20*fontsize)),show='*')
EntreOptioncodevalidation=tk.Entry(Fenetre,bg=colorbg,textvariable=optioncodevalidation,width=30,bd=3,font=(policeecriture, int(20*fontsize)))

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
    chiffres=[[canvas.create_text((2*i+1)*(H/(x*2)),H/(x*2)*(2*j+1),text=(i+1)+(x*j),font=(policeecriture, int((15*fontsize)*0.1/nbcase)))for i in range(x)]for j in range(x)]

def AffichageMenu():
    titre=canvas.create_text(L/2,H*(1/4),text='TOMBOLA',font=police)
    creer=canvas.create_text(L*(1/2),H*(3/7),text='Créer une Tombola', font=(policeecriture, int(30*fontsize)))
    ouvrir=canvas.create_text(L*(1/2),H*(4/7),text='Ouvrir une Tombola', font=(policeecriture, int(30*fontsize)))
    afficheresult=canvas.create_text(L*(1/2),H*(5/7),text='Afficher les résultats', font=(policeecriture, int(30*fontsize)))
    
    #Boutons à ajouter
    BoutonQuitter.place(x=L*(9/10),y=H*(7/8))
    BoutonOption.place(x=L*(9/10),y=H*(1/20))
    #Boutons à supprimer

    BoutonRetour.place_forget()
    BoutonValider.place_forget()
    BoutonRetourMenuPrincipal.place_forget()
    BoutonEnvoieMail.place_forget()
    #Entrées à supprimer
    Entrenbcase.place_forget()
    Entreprixcase.place_forget()
    texteresultat.place_forget()
    EntreOptionmail.place_forget()
    EntreOptionmdp.place_forget()
    EntreOptioncodevalidation.place_forget()
def AffichageMenu2():
    titrenbcase=canvas.create_text(L*(1/4),H*(3/7), text='Entrer nombre de cases',font=(policeecriture,int(45*fontsize)))
    titrenbcase=canvas.create_text(L*(1/4),H*(10/21), text='(nombre minimum de cases pour la tombola)',font=(policeecriture,int(15*fontsize)))
    titreprix=canvas.create_text(L*(3/4),H*(3/7), text='Prix de la case (unitaire)',font=(policeecriture,int(40*fontsize)))
    

    #Boutons à ajouter
    BoutonValider.place(x=L*(5/10),y=H*(7/8))
    BoutonOption.place(x=L*(9/10),y=H*(1/20))
    #Boutons à supprimer
    BoutonRetourMenuPrincipal.place_forget()
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
    Titreaffichage3=canvas.create_text(L*(1/2),H*(5/20), text='Enregistrement des lots',font=(policeecriture,int(50*fontsize)))
    
    Textenomlot=canvas.create_text(L*(22/40),H*(21/40),text='Nom du lot', font=(policeecriture,int(20*fontsize)))
   
    Textequantite=canvas.create_text(L*(12/40),H*(21/40),text='Quantité', font=(policeecriture,int(20*fontsize)))
   
    Titrerecapitulatif=canvas.create_text(L*(3/20),H*(2/20),text='RECAPITULATIF DES LOTS', font=(policeecriture,int(20*fontsize)))

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
    BoutonRetourMenuPrincipal.place_forget()
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
    carre=math.ceil(math.sqrt(nbcase))
    Grille(carre)
    nom=canvas.create_text(L*(8/10),H*(4/16),text='Nom', font=(policeecriture,int(30*fontsize)))
    prenom=canvas.create_text(L*(8/10),H*(6/16),text='Prénom', font=(policeecriture,int(30*fontsize)))
    prixtotal=canvas.create_text(L*(8/10),H*(1/8),text='PRIX TOTAL', font=(policeecriture,int(30*fontsize)))
    calcprix=canvas.create_text(L*(8/10),H*(3/16),text=str((nbticket)*prix)+' €', font=(policeecriture,int(30*fontsize)))
    adresse=canvas.create_text(L*(8/10),H*(8/16),text='Mail', font=(policeecriture,int(30*fontsize)))
    cocheimpossible=canvas.create_text(L*(16/20) ,H*(5/32) ,text='Déjà coché', font=(policeecriture,int(20*fontsize)), fill=colorerror)
    #Boutons à ajouter
    BoutonRetour.place(x=L*(70/100),y=H*(7/8))
    BoutonValider.place(x=L*(31/40),y=H*(60/100))
    BoutonEffectuerTirage.place(x=L*(31/40),y=H*(7/8))
    BoutonOption.place(x=L*(9/10),y=H*(1/20))
    #Boutons à supprimer
    BoutonRetourMenuPrincipal.place_forget()
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
    emailconfirmation=canvas.create_text((L*(35/40)),H*(9/16),text='Emails envoyés', font=(policeecriture,int(15*fontsize)), fill=colorok)
    #Label à ajouter
    texteresultat.place(x=L*(2/10),y=H*(4/10))
    #Boutons à ajouter
    BoutonRetourMenuPrincipal.place(x=L*(8/10),y=H*(1/8))
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
    texteconfirmation=canvas.create_text((L*(20/40)),H*(40/100),text='Confirmation', font=(policeecriture,int(40*fontsize)))
    confenvoie=canvas.create_text((L*(20/40)),H*(45/100),text='Si une tombola a déjà été créée, celle-ci sera supprimée', font=(policeecriture,int(15*fontsize)))
    BoutonValider.place(x=6*L/10,y=H/2)
    BoutonRetour.place(x=4*L/10,y=H/2)
    EntreOptionmail.place_forget()
    EntreOptionmdp.place_forget()
    EntreOptioncodevalidation.place_forget()
    BoutonOption.place(x=L*(9/10),y=H*(1/20))
def AffichageMenuConfirmation2():
    texteconfirmation2=canvas.create_text((L*(20/40)),H*(40/100),text='Confirmation', font=(policeecriture,int(40*fontsize)))
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
    Texteoption=canvas.create_text((L*(20/40)),H*(30/100),text='Options', font=(policeecriture,int(40*fontsize)))
    
    #Bouton à ajouter
    BoutonRetour.place(x=4*L/10,y=2*H/3)
    BoutonValider.place(x=6*L/10,y=2*H/3)
    #Entrées à ajouter
    EntreOptionmail.place(x=L*(40/100),y=H*(40/100))
    EntreOptionmdp.place(x=L*(40/100),y=H*(45/100))
    EntreOptioncodevalidation.place(x=L*(40/100),y=H*(50/100))
    
    
    BoutonOption.place_forget()
    BoutonRetourMenuPrincipal.place_forget()
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
    l=[]                                                    # ligne 
    for i in L:
        l.append(i.replace('\n',''))
    return(l)

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
    if (len(listenom)) > (len(listelot)) :
        for i in range(len(listelot)):
            L_finale.append(listenom[i]+' a gagne '+listelot[i]+' grâce à la case numéro: '+ listecase[i]+'\n')
    else:
        for i in range(len(listenom)):
            L_finale.append(listenom[i]+' a gagne '+listelot[i]+' grâce à la case numéro: '+ listecase[i]+'\n') 
    L_finale.sort()        
    for result in L_finale:                                           #on écrit le nom des personnes et leur lot dans
        fichier = open("TIPE/resultats.txt", "a")  #un fichier texte
        fichier.write(result)
        fichier.close()

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
    listenom=[]
    for i in listeinfo:
        listenom.append(cherchernoms(i))

def trouvercase(str): 
    array = re.findall(r'[0-9]+', str) 
    return array 

def associerlisteinfo():
    global listeinfo, listecase
    listeinfo=[]
    listecase=[]
    lenumero=[]
    lesnumero=[]
    fichier = open("TIPE/informations.txt", "r")        #lit tous les noms et prénoms dans le fichier
    ligne = fichier.readline()                                     # texte et les ajoute dans une liste
    fichier.close                                
    while ligne:
        if cherchernoms(ligne)!=None:
            listeinfo.append (ligne)
            ligne = fichier.readline()
        else :
            listecase.append(ligne)
            ligne = fichier.readline()
    listeinfo=suppassageligne(listeinfo)
    listecase=suppassageligne(listecase)
    for i in listecase:
        lesnumero.append(trouvercase(i))
    for listenum in lesnumero:
        for i in listenum:
            lenumero.append(i)
    for i in range (len(listeinfo)):
        listeinfo[i]+=' '+lenumero[i]
        
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
        fichier.write(str(numerocase)+' ')
    fichier.write('\n')
    for i in range (nbticket):
        fichier.write(txtnom.get()+ ' ')
        fichier.write(txtprenom.get() + ' ')
        fichier.write(txtmail.get()+'\n')
        fichier.close

def Enregistrerlot():
    fichier = open("TIPE/lot.txt", "a")       #écrit les lots dans un fichier texte
    for i in range (int(txtquantite.get())):
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
    listemail=[]
    for i in listeinfo:
        listemail.append(cherchermail(i))

def associerlistecase():
    global listecase
    listecase=[]
    for i in listeinfo:
        listecase.append(trouvercase(i)[0])

canvas.bind('<Button-1>',Clic)
canvas.focus_set()

while start:
    canvas.delete(tk.ALL)
    Affichage()
    Fenetre.update()