# -*- coding: utf-8 -*-

#Importations 
import pandas as pd
import matplotlib.pyplot as plt
# from sqlalchemy import create_engine 



#Traitement des données récoltées

def categorisationVax(personne): #Permet de définir si la personne est considérée comme pro-vax, neutre ou anti-vax

    #Catégories retenues
    vax = 0
    usage_vaccin = 0
    pass_vaccin = 0
    
    #Coefficient des catégorie
    c_vax = 5
    c_usage_vaccin = 4
    c_pass_vaccin = 3
    c_somme = c_vax + c_usage_vaccin + c_pass_vaccin

    #Positionnement pro/anti
    if personne['Vous vous considérez comme :'] == '"Pro-vax"':
        vax = 1
    elif personne['Vous vous considérez comme :'] == 'Neutre':
        vax = 0
    elif personne['Vous vous considérez comme :'] == '"Anti-vax"':
        vax = -1
       
    #Positionnement usage du vaccin
    if personne["Quel est votre positionnement par rapport à l'usage actuel des vaccins contre le Covid ?"] == "J'approuve totalement leur usage":
        usage_vaccin = 2
    elif personne["Quel est votre positionnement par rapport à l'usage actuel des vaccins contre le Covid ?"] == "J'approuve plutôt leur usage":
        usage_vaccin = 1
    elif personne["Quel est votre positionnement par rapport à l'usage actuel des vaccins contre le Covid ?"] == "Je n'approuve que partiellement leur usage":
        usage_vaccin = 0
    elif personne["Quel est votre positionnement par rapport à l'usage actuel des vaccins contre le Covid ?"] == "Je désapprouve plutôt leur usage":
        usage_vaccin = -1
    elif personne["Quel est votre positionnement par rapport à l'usage actuel des vaccins contre le Covid ?"] == "Je désapprouve totalement leur usage":
        usage_vaccin = -2
        
    #Positionnement pass vaccinal
    if personne["Quel est votre positionnement par rapport aux décisions gouvernementales prises depuis le début de la pandémie concernant le pass vaccinal ?"] == "J'approuve totalement ces décisions":
        pass_vaccin = 2
    elif personne["Quel est votre positionnement par rapport aux décisions gouvernementales prises depuis le début de la pandémie concernant le pass vaccinal ?"] == "J'approuve plutôt ces décisions":
        pass_vaccin = 1
    elif personne["Quel est votre positionnement par rapport aux décisions gouvernementales prises depuis le début de la pandémie concernant le pass vaccinal ?"] == "Je n'approuve que partiellement ces décisions":
        pass_vaccin = 0
    elif personne["Quel est votre positionnement par rapport aux décisions gouvernementales prises depuis le début de la pandémie concernant le pass vaccinal ?"] == "Je désapprouve plutôt ces décisions":
        pass_vaccin = -1
    elif personne["Quel est votre positionnement par rapport aux décisions gouvernementales prises depuis le début de la pandémie concernant le pass vaccinal ?"] == "Je désapprouve totalement ces décisions":
        pass_vaccin = -2
        
    #Renvoie de la détermination
    score = c_vax/c_somme *vax + c_usage_vaccin/c_somme *usage_vaccin/2 + c_pass_vaccin/c_somme * pass_vaccin/2
    
    if -1 <= score < -0.25:
        return "Anti-Vax"
    elif 0.25 < score <= 1:
        return "Pro-vax"
    else:
        return "Neutre"
  
  
def categorisationPolitque(personne): #Permet de placer la personne sur l'échiquier politique
    positionnement = personne["Quel est votre positionnement politique ? (Optionnel)"]
    if positionnement in [0, 1] :
        return "Extrème-gauche"
    elif positionnement in [2, 3]:
        return "Gauche"
    elif positionnement in [4, 5, 6]:
        return "Centre"
    elif positionnement in [7, 8]:
        return "Droite"
    elif positionnement in [9, 10]:
        return "Extrème-droite"
    
    
