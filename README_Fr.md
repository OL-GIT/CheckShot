# CheckShot
### Vérifie l'intégrité des sous-répertoires d'un projet de post-production. ###


## Scenario :

  Les images sont rendues sur des ordinateurs/fermes de rendu et déposées sur un serveur. L'arborescence pouvant être différente dans chaque projet, CheckSeq ne sera exécuté qu'au niveau de la séquence. (Séquence/Plans/Images)


## Objectif principal :

  Vérifie si les répertoires des plans contiennent :
- Le fichier (.bounds) identifiant les bornes de début/fin de plan souhaitées.
- L'adéquation avec le nombre d'images trouvées.
- Les fichiers avec le bon nombre de champs (nom.numéro.extension)
- Les fichiers avec le champ numérique correct (4 chiffres, soit ####)
- Les fichiers avec la bonne extension
- Les fichiers avec un poids non nul
- Toutes les images demandées, recherche des fichiers manquants


## Utilisation :

  L'outil est utilisable dans un cas ponctuel ainsi que lors de contrôles journaliers/horaires.
Il peut être lancé par une tâche cron ou un script personnalisé.

- S'il est lancé manuellement, le script génère un rapport lisible dans la console,
qui met en évidence les erreurs possibles trouvées.
Il peut être lancé plan par plan, ou plus globalement sur une séquence.

- Si automatisé, l'utilisateur pourra vérifier la version Web du dump, qui peut être vue sur n'importe quel appareil qui gère les pages HTML.

- Dans les deux cas, il générera également un rapport de log qui serait
plutôt destiné aux administrateurs système.

L'outil web est destiné aux superviseurs de post-production, qui peuvent rapidement jeter un coup d'œil sur les prises de vue en cours, voir les erreurs possibles, ou simplement vérifier la progression du calcul.


## Conditions :

Python3 doit être installé sur le serveur s'il est automatisé, 
ou sur le client en cas d'utilisation en réseau.

Les scripts tournent sous Linux et Windows (avec cygwin).

Dans le repertoire d'installation doivent figurer :
  * olCheckSeq.py
  * olCheckShot.py
  
et les répertoires :
  * olCheckLibs/
  * olCheckWebRef/


## Installation :

Allez dans le repertoire dans lequel vous voulez télécharger l'archive.

- Téléchargez et décompressez l'archive .zip du programme [ici](https://github.com/OL-GIT/CheckShot/archive/refs/heads/main.zip).

ou tapez :

```
> git clone https://github.com/OL-GIT/CheckShot.git
```

puis lancez installation :

```
> cd CheckShot
> chmod 774 ./install.bash
> sudo ./install.bash
```


## Méthode :

*olCheckSeq.py* peut être exécuté au niveau de la séquence.
Vous devez spécifier le nom des plans que vous souhaitez vérifier :
```
> python3 olCheckSeq.py P1 P2 P3
> python3 olCheckSeq.py P*
> python3 olCheckSeq.py *
```
*olCheckShot.py* peut être exécuté au niveau du plan.
Il n'a pas besoin d'argument :
```
> python3 olCheckShot.py
```


## Resultats :

- S'ils sont lancés manuellement, checkSeq et checkShot afficheront les résultats dans la console.

>Cette méthode est recommandée pour un usage ponctuel.

- Le ministe HTML se trouve dans $PROJ/$SEQ/.web/index.htm

>seqreport.htm est affiché dans le cadre de gauche.

>Les rapports de plans sont écrits dans $PROJ/$SEQ/$SHOT/report.htm

>Ils seront affichés dans le cadre de droite du minisite.

>Des versions archivées de report.htm sont copiées dans report_$PROJ_$SEQ_$SHOT_DATE_TIME.htm

- Les fichiers globaux de log sont dans $PROJ/LOGS/ (olCheckSeqlog.DATE-TIME.txt)

>Ils contiennent des versions courtes des retours console.

