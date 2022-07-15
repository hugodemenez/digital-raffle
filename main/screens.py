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
        self.canvas = tk.canvas(self.Window, width= self.LENGTH, height= self.HEIGHT, bg=self.BACKGROUND)
        self.canvas.pack()
        self.state='Menu'
        self.kL=L/1536
        self.kH=H/864
        self.nbCase=0
        
        ## Lists
        self.reg=[]
        self.listeNom=[]
        self.listeLot=[]
        self.listeMail=[]
        self.listeInfo=[] 
        self.registreAttente=[]
        self.registrePermanent=[]
        self.listeCase=[]
        
        
        
        # Tkinter variables
        self.LABEL_NB_CASE=tk.StringVar()
        self.LABEL_NOM=tk.StringVar()
        self.LABEL_PRENOM=tk.StringVar()
        self.LABEL_MAIL=tk.StringVar()
        self.LABEL_PRIX=tk.StringVar()
        self.LABEL_OPTION_MAIL=tk.StringVar()
        self.LABEL_OPTION_MDP=tk.StringVar()
        self.LABEL_CODE_VALIDATION=tk.StringVar()
        self.LABEL_CASE=tk.StringVar()
        self.LABEL_QUANTITE=tk.StringVar()
        self.LABEL_NOM_LOT=tk.StringVar()
        

        # Tkinter settings
        ## Creation du texte
        self.LABEL_RESUME_LOT=tk.Text(self.canvas,width=str(int(35*self.FONTSIZE)),height='10', font=(self.FONT, int(15**self.FONTSIZE)))
        self.LABEL_RESULTAT=tk.Text(self.canvas,width=str(int(100*self.FONTSIZE)),height='10', font=(self.FONT, int(15**self.FONTSIZE)))
        
        ## Creation des boutons :
        self.BOUTON_QUITTER=tk.Button(self.canvas,text='Quitter',font=(self.FONT, int(15*self.FONTSIZE)),bg=self.COLOR_BOUTON,command=self.Quitter)
        self.BOUTON_RETOUR=tk.Button(self.canvas,text='Retour',font=(self.FONT, int(15*self.FONTSIZE)),bg=self.COLOR_BOUTON,command=self.Retour)
        self.BOUTON_VALIDER=tk.Button(self.canvas,text='Valider',font=(self.FONT, int(15*self.FONTSIZE)),bg=self.COLOR_BOUTON,command=self.Valider)
        self.BOUTON_OPTION=tk.Button(self.canvas,text='Options',font=(self.FONT, int(15*self.FONTSIZE)),bg=self.COLOR_BOUTON,command=self.Option)
        self.BOUTON_HOME=tk.Button(self.canvas,text='Retour au Menu Principal',font=(self.FONT, int(15*self.FONTSIZE)),bg=self.COLOR_BOUTON,command=self.back_main_menu)
        self.BOUTON_CONTINUER=tk.Button(self.canvas,text='Continuer',font=(self.FONT, int(15*self.FONTSIZE)),bg=self.COLOR_BOUTON,command=self.Continuer)
        self.BOUTON_SUPPRIMER_LOT=tk.Button(self.canvas,text='Supprimer le dernier lot',font=(self.FONT,int(15*self.FONTSIZE)),bg=self.COLOR_BOUTON,command=self.supprimerlot)
        self.BOUTON_EFFECTUER_TIRAGE=tk.Button(self.canvas,text='Effectuer le tirage',font=(self.FONT,int(15*self.FONTSIZE)),bg=self.COLOR_BOUTON,command=self.commandself.BOUTON_EFFECTUER_TIRAGE)
        self.BOUTON_VALIDER_LOT=tk.Button(self.canvas,text='Valider le lot',font=(self.FONT, int(15*self.FONTSIZE)),bg=self.COLOR_BOUTON,command=self.Valider)
        self.BOUTON_ENVOIE_MAIL=tk.Button(self.canvas,text='Envoyer un mail aux gagnants',font=(self.FONT, int(15*self.FONTSIZE)),bg=self.COLOR_BOUTON,command=self.envoiemail)

        ## Création d'entrées
        Entrequantite= tk.Entry(self.Window,bg=self.BACKGROUND,textvariable=self.LABEL_QUANTITE,width=5,bd=3,font=(self.FONT, int(45*self.FONTSIZE)))
        Entrenomlot= tk.Entry(self.Window,bg=self.BACKGROUND,bd=3,textvariable=self.LABEL_NOM_LOT,font=(self.FONT, int(45*self.FONTSIZE)))
        Entrenbcase=tk.Entry(self.Window,bg=self.BACKGROUND,textvariable=self.LABELNBCASE,width=5,bd=3,font=(self.FONT, int(45*self.FONTSIZE)))
        Entreprixcase=tk.Entry(self.Window,bg=self.BACKGROUND,textvariable=self.LABEL_PRIX,width=5,bd=3,font=(self.FONT, int(45*self.FONTSIZE)))
        Entrenom=tk.Entry(self.Window,bg=self.BACKGROUND,textvariable=self.LABEL_NOM,width=30,bd=3,font=(self.FONT, int(20*self.FONTSIZE)))
        Entreprenom=tk.Entry(self.Window,bg=self.BACKGROUND,textvariable=self.LABEL_PRENOM,width=30,bd=3,font=(self.FONT, int(20*self.FONTSIZE)))
        Entremail=tk.Entry(self.Window,bg=self.BACKGROUND,textvariable=self.LABEL_MAIL,width=30,bd=3,font=(self.FONT, int(20*self.FONTSIZE)))
        EntreOptionmail=tk.Entry(self.Window,bg=self.BACKGROUND,textvariable=self.LABEL_OPTION_MAIL,width=30,bd=3,font=(self.FONT, int(20*self.FONTSIZE)))
        EntreOptionmdp=tk.Entry(self.Window,bg=self.BACKGROUND,textvariable=self.LABEL_OPTION_MDP,width=30,bd=3,font=(self.FONT, int(20*self.FONTSIZE)),show='*')
        EntreOptioncodevalidation=tk.Entry(self.Window,bg=self.BACKGROUND,textvariable=self.LABEL_CODE_VALIDATION,width=30,bd=3,font=(self.FONT, int(20*self.FONTSIZE)))

        #Paramètre des entrées
        EntreOptionmail.bind('<FocusIn>', self.on_entry_click)
        EntreOptionmail.bind('<FocusOut>', self.on_focusout)
        EntreOptionmail.insert(0, 'Entrez votre adresse mail')
        EntreOptionmdp.bind('<FocusIn>', self.on_entry_click2)
        EntreOptionmdp.bind('<FocusOut>', self.on_focusout2)
        EntreOptionmdp.insert(0, 'Entrez votre mot de passe')

        EntreOptioncodevalidation.bind('<FocusIn>', self.on_entry_click3)
        EntreOptioncodevalidation.bind('<FocusOut>', self.on_focusout3)
        EntreOptioncodevalidation.insert(0, 'clé de validation')




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
        if self.state=='Menu2':
            if self.LABELNBCASE.get()!='' and self.LABEL_PRIX.get()!='':
                nbcase=int(self.LABELNBCASE.get())
                prix=int(self.LABEL_PRIX.get())
                etat='Menu3'
        if self.state=='Menu3':
            if self.LABEL_QUANTITE.get()!='' and self.LABEL_NOM_LOT.get()!='':
                self.Enregistrerlot()
                self.Lecturedeslots()
                self.Enregistrertombola()
        if self.state=='Menu4':
            if self.LABEL_NOM.get()!='' and self.LABEL_PRENOM.get()!='':
                nom=self.LABEL_NOM.get()
                prenom=self.LABEL_PRENOM.get()
                mail=self.LABEL_MAIL.get()
                self.Enregistrement()
                self.LABEL_NOM.set('')
                self.LABEL_PRENOM.set('')
                self.LABEL_MAIL.set('')
                nbticket=0
                for i in registreattente:
                    reg.append(i)
                registreattente=[]
                self.Enregistrertombola()
        if self.state=='MenuConfirmation':
                self.SupprimerTombola()
                self.Creer()
        if self.state=='MenuConfirmation2':
            self.Creer()
            f = open("TIPE/resultats.txt", 'r+')
            if f.read()=='':
                self.effectuertirage()
        if self.state=='MenuOption':
            if EntreOptioncodevalidation.get()=='1234':
                mailorganisateur=EntreOptionmail.get()
                mdporganisateur=EntreOptionmdp.get()
                optioncodevalidation.set("Le compte mail a été modifié")
            else:
                optioncodevalidation.set("Mauvais mot de passe")
                
    def choose(self):
        regcompte=int(self.LABEL_CASE.get())
        if regcompte not in reg: #Verifie que l'on n'a pas deja coché la case
            reg.append(int(self.LABEL_CASE.get()))
            nbticket+=1
            self.LABEL_CASE.set('')
            self.Enregistrertombola()
            colorerror='#ffefd8'
        else:
            colorerror='red'
            self.LABEL_CASE.set('')

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
        supprlot=self.suppassageligne(supprlot)
        supprlot=self.list_filter(supprlot,supprlot[len(supprlot)-1])
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
        registre=self.retirersautligne(ligne)
        self.LABEL_RESUME_LOT.delete(0.0, tk.END)
        while ligne:
            if registre==retirersautligne(ligne):
                quantite+=1
                ligne = fichier.readline()
            else :
                self.LABEL_RESUME_LOT.insert(tk.END,str(quantite)+retirersautligne(registre)+'\n')
                registre=ligne
                quantite=0
        if quantite!=0:
            self.LABEL_RESUME_LOT.insert(tk.END,str(quantite)+retirersautligne(registre)+'\n')
        else :
            self.LABEL_RESUME_LOT.insert(tk.END,retirersautligne(registre))
            
            
    def commandself.BOUTON_EFFECTUER_TIRAGE():
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
            
    

    def Grille(x):
        carreau=[[self.canvas.create_rectangle(i*H/x,j*H/x,(i+1)*H/x,(j+1)*H/x,fill=colorbg) for i in range(x)] for j in range(x)]
        Framecoche(carre)
        chiffres=[[self.canvas.create_text((2*i+1)*(H/(x*2)),H/(x*2)*(2*j+1),text=(i+1)+(x*j),font=(self.FONT, int((15*fontsize)*0.1/nbcase)))for i in range(x)]for j in range(x)]

    def AffichageMenu(self):
        titre=self.canvas.create_text(L/2,H*(1/4),text='TOMBOLA',font=police)
        creer=self.canvas.create_text(L*(1/2),H*(3/7),text='Créer une Tombola', font=(self.FONT, int(30*fontsize)))
        ouvrir=self.canvas.create_text(L*(1/2),H*(4/7),text='Ouvrir une Tombola', font=(self.FONT, int(30*fontsize)))
        afficheresult=self.canvas.create_text(L*(1/2),H*(5/7),text='Afficher les résultats', font=(self.FONT, int(30*fontsize)))
        
        #Boutons à ajouter
        self.BOUTON_QUITTER.place(x=L*(9/10),y=H*(7/8))
        self.BOUTON_OPTION.place(x=L*(9/10),y=H*(1/20))
        #Boutons à supprimer

        self.BOUTON_RETOUR.place_forget()
        self.BOUTON_VALIDER.place_forget()
        self.BOUTON_HOME.place_forget()
        self.BOUTON_ENVOIE_MAIL.place_forget()
        #Entrées à supprimer
        Entrenbcase.place_forget()
        Entreprixcase.place_forget()
        self.LABEL_RESULTAT.place_forget()
        EntreOptionmail.place_forget()
        EntreOptionmdp.place_forget()
        EntreOptioncodevalidation.place_forget()
    def AffichageMenu2(self):
        titrenbcase=self.canvas.create_text(L*(1/4),H*(3/7), text='Entrer nombre de cases',font=(self.FONT,int(45*fontsize)))
        titrenbcase=self.canvas.create_text(L*(1/4),H*(10/21), text='(nombre minimum de cases pour la tombola)',font=(self.FONT,int(15*fontsize)))
        titreprix=self.canvas.create_text(L*(3/4),H*(3/7), text='Prix de la case (unitaire)',font=(self.FONT,int(40*fontsize)))
        

        #Boutons à ajouter
        self.BOUTON_VALIDER.place(x=L*(5/10),y=H*(7/8))
        self.BOUTON_OPTION.place(x=L*(9/10),y=H*(1/20))
        #Boutons à supprimer
        self.BOUTON_HOME.place_forget()
        self.BOUTON_CONTINUER.place_forget()
        self.BOUTON_SUPPRIMER_LOT.place_forget()
        self.BOUTON_VALIDER_LOT.place_forget()
        self.BOUTON_RETOUR.place_forget()
        #Entrées à ajouter
        Entreprixcase.place(x=L*(70/100),y= H*(55/100))
        Entrenbcase.place(x=L*(20/100),y=H*(55/100))
        #Entrées à supprimer
        Entrenomlot.place_forget()
        Entrequantite.place_forget()
        self.LABEL_RESUME_LOT.place_forget()
        EntreOptionmail.place_forget()
        EntreOptionmdp.place_forget()
        EntreOptioncodevalidation.place_forget()
        
    def AffichageMenu3(self):
        Titreaffichage3=self.canvas.create_text(L*(1/2),H*(5/20), text='Enregistrement des lots',font=(self.FONT,int(50*fontsize)))
        
        Textenomlot=self.canvas.create_text(L*(22/40),H*(21/40),text='Nom du lot', font=(self.FONT,int(20*fontsize)))
    
        Textequantite=self.canvas.create_text(L*(12/40),H*(21/40),text='Quantité', font=(self.FONT,int(20*fontsize)))
    
        Titrerecapitulatif=self.canvas.create_text(L*(3/20),H*(2/20),text='RECAPITULATIF DES LOTS', font=(self.FONT,int(20*fontsize)))

        self.LABEL_RESUME_LOT.place(x=L*(5/100),y=H*(3/20))
        #Entrées à ajouter
        Entrenomlot.place(x=L*(8/20),y=H*(23/40))
        Entrequantite.place(x=L*(5/20),y=H*(23/40))
        #Boutons à ajouter
        self.BOUTON_VALIDER_LOT.place(x=L*(82/100),y=H*(55/100))
        self.BOUTON_CONTINUER.place(x=L*(5/10),y=H*(7/8))
        self.BOUTON_SUPPRIMER_LOT.place(x=L*(16/20),y=H*(65/100))
        self.BOUTON_OPTION.place(x=L*(9/10),y=H*(1/20))
        #Boutons à supprimer
        self.BOUTON_HOME.place_forget()
        self.BOUTON_EFFECTUER_TIRAGE.place_forget()
        self.BOUTON_VALIDER.place_forget()
        self.BOUTON_RETOUR.place_forget()
        #Entrées à supprimer
        Entrenbcase.place_forget()
        Entreprixcase.place_forget()
        Entrenom.place_forget()
        Entreprenom.place_forget()
        Entremail.place_forget()
        EntreOptionmail.place_forget()
        EntreOptionmdp.place_forget()
        EntreOptioncodevalidation.place_forget()
        
    def AffichageMenu4(self):
        global carre
        carre=math.ceil(math.sqrt(nbcase))
        Grille(carre)
        nom=self.canvas.create_text(L*(8/10),H*(4/16),text='Nom', font=(self.FONT,int(30*fontsize)))
        prenom=self.canvas.create_text(L*(8/10),H*(6/16),text='Prénom', font=(self.FONT,int(30*fontsize)))
        prixtotal=self.canvas.create_text(L*(8/10),H*(1/8),text='PRIX TOTAL', font=(self.FONT,int(30*fontsize)))
        calcprix=self.canvas.create_text(L*(8/10),H*(3/16),text=str((nbticket)*prix)+' €', font=(self.FONT,int(30*fontsize)))
        adresse=self.canvas.create_text(L*(8/10),H*(8/16),text='Mail', font=(self.FONT,int(30*fontsize)))
        cocheimpossible=self.canvas.create_text(L*(16/20) ,H*(5/32) ,text='Déjà coché', font=(self.FONT,int(20*fontsize)), fill=colorerror)
        #Boutons à ajouter
        self.BOUTON_RETOUR.place(x=L*(70/100),y=H*(7/8))
        self.BOUTON_VALIDER.place(x=L*(31/40),y=H*(60/100))
        self.BOUTON_EFFECTUER_TIRAGE.place(x=L*(31/40),y=H*(7/8))
        self.BOUTON_OPTION.place(x=L*(9/10),y=H*(1/20))
        #Boutons à supprimer
        self.BOUTON_HOME.place_forget()
        self.BOUTON_CONTINUER.place_forget()
        self.BOUTON_SUPPRIMER_LOT.place_forget()
        self.BOUTON_VALIDER_LOT.place_forget()
        self.BOUTON_ENVOIE_MAIL.place_forget()
        #Entrées à ajouter
        Entrenom.place(x=L*(70/100),y=H*(28/100))
        Entreprenom.place(x=L*(70/100),y=H*(40/100))
        Entremail.place(x=L*(70/100),y=H*(53/100))
        #Entrées à supprimer
        Entrenomlot.place_forget()
        Entrequantite.place_forget()
        self.LABEL_RESUME_LOT.place_forget()
        self.LABEL_RESULTAT.place_forget()
        EntreOptionmail.place_forget()
        EntreOptionmdp.place_forget()
        EntreOptioncodevalidation.place_forget()
        
    def AffichageMenu5(self):
        emailconfirmation=self.canvas.create_text((L*(35/40)),H*(9/16),text='Emails envoyés', font=(self.FONT,int(15*fontsize)), fill=colorok)
        #Label à ajouter
        self.LABEL_RESULTAT.place(x=L*(2/10),y=H*(4/10))
        #Boutons à ajouter
        self.BOUTON_HOME.place(x=L*(8/10),y=H*(1/8))
        self.BOUTON_ENVOIE_MAIL.place(x=(L*(8/10)),y=H*(5/8))
        self.BOUTON_OPTION.place(x=L*(9/10),y=H*(1/20))
        #Boutons à supprimer
        self.BOUTON_RETOUR.place_forget()
        self.BOUTON_VALIDER.place_forget()
        self.BOUTON_EFFECTUER_TIRAGE.place_forget()
        #Entrées à supprimer
        Entrenom.place_forget()
        Entreprenom.place_forget()
        Entremail.place_forget()
        EntreOptionmail.place_forget()
        EntreOptionmdp.place_forget()
        EntreOptioncodevalidation.place_forget()
        
    def AffichageMenuConfirmation(self):
        texteconfirmation=self.canvas.create_text((L*(20/40)),H*(40/100),text='Confirmation', font=(self.FONT,int(40*fontsize)))
        confenvoie=self.canvas.create_text((L*(20/40)),H*(45/100),text='Si une tombola a déjà été créée, celle-ci sera supprimée', font=(self.FONT,int(15*fontsize)))
        self.BOUTON_VALIDER.place(x=6*L/10,y=H/2)
        self.BOUTON_RETOUR.place(x=4*L/10,y=H/2)
        EntreOptionmail.place_forget()
        EntreOptionmdp.place_forget()
        EntreOptioncodevalidation.place_forget()
        self.BOUTON_OPTION.place(x=L*(9/10),y=H*(1/20))
        
    def AffichageMenuConfirmation2(self):
        texteconfirmation2=self.canvas.create_text((L*(20/40)),H*(40/100),text='Confirmation', font=(self.FONT,int(40*fontsize)))
        #Bouton à ajouter
        self.BOUTON_VALIDER.place(x=6*L/10,y=H/2)
        self.BOUTON_RETOUR.place(x=4*L/10,y=H/2)
        self.BOUTON_OPTION.place(x=L*(9/10),y=H*(1/20))
        #Entrées à supprimer
        Entrenom.place_forget()
        Entreprenom.place_forget()
        Entremail.place_forget()
        self.BOUTON_EFFECTUER_TIRAGE.place_forget()
        EntreOptionmail.place_forget()
        EntreOptionmdp.place_forget()
        EntreOptioncodevalidation.place_forget()
        
    def AffichageOption(self):
        Texteoption=self.canvas.create_text((L*(20/40)),H*(30/100),text='Options', font=(self.FONT,int(40*fontsize)))
        
        #Bouton à ajouter
        self.BOUTON_RETOUR.place(x=4*L/10,y=2*H/3)
        self.BOUTON_VALIDER.place(x=6*L/10,y=2*H/3)
        #Entrées à ajouter
        EntreOptionmail.place(x=L*(40/100),y=H*(40/100))
        EntreOptionmdp.place(x=L*(40/100),y=H*(45/100))
        EntreOptioncodevalidation.place(x=L*(40/100),y=H*(50/100))
        
        
        self.BOUTON_OPTION.place_forget()
        self.BOUTON_HOME.place_forget()
        self.BOUTON_CONTINUER.place_forget()
        self.BOUTON_SUPPRIMER_LOT.place_forget()
        self.BOUTON_EFFECTUER_TIRAGE.place_forget()
        self.BOUTON_VALIDER_LOT.place_forget()
        self.BOUTON_ENVOIE_MAIL.place_forget()
        Entrequantite.place_forget()
        Entrenomlot.place_forget()
        Entrenbcase.place_forget()
        Entreprixcase.place_forget()
        Entrenom.place_forget()
        Entreprenom.place_forget()
        Entremail.place_forget()
        self.LABEL_RESUME_LOT.place_forget()
        self.LABEL_RESULTAT.place_forget()
        
    def Lecturedeslots(self):
        if self.LABEL_NOM_LOT.get()!='':
            leclot=self.LABEL_NOM_LOT.get()
            quantlot=self.LABEL_QUANTITE.get()
            self.LABEL_RESUME_LOT.insert(tk.END,quantlot+leclot+'\n')
            self.LABEL_NOM_LOT.set('')
            self.LABEL_QUANTITE.set('')

    def suppassageligne(L):                                     # enlève les \n d'une liste pour ne pas sauter une           
        l=[]                                                    # ligne 
        for i in L:
            l.append(i.replace('\n',''))
        return(l)

    def Affichage(self):
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
    def Creer(self):
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
                            cochage=((self.canvas.create_rectangle((i*H/x),j*H/x,(i+1)*H/x,(j+1)*H/x ,fill='black')))
        for w in registreattente :
            for j in range (x):
                for i in range (x):
                    compteur=(1+i)+(x*j)
                    if compteur==w: #Localise la case à cocher
                            cochage=((self.canvas.create_rectangle((i*H/x),j*H/x,(i+1)*H/x,(j+1)*H/x ,fill='#6ab04c')))

    def lectureresultat(self):
        global affichageresult
        self.LABEL_RESULTAT.delete(0.0,tk.END)
        affichageresult=''
        fichier = open("TIPE/resultats.txt", "r")        #lit tous les noms et prénoms dans le fichier
        ligne = fichier.readline()                                     # texte et les ajoute dans une liste
        fichier.close                                
        while ligne:
            affichageresult=affichageresult+ligne
            ligne = fichier.readline()
        self.LABEL_RESULTAT.insert(0.0,affichageresult)

    def effectuertirage(self):
        global affichageresult
        self.LABEL_RESULTAT.delete(0.0,tk.END)
        affichageresult=''
        Tirageautomatique()
        fichier = open("TIPE/resultats.txt", "r")        #lit tous les noms et prénoms dans le fichier
        ligne = fichier.readline()                                     # texte et les ajoute dans une liste
        fichier.close                                
        while ligne:
            affichageresult=affichageresult+ligne
            ligne = fichier.readline()
        self.LABEL_RESULTAT.insert(0.0,affichageresult)
        
    def Ouvrir(self):
        global etat
        if etat=='Menu':
            chargetombola()
            etat='Menu4'

    def SupprimerTombola (self):
        global reg
        reg=[]
        self.LABEL_RESUME_LOT.delete(0.0,tk.END)
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

    def Tirageautomatique(self):
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
        
    def chargetombola(self):
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
        self.LABEL_RESUME_LOT.delete(0.0, tk.END)
        while ligne:
            if registre==retirersautligne(ligne):
                quantite+=1
                ligne = fichier.readline()
            else :
                self.LABEL_RESUME_LOT.insert(tk.END,str(quantite)+retirersautligne(registre)+'\n')
                registre=retirersautligne(ligne)
                quantite=0
        self.LABEL_RESUME_LOT.insert(tk.END,str(quantite)+retirersautligne(registre)+'\n')

    def associerlistenom(self):
        global listenom
        listenom=[]
        for i in listeinfo:
            listenom.append(cherchernoms(i))

    def trouvercase(str): 
        array = re.findall(r'[0-9]+', str) 
        return array 

    def associerlisteinfo(self):
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
            
    def associerlistelot(self):
        global listelot
        listelot=[]
        fichier = open("TIPE/lot.txt", "r")           #lit tous les lots dans le fichier texte 
        ligne = fichier.readline()                                        #et les ajoute dans une liste
        fichier.close                                                     
        while ligne:
            listelot.append (ligne)
            ligne = fichier.readline()
        listelot=suppassageligne(listelot)

    def Enregistrement(self):
        fichier = open("TIPE/informations.txt", "a")       #écrit les noms dans un fichier texte
        for numerocase in registreattente:
            fichier.write(str(numerocase)+' ')
        fichier.write('\n')
        for i in range (nbticket):
            fichier.write(self.LABEL_NOM.get()+ ' ')
            fichier.write(self.LABEL_PRENOM.get() + ' ')
            fichier.write(self.LABEL_MAIL.get()+'\n')
            fichier.close

    def Enregistrerlot(self):
        fichier = open("TIPE/lot.txt", "a")       #écrit les lots dans un fichier texte
        for i in range (int(self.LABEL_QUANTITE.get())):
            fichier.write(self.LABEL_NOM_LOT.get()+'\n')
        fichier.close

    def Enregistrertombola(self):
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

    def associerlistemail(self):
        global listemail
        listemail=[]
        for i in listeinfo:
            listemail.append(cherchermail(i))

    def associerlistecase(self):
        global listecase
        listecase=[]
        for i in listeinfo:
            listecase.append(trouvercase(i)[0])

    self.canvas.bind('<Button-1>',Clic)
    self.canvas.focus_set()

    while start:
        self.canvas.delete(tk.ALL)
        Affichage()
        Fenetre.update()