def categorisationEntourage(personne): #Permet de définir si l'entourage de la personne est à tendance pro-vax, neutre ou anti-vax
    
    #Point de catégorisation
    masque = 0
    usage_vaccin = 0 
    pass_vaccin = 0
    vax = 0
    
    #Positionnement masque 
    if personne["Votre entourage est majoritairement : (m)"] == "D'accord avec l'obligation de port du masque dans les lieux ":
        masque = 1
    elif personne["Votre entourage est majoritairement : (m)"] == "Neutre par rapport à l'obligation de port du masque dans les lieux publics":
        masque = 0
    elif personne["Votre entourage est majoritairement : (m)"] == "Pas d'accord avec l'obligation de port du masque dans les lieux publics":
        masque = -1
    
    #Positionnement usage du vaccin
    if personne["Votre entourage est majoritairement : (v)"] == "D'accord avec l'usage actuel des vaccins":
        usage_vaccin = 1
    elif personne["Votre entourage est majoritairement : (v)"] == "Neutre par rapport à l'usage actuel des vaccins":
        usage_vaccin = 0 
    elif personne["Votre entourage est majoritairement : (v)"] == "Pas d'accord avec l'usage actuel des vaccins":
        usage_vaccin = -1
    
    #Positionnement pass vaccinal
    if personne["Votre entourage est majoritairement : (ps)"] == "D'accord avec le pass vaccinal":
        pass_vaccin = 1
    elif personne["Votre entourage est majoritairement : (ps)"] == "Neutre par rapport au pass vaccinal":
        pass_vaccin = 0
    elif personne["Votre entourage est majoritairement : (ps)"] == "Pas d'accord avec le pass vaccinal":
        pass_vaccin = -1
    
    #Positionnement pro/anti
    if personne['Votre entourage est majoritairement :'] == '"Pro-vax"':
        vax = 1
    elif personne['Votre entourage est majoritairement :'] == 'Neutre':
        vax = 0
    elif personne['Votre entourage est majoritairement :'] == '"Anti-vax"':
        vax = -1
    
    #Retour sur l'entourage majoritaire
    score = (masque + usage_vaccin + pass_vaccin + vax) /4
    
    if -1 <= score < -0.25:
        return "Anti-Vax"
    elif 0.25 < score <= 1:
        return "Pro-vax"
    else:
        return "Neutre"
  

def categorisationPassifCovid(personne): #Permet de définir à quel point une personne a été impacté par la covid-19
    score = 0
    
    if personne['Vous connaissez ou avez connu :'] == 'Un proche ayant contracté une forme grave de Covid-19':
        score += 1
    if personne['Vous connaissez ou avez connu :'] == "Le décès d'un proche dû au Covid-19":
        score += 3
    if personne['Pour ma part :'] == "J'ai contracté une forme grave de Covid-19 suite à une infection":
        score += 2
    
    if score == 0:
        return "Non touché"
    elif score in [1, 2]:
        return "Peu touché"
    elif score >= 3:
        return "Très touché"
       
    
def categorisationGeneMesure(personne):
    score = 0
    
    if "Je tolère le port du masque au quotidien (ne me gène pas trop sur le visage...)" in personne["Quels sont les arguments qui vous font pencher plutôt pour le port du masque ?"]:
        score += -1
    if "Le masque me gêne physiquement au quotidien (gratte, empêche de bien parler/respirer, etc.)" in personne["Quels sont les arguments qui vous font pencher plutôt contre le port du masque ?"]:
        score += 1
    if "Je pense que le vaccin a un impact positif concret pour ma protection personnelle face au Covid" in personne["Quels sont les arguments qui vous font pencher plutôt pour la vaccination au Covid-19 ?"]:
        score += -1
    if "Je pense que le vaccin obligatoire pour tous n'empiète pas ou peu sur mes libertés personnelles" in personne["Quels sont les arguments qui vous font pencher plutôt pour la vaccination au Covid-19 ?"]:
        score += -1
    if "Pour des raisons personnelles médicales (allergies, faiblesses immunitaires, etc.)" in personne["Quels sont les arguments qui vous font pencher plutôt contre la vaccination au Covid-19 ?"]:
        score += 1
    if "Je pense que le vaccin n'a pas d'impact positif concret pour ma protection personnelle face au Covid" in personne["Quels sont les arguments qui vous font pencher plutôt contre la vaccination au Covid-19 ?"]:
        score += 1
    if "Je tolère l'effet du pass sanitaire sur mes libertés personnelles provisoirement" in personne["Quels sont les arguments qui vous font pencher plutôt pour le pass vaccinal ?"]:
        score += -1
    if "Je pense que le pass sanitaire permet d'éviter des couvre-feux ou confinements" in personne["Quels sont les arguments qui vous font pencher plutôt pour le pass vaccinal ?"]:
        score += -1
    if "Le pass vaccinal m'empêche personnellement de faire ce que je souhaite au quotidien" in personne["Quels sont les arguments qui vous font pencher plutôt contre le pass vaccinal ?"]:
        score += 1
    if "Je pense que le pass vaccinal est une atteinte à ma liberté personnelle fondamentale" in personne["Quels sont les arguments qui vous font pencher plutôt contre le pass vaccinal ?"]:
        score += 1
    
    score = score/5
    
    if -1 <= score < -0.6:
        return "Pas du tout"
    elif -0.6 <= score < -0.2:
        return "Peu"
    elif -0.2 <= score < 0.2:
        return "Neutre"
    elif 0.2 <= score < 0.6:
        return "Plutôt"
    elif 0.6 <= score:
        return "Très"


def categorisationConfianceGouvernement(personne):
    score = 0
    
    if "Je fais confiance à cette mesure du gouvernement pour son intérêt dans la gestion de la pandémie" in personne["Quels sont les arguments qui vous font pencher plutôt pour le port du masque ?"]:
        score += -1
    if "Je pense que le port obligatoire du masque est une attente à nos libertés" in personne["Quels sont les arguments qui vous font pencher plutôt contre le port du masque ?"]:
        score += 1
    if "Je pense que le vaccin est et restera suffisamment inoffensif pour la santé" in personne["Quels sont les arguments qui vous font pencher plutôt pour la vaccination au Covid-19 ?"]:
        score += -1
    if "Je pense que le vaccin obligatoire pour tous n'empiète pas ou peu sur mes libertés personnelles" in personne["Quels sont les arguments qui vous font pencher plutôt pour la vaccination au Covid-19 ?"]:
        score += -1
    if "Je fais confiance au gouvernement sur les bienfaits de cette mesure" in personne["Quels sont les arguments qui vous font pencher plutôt pour la vaccination au Covid-19 ?"]:
        score += -1    
    if "Je pense que le vaccin obligatoire pour tous est une atteinte à la liberté personnelle" in personne["Quels sont les arguments qui vous font pencher plutôt contre la vaccination au Covid-19 ?"]:
        score += 1
    if "Je pense que le vaccin a été intentionnellement conçu pour réduire nos libertés" in personne["Quels sont les arguments qui vous font pencher plutôt contre la vaccination au Covid-19 ?"]:
        score += 1
    if "Je tolère l'effet du pass sanitaire sur mes libertés personnelles provisoirement" in personne["Quels sont les arguments qui vous font pencher plutôt pour le pass vaccinal ?"]:
        score += -1
    if "Je fais confiance au gouvernement sur la pertinence du pass vaccinal" in personne["Quels sont les arguments qui vous font pencher plutôt pour le pass vaccinal ?"]:
        score += -1
    if "Je pense que le pass vaccinal est une atteinte à la liberté des Français" in personne["Quels sont les arguments qui vous font pencher plutôt contre le pass vaccinal ?"]:
        score += 1
    if "Je pense que le gouvernement n'a pas à décider de ce qui est bon ou non pour nous" in personne["Quels sont les arguments qui vous font pencher plutôt contre le pass vaccinal ?"]:
        score += 1
    if "Je souhaite exprimer mon insatisfaction face au gouvernement actuel qui ne me convient pas" in personne["Quels sont les arguments qui vous font pencher plutôt contre le pass vaccinal ?"]:
        score += 1
    
    score = score/6
    
    if -1 <= score < -0.6:
        return "Très"
    elif -0.6 <= score < -0.2:
        return "Plutôt"
    elif -0.2 <= score < 0.2:
        return "Neutre"
    elif 0.2 <= score < 0.6:
        return "Peu"
    elif 0.6 <= score:
        return "Pas du tout"
    
    
def categorisationSceptiscismeMesure(personne):
    score = 0
    
    if "Je pense que le masque est utile pour freiner la propagation du virus" in personne["Quels sont les arguments qui vous font pencher plutôt pour le port du masque ?"]:
        score += -1
    if "Je pense que le port du masque protège mes proches" in personne["Quels sont les arguments qui vous font pencher plutôt pour le port du masque ?"]:
        score += -1
    if "Je pense que le masque est inoffensif pour la santé" in personne["Quels sont les arguments qui vous font pencher plutôt pour le port du masque ?"]:
        score += -1
    if "Je pense que le masque est inutile pour freiner la propagation du virus" in personne["Quels sont les arguments qui vous font pencher plutôt contre le port du masque ?"]:
        score += 1
    if "Je pense que le port du masque ne protège pas mes proches" in personne["Quels sont les arguments qui vous font pencher plutôt contre le port du masque ?"]:
        score += 1
    if "Je pense que le vaccin est et restera suffisamment inoffensif pour la santé" in personne["Quels sont les arguments qui vous font pencher plutôt pour la vaccination au Covid-19 ?"]:
        score += -1
    if "Je pense que les vaccins ont été développés en suffisamment de temps pour être fiables" in personne["Quels sont les arguments qui vous font pencher plutôt pour la vaccination au Covid-19 ?"]:
        score += -1
    if "Je pense que notre connaissance en vaccins à ARN messager est suffisante pour les utiliser à grande échelle" in personne["Quels sont les arguments qui vous font pencher plutôt pour la vaccination au Covid-19 ?"]:
        score += -1
    if "Je pense que le vaccin a un impact positif concret pour ma protection personnelle face au Covid" in personne["Quels sont les arguments qui vous font pencher plutôt pour la vaccination au Covid-19 ?"]:
        score += -1  
    if "Je pense le vaccin a un impact positif concret dans le cadre de l'immunité collective" in personne["Quels sont les arguments qui vous font pencher plutôt pour la vaccination au Covid-19 ?"]:
        score += -1 
    if "Je pense que les vaccins ont été développés en trop peu de temps pour qu'ils soient fiables" in personne["Quels sont les arguments qui vous font pencher plutôt contre la vaccination au Covid-19 ?"]:
        score += 1
    if "Je pense que nous n'avons pas assez de recul par rapport aux vaccins à ARN messager" in personne["Quels sont les arguments qui vous font pencher plutôt contre la vaccination au Covid-19 ?"]:
        score += 1
    if "Je pense que le vaccin n'a pas d'impact positif concret pour ma protection personnelle face au Covid" in personne["Quels sont les arguments qui vous font pencher plutôt contre la vaccination au Covid-19 ?"]:
        score += 1   
    if "Je pense que le vaccin n'aura pas d'impact positif concret sur la sécurité de mes proches" in personne["Quels sont les arguments qui vous font pencher plutôt contre la vaccination au Covid-19 ?"]:
        score += 1
    if "Je pense que le vaccin n'a pas d'impact positif concret dans le cadre de l'immunité collective" in personne["Quels sont les arguments qui vous font pencher plutôt contre la vaccination au Covid-19 ?"]:
        score += 1 
    if "Je pense que le pass sanitaire permet d'éviter des couvre-feux ou confinements" in personne["Quels sont les arguments qui vous font pencher plutôt pour le pass vaccinal ?"]:
        score += -1       
    if "Je fais confiance au gouvernement sur la pertinence du pass vaccinal" in personne["Quels sont les arguments qui vous font pencher plutôt pour le pass vaccinal ?"]:
        score += -1
    if "Je pense que le pass vaccinal est une atteinte à ma liberté personnelle fondamentale" in personne["Quels sont les arguments qui vous font pencher plutôt contre le pass vaccinal ?"]:
        score += 1
    if "Je pense que le pass vaccinal est une atteinte à la liberté des Français" in personne["Quels sont les arguments qui vous font pencher plutôt contre le pass vaccinal ?"]:
        score += 1
    if "Je ne fais pas confiance aux vaccins contre le Covid-19" in personne["Quels sont les arguments qui vous font pencher plutôt contre le pass vaccinal ?"]:
        score += 1
    
    score = score/10
    
    if -1 <= score < -0.6:
        return "Pas du tout"
    elif -0.6 <= score < -0.2:
        return "Peu"
    elif -0.2 <= score < 0.2:
        return "Neutre"
    elif 0.2 <= score < 0.6:
        return "Plutôt"
    elif 0.6 <= score:
        return "Très"   


def categorisationSceptiscismePandemie(personne):
    score = 0
    
    if "Je pense que le masque est utile pour freiner la propagation du virus" in personne["Quels sont les arguments qui vous font pencher plutôt pour le port du masque ?"]:
        score += -1
    if "Je pense que le port du masque protège mes proches" in personne["Quels sont les arguments qui vous font pencher plutôt pour le port du masque ?"]:
        score += -1
    if "Je fais confiance à cette mesure du gouvernement pour son intérêt dans la gestion de la pandémie" in personne["Quels sont les arguments qui vous font pencher plutôt pour le port du masque ?"]:
        score += -1
    if "Je pense que le port obligatoire du masque est une attente à nos libertés" in personne["Quels sont les arguments qui vous font pencher plutôt contre le port du masque ?"]:
        score += 1
    if "Je pense que le masque peut causer des problèmes de santé (acné, problèmes respiratoires, etc.)" in personne["Quels sont les arguments qui vous font pencher plutôt contre le port du masque ?"]:
        score += 1   
    if "Je pense le vaccin a un impact positif concret dans le cadre de l'immunité collective" in personne["Quels sont les arguments qui vous font pencher plutôt pour la vaccination au Covid-19 ?"]:
        score += -1
    if "Je pense que le vaccin obligatoire pour tous n'empiète pas ou peu sur mes libertés personnelles" in personne["Quels sont les arguments qui vous font pencher plutôt pour la vaccination au Covid-19 ?"]:
        score += -1
    if "Je fais confiance au gouvernement sur les bienfaits de cette mesure" in personne["Quels sont les arguments qui vous font pencher plutôt pour la vaccination au Covid-19 ?"]:
        score += -1    
    if "Je pense que le vaccin n'a pas d'impact positif concret dans le cadre de l'immunité collective" in personne["Quels sont les arguments qui vous font pencher plutôt contre la vaccination au Covid-19 ?"]:
        score += 1
    if "Je pense que le vaccin obligatoire pour tous est une atteinte à la liberté personnelle" in personne["Quels sont les arguments qui vous font pencher plutôt contre la vaccination au Covid-19 ?"]:
        score += 1
    if "Je pense que le vaccin a été intentionnellement conçu pour réduire nos libertés" in personne["Quels sont les arguments qui vous font pencher plutôt contre la vaccination au Covid-19 ?"]:
        score += 1
    if "Je fais confiance au gouvernement sur la pertinence du pass vaccinal" in personne["Quels sont les arguments qui vous font pencher plutôt pour le pass vaccinal ?"]:
        score += -1
    if "Je pense que le pass vaccinal est une atteinte à ma liberté personnelle fondamentale" in personne["Quels sont les arguments qui vous font pencher plutôt contre le pass vaccinal ?"]:
        score += 1
    if "Je pense que le pass vaccinal est une atteinte à la liberté des Français" in personne["Quels sont les arguments qui vous font pencher plutôt contre le pass vaccinal ?"]:
        score += 1
    
    score = score/7
    
    if -1 <= score < -0.6:
        return "Pas du tout"
    elif -0.6 <= score < -0.2:
        return "Peu"
    elif -0.2 <= score < 0.2:
        return "Neutre"
    elif 0.2 <= score < 0.6:
        return "Plutôt"
    elif 0.6 <= score:
        return "Très"

    
def categorisationSceptiscismeVaccin(personne):
    score = 0
    
    if "Je pense que le vaccin est et restera suffisamment inoffensif pour la santé" in personne["Quels sont les arguments qui vous font pencher plutôt pour la vaccination au Covid-19 ?"]:
        score += -1
    if "Je pense que les vaccins ont été développés en suffisamment de temps pour être fiables" in personne["Quels sont les arguments qui vous font pencher plutôt pour la vaccination au Covid-19 ?"]:
        score += -1
    if "Je pense que notre connaissance en vaccins à ARN messager est suffisante pour les utiliser à grande échelle" in personne["Quels sont les arguments qui vous font pencher plutôt pour la vaccination au Covid-19 ?"]:
        score += -1
    if "Je pense que le vaccin a un impact positif concret pour ma protection personnelle face au Covid" in personne["Quels sont les arguments qui vous font pencher plutôt pour la vaccination au Covid-19 ?"]:
        score += -1
    if "Je pense le vaccin a un impact positif concret dans le cadre de l'immunité collective" in personne["Quels sont les arguments qui vous font pencher plutôt pour la vaccination au Covid-19 ?"]:
        score += -1
    if "Je fais confiance au gouvernement sur les bienfaits de cette mesure" in personne["Quels sont les arguments qui vous font pencher plutôt pour la vaccination au Covid-19 ?"]:
        score += -1  
    if "Je pense que les vaccins ont été développés en trop peu de temps pour qu'ils soient fiables" in personne["Quels sont les arguments qui vous font pencher plutôt contre la vaccination au Covid-19 ?"]:
        score += 1
    if "Je pense que nous n'avons pas assez de recul par rapport aux vaccins à ARN messager" in personne["Quels sont les arguments qui vous font pencher plutôt contre la vaccination au Covid-19 ?"]:
        score += 1
    if "Je pense que le vaccin n'a pas d'impact positif concret pour ma protection personnelle face au Covid" in personne["Quels sont les arguments qui vous font pencher plutôt contre la vaccination au Covid-19 ?"]:
        score += 1
    if "Je pense que le vaccin n'aura pas d'impact positif concret sur la sécurité de mes proches" in personne["Quels sont les arguments qui vous font pencher plutôt contre la vaccination au Covid-19 ?"]:
        score += 1
    if "Je pense que le vaccin n'a pas d'impact positif concret dans le cadre de l'immunité collective" in personne["Quels sont les arguments qui vous font pencher plutôt contre la vaccination au Covid-19 ?"]:
        score += 1
    if "Je pense que le vaccin a été intentionnellement conçu pour réduire nos libertés" in personne["Quels sont les arguments qui vous font pencher plutôt contre la vaccination au Covid-19 ?"]:
        score += 1
    if "Je fais confiance au gouvernement sur la pertinence du pass vaccinal" in personne["Quels sont les arguments qui vous font pencher plutôt pour le pass vaccinal ?"]:
        score += -1
    if "Je ne fais pas confiance aux vaccins contre le Covid-19" in personne["Quels sont les arguments qui vous font pencher plutôt contre le pass vaccinal ?"]:
        score += 1
    
    score = score/7
    
    if -1 <= score < -0.6:
        return "Pas du tout"
    elif -0.6 <= score < -0.2:
        return "Peu"
    elif -0.2 <= score < 0.2:
        return "Neutre"
    elif 0.2 <= score < 0.6:
        return "Plutôt"
    elif 0.6 <= score:
        return "Très"
    
    
    
def traitementPersonne(personne):
    resPersonne = []
    
    resPersonne.append(categorisationVax(personne))
    resPersonne.append(personne['Quel est votre genre ?'])
    resPersonne.append(personne["Quelle est votre tranche d'âge ?"])
    resPersonne.append(personne["Combien de doses de vaccin au Covid-19 avez vous reçues ? "]) 
    resPersonne.append(personne["Quelle est votre catégorie socio-professionnelle ?"])
    resPersonne.append(personne["Quelle est la population de votre ville de résidence ?"])
    resPersonne.append(categorisationPolitque(personne))
    resPersonne.append(categorisationEntourage(personne))
    resPersonne.append(categorisationPassifCovid(personne))
    resPersonne.append(categorisationGeneMesure(personne))
    resPersonne.append(categorisationConfianceGouvernement(personne))
    resPersonne.append(categorisationSceptiscismeMesure(personne))
    resPersonne.append(categorisationSceptiscismePandemie(personne))
    resPersonne.append(categorisationSceptiscismeVaccin(personne))
    
    return resPersonne


#Initialisation des dataset
dataset1 = pd.read_csv("[ecole]_Questionnaire_sur_la_vaccination_anti-Covid19.csv")
dataset2 = pd.read_csv("[groupes]_Questionnaire_sur_la_vaccination_anti-Covid19.csv")
data = pd.concat([dataset1, dataset2])

datasetF = pd.DataFrame( columns = ["Catégorie", "Genre", "Age", "Nombre Doses Vaccin", "Socio-professionelle", "Taille ville", "Positionnement politique", "Entourage", "Passif Covid", 
                                        "Gène des Mesures", "Confiance Gouvernement", "Scepticisme Mesure", "Scepticisme Pandémie", "Scepticisme Vaccin"])



#Remplissage du dataset final
for i in range(data.shape[0]):
    datasetF.iloc[i] = traitementPersonne(data.iloc[i])

"""
#Export vers SQL
engine = create_engine("sqldevelopper://", echo = False)
datasetF.to_sql("Anti-Vax DataBase", con = engine )


#Export vers csv
datasetF.to_csv("Données_traitées.csv", index = False)
"""