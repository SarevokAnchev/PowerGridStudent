
# PowerGrid : Gestion de projet informatique (M1 EEEA - ISTIC)

## Introduction

Au cours du module de développement logiciel du parcours M1-EEEA, vous avez acquis des compétences en programmation, ainsi que des connaissances des outils de gestion de projet informatique. À travers ce projet, il s'agit de mettre à profit ces compétences en menant à bien un projet de développement informatique en équipe. Vous devrez ainsi concevoir et mettre en place un système d'optimisation d'un réseau de distribution électrique. Vous produirez à la fois la documentation descriptive du projet, ainsi que le code Python qui en découle. Vous écrirez également les tests unitaires des sous-parties du projet, et mettrez en place un serveur d'intégration continue pour automatiser les tests.

Les sections suivantes décrivent le déroulement du projet. Vous devrez suivre les instructions décrivant la mise en place d'un environnement de développement reproductible au sein d'une machine virtuelle, et l'appropriation du projet PowerGrid. 

### Consignes et évaluation du projet

Le TP doit être réalisé par groupes de deux ou trois étudiants. Faites en sorte que chaque étudiant de chaque groupe dispose d'un ordinateur pour travailler en séance de TP (ordinateur personnel ou ordinateur de l'université). Faites également en sorte que chaque groupe ait accès à un ordinateur de l'université.

Le rendu final pour ce projet sera constitué **d'un rapport au format PDF** signé par tous les membres du groupes, ainsi que du lien vers le **dépôt GitHub public** sur lequel trouver votre code.

La liste (non exhaustive) suivante comporte des éléments d'évaluation du projet, qui seront valorisés pour la note finale si visibles dans le rapport ou dans votre dépôt :
- [ ] Traces de travail d'équipe dans l'historique Git du projet (fusions, commits réalisés par des utilisateurs différents, branches de travail...)
- [ ] Éléments de description du projet et de l'architecture du code et des outils et machines virtuelles mis en place (schémas, diagrammes UML...).
- [ ] Descriptions des difficultés rencontrées, et des recherches réalisées pour les surmonter (segments de code, captures d'écrans, références des forums/documentations utilisées...)
- [ ] Fonctionnement final de PowerGrid, réponse au cahier des charges
- [ ] Écriture et utilisation des différents tests unitaires du projet
- [ ] Améliorations apportées spontanément au fonctionnement de PowerGrid (suggestions fournies en fin de présentation du projet)
- [ ] Preuve de la compréhension et de la mise à profit des outils suggérés (Git, GitHub, unittest, Jenkins, WSL...)
- [ ] Amélioration de l'utilisation du serveur d'intégration continue
----

## Table des matières

1. [Duplication (fork) du projet](#fork)
2. [Configuration de votre poste de travail](#config-pdt)
    1. [Installation et configuration de VSCode](#install-vs)
    2. [Installation de WSL](#install-wsl)
    3. [Configuration d'une VM WSL2](#config-wsl)
    4. [Création de clés SSH pour l'authentification avec GitHub](#ssh-dev)
    5. [Clonage du projet et configuration des identifiants](#clone)
    6. [Configuration de VSCode pour le développement Python dans WSL](#config-vs)
    7. [Export de votre machine virtuelle pour réutilisation ultérieure](#export-wsl)
3. [Mise en place du serveur CI](#jenkins)
    1. [Configuration d'un environnement WSL](#jenkins-wsl)
    2. [Autorisation de Jenkins dans GitHub](#jenkins-github)
    3. [Accès au tableau de bord Jenkins](#jenkins-dashboard)
    4. [Configuration de la pipeline Jenkins](#jenkins-pipeline)
4. [Appropriation du projet](#projet)
    1. [Description de PowerGrid](#projet-desc)
    2. [Architecture du projet](#projet-arch)
    4. [Étapes de développement du projet](#projet-pem)

----

<a name="fork" />

## Duplication (fork) du projet

Ce projet est actuellement hébergé de manière publique sur le compte GitHub d'un autre développeur. Si vous voulez reprendre le projet à votre compte et le développer de votre coté, il vous faudra tout d'abord réaliser un fork du dépôt actuel. Un fork d'un projet consiste à placer une copie du projet d'un autre développeur sur votre compte, que vous pouvez éditer comme bon vous semble. Il est ensuite possible, si besoin, de proposer une fusion du fork avec le projet original.

Commencez par créer un compte GitHub pour chacun des membres de votre groupe.

Une fois vos comptes créés, l'un des membres du groupe doit se déplacer en haut de cette page et cliquer sur le bouton **fork**. Vérifiez que l'affichage suivant montre bien votre compte comme propriétaire du nouveau fork, puis validez. Cela devrait créer une copie du dépôt actuel liée à votre compte, avec la même visibilité publique.

Il faut maintenant faire en sorte que tous les membres du groupe puissent collaborer sur le projet. GitHub propose à l'administrateur d'un projet d'ajouter des collaborateurs qui pourront pousser leurs contributions vers le dépôt. Sur la page du projet associé à votre compte, cliquez sur **Settings**, puis sur **Collaborators**. Le bouton vert **Add People** vous permet alors de rechercher d'autres comptes et de les inviter à collaborer sur votre projet. Une fois l'invitation acceptée, vos nouveaux collaborateurs devraient être en mesure de modifier le dépôt sur votre compte.

<a name="config-pdt" />

## Configuration de votre poste de travail

Ce projet comporte une part de développement Python pour lequel il vous sera possible de travailler depuis votre poste personnel ou en utilisant les machines de l'université. Les étapes décrites ci-dessous décrivent la marche à suivre.

**Veillez à lire et comprendre chacune des opérations décrites. Elles doivent vous permettre d'installer et de configurer des logiciels nécessaires à ce TP. Il est nécessaire que chacun des membres du groupe procède individuellement à la configuration de son environnement de travail. Chacun doit être en mesure de contribuer au développement du programme.**

> Note : la procédure ci-dessous documente le développement Python dans une machine virtuelle WSL. Si vous souhaitez configurer différemment votre poste pour développer dans le système hôte sans machine virtuelle, **et êtes capable de le faire sans assistance**, ce choix vous incombe.

<a name="install-vs" />

### Installation et configuration de VSCode

Pour installer Visual Studio Code sur votre poste de travail, rendez-vous à l'adresse suivante : [https://code.visualstudio.com/download](https://code.visualstudio.com/download). Choisissez le téléchargement pour Windows et exécutez le programme d'installation.

> Note : Visual Studio Code est déjà installé sur les machines de l'université, il vous suffit donc d'installer les extensions nécessaires en suivant les instructions ci-dessous.

Pour configurer un environnement de développement avec WSL, il vous faut installer l'extension correspondante pour Visual Studio Code. Ouvrez le panneau des extensions grâce au raccourci `Ctrl + Shift + X`. Dans la barre de recherche en haut du panneau, taper WSL et installez la première extension qui apparaît en haut des résultats de recherches. Procédez de la même panière pour installer l'extension Python.

<a name="install-wsl" />

### Installation de WSL

Afin de vérifier que WSL est bien installé sur votre machine, ouvrez un terminal Windows PowerShell (n'utilisez pas l'invite de commande par défaut de Windows, qui risque de vous empêcher de copier des commandes), et exécutez la commande suivante :

```bash
wsl --list --online
```

Si la commande retourne un message d'erreur, il vous faut installer WSL sur votre ordinateur. Sinon, vous pouvez passer à la section suivante. 

Afin d'installer WSL sur votre ordinateur, exécutez la commande suivante dans votre terminal Windows PowerShell :

```bash
wsl --install
```

Cette commande installe les composants de WSL, et vous permettra de réaliser les opérations suivantes. Il vous est ensuite demandé de redémarrer l'ordinateur.

<a name="config-wsl" />

### Configuration d'une VM WSL2

Nous allons réaliser les manipulations de ce TP en utilisant le WSL2. Il s'agit d'une machine virtuelle linux intégrée au système Windows. Ouvrez une invite de commande Windows (PowerShell), puis tapez la commande suivante pour installer une distribution Ubuntu pour votre future machine virtuelle :

```bash
wsl --install Ubuntu
```
Une fois la distribution installée, vous pouvez lancer une nouvelle machine virtuelle en exécutant la commande :

```bash
wsl -d Ubuntu
```

Vous êtes alors invité à choisir un nom d'utilisateur ainsi qu'un mot de passe. Choisissez des identifiants courts afin de pouvoir les taper à plusieurs reprises sans complications. Une fois l'installation terminée, vous devez être en mesure de taper des commandes linux dans la console. L'affichage du début de ligne de l'invite de commande doit refléter le changement d'environnement. Vous pouvez maintenant exécuter les commandes suivantes pour terminer la configuration de la machine virtuelle :

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y wget git vim openssh-client python3 python3-pip python3-venv
```

Ces commandes doivent mettre à jour la machine virtuelle, et installer Git et Python afin que vous puissiez développer votre projet.

**À partir de maintenant, cette fenêtre doit rester ouverte puisqu'elle est liée à l'environnement dans lequel vous travaillez. Si la fenêtre est fermée, la machine virtuelle est éteinte.**

<a name="ssh-dev" />

### Création de clés SSH pour l'authentification avec GitHub

Votre invite de commande est maintenant située à l'intérieur d'une machine virtuelle configurée pour le développement Python. Vous pourrez bientôt télécharger le projet PowerGrid pour commencer à programmer. Cependant, l'utilisateur de la machine virtuelle ne possède pas encore les droits nécessaires pour pousser des modifications vers le dépôt sur GitHub. GitHub gère les droits de modification à partir de jeux de clés cryptographiques générés par un utilisateur pour garantir son identité. Linux dispose d'une commande permettant de générer une clé de chiffrement. Celle-ci vous permettra de confirmer votre identité au site GitHub. Exécutez tout d'abord la commande suivante, en acceptant le chemin par défaut pour les fichiers générés (tapez ENTRÉE), et en choisissant un mot de passe simple pour la clé SSH :

```bash
ssh-keygen -t ed25519 -C "prenom.nom@etudiant.univ-rennes.fr"
```

Le mot de passe choisi est celui qui sécurise votre clé. Pour ce TP, vous pouvez choisir le même que celui que vous avez entré comme mot de passe utilisateur pour la machine virtuelle. Tapez enfin la commande :

```bash
cat ~/.ssh/id_ed25519.pub
```

Copiez la sortie de la commande dans le presse-papier. Il s'agit de votre clé publique, qui servira à vous identifier en ligne.

Enfin, il faut signaler à GitHub que cette clé vous identifie comme un utilisateur ayant le droit de modification de vos dépôts en ligne. Pour ce faire, rendez-vous à nouveau sur le site web GitHub. En cliquant sur votre profil en haut à droite de la page, choisissez **Settings**, puis **SSH and GPG keys**, et choisissez **New SSH key**. Dans le champ **key**, collez la clé publique que vous avez copiée à l'étape précédente. Renseignez un nom pour cette clé dans le champ **Title**, par exemple *DevWSL*. Validez enfin avec **Add SSH key**.

<a name="clone" />

### Clonage du projet et configuration des identifiants

Vous êtes maintenant en mesure de développer dans l'environnement de la machine virtuelle, et de pousser vos modifications vers le dépôt stocké sur GitHub. Téléchargez tout d'abord le dépôt dans votre environnement de développement. La commande `git clone` permet de copier localement un dépôt désigné par son URL. Exécutez les commandes suivantes, en remplaçant par le nom d'utilisateur GitHub du détenteur du fork :

```bash
cd ~
git clone git@github.com:[NOM UTILISATEUR]/PowerGridStudent.git
cd PowerGridStudent
```
La première commande déplace votre terminal vers votre dossier personnel, où vous avez les droits d'écriture, la deuxième clone le projet dans ce dossier et la troisième place le terminal dans le dossier du projet.

Vous avez maintenant cloné le dépôt de code PowerGrid dans votre machine virtuelle, et avez déplacé votre terminal à l'intérieur du répertoire ainsi créé. Il vous est maintenant possible d'ouvrir et de modifier les différents fichiers du projet. Cependant, vous n'avez pas encore défini d'identifiants au sein de git vous permettant de créer et pousser de nouveaux commits. Pour ce faire, exécutez les commandes suivantes, en remplaçant avec votre identité :

```bash
git config --global user.name "MonNom"
git config --global user.email "prenom.nom@univ-rennes.fr"
```

<a name="config-vs" />

### Configuration de VSCode pour le développement Python dans WSL

À l'intérieur du terminal de la machine virtuelle, vous pouvez taper la commande suivante pour ouvrir le projet dans Visual Studio Code :

```bash
code .
```

> Vous devriez voir apparaître un message vous indiquant le téléchargement de vscode-server sur la machine virtuelle. Si un message d'erreur apparaît à la place, assurez-vous que vous avez bien suivi les [instructions](#install-vs) d'installation de Visual Studio Code, puis redémarrez le terminal et la machine virtuelle.

Ouvrez l'un des fichiers Python du projet dans VSCode. Un message devrait apparaître, vous invitant à installer l'extension Python dans WSL. Faites cette installation.

> Dans le terminal de Visual Studio Code, si vous travaillez sur une machine de l'université, il est possible que vous soyez connecté en tant que `root` lorsque vous ouvrez votre projet. Si c'est le cas, changez d'utilisateur en utilisant la commande `su -- [NOM UTILISATEUR]`.

Dans le terminal de la machine virtuelle, vous devez maintenant créer un environnement Python, dans lequel seront installés les paquets dont dépend votre projet. Exécutez les commandes suivantes :

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Dans l'interface de Visual Studio Code, un message a du apparaître pour signaler la détection de la création d'un nouvel environnement Python. Acceptez la sélection de cet environnement pour le projet. Si aucun message n'apparaît, vous pouvez sélectionner l'environnement python `venv` en cliquant sur la mention concernant votre version de python, en bas à droite de l'interface quand un fichier `.py` est ouvert dans l'éditeur.

Vérifiez que vous êtes en mesure d'exécuter le projet (script `PowerGrid.py`). Si vous n'avez pas directement une flèche verte pour l'exécution en haut à droite de l'interface de VSCode, vous pouvez exécuter vos scripts en ligne de commande dans le terminal de l'éditeur. L'activation d'un environnement python dans le terminal se fait grâce à la commande :

```bash
source venv/bin/activate
```

<a name="export-wsl" />

### Export de votre machine virtuelle pour réutilisation ultérieure

#### Quitter ou relancer une machine virtuelle

Depuis un terminal d'une machine virtuelle, vous pouvez quitter celle-ci en tapant la commande `exit`. Vous quitterez également la machine virtuelle si vous êtes emmené à fermer le terminal.

Pour se reconnecter à une machine virtuelle, il faut connaître le nom de la ditribution de celle-ci (par exemple `Ubuntu` dans le cas de la machine virtuelle décrite ci-dessous comme notre environnement de développement), ainsi que le nom d'utilisateur que vous aviez choisi pour cette machine virtuelle.

Par exemple, pour me connecter à une machine virtuelle `Ubuntu` avec l'utilisateur `louis`, j'exécuterai alors la commande :

```bash
wsl --distribution Ubuntu --user louis
```

Pour retourner à l'intérieur de votre espace personnel sur la VM, vous pouvez finalement exécuter la commande :

```bash
cd ~
```

#### Export d'une machine virtuelle pour réutilisation ultérieure

> Note : Cette section est principalement à destination des étudiants ayant choisi de développer en utilisant les machines de l'université, les autres étudiants peuvent ignorer ces instructions.

Si vous souhaitez sauvegarder un état de votre machine virtuelle (par exemple, dans le cas des ordinateurs de l'université qui sont réinitialisés à chaque déconnexion), vous pouvez exporter la machine virtuelle vers un fichier au moyen d'une commande. Vous pourrez alors stocker ce fichier à un endroit sécurisé et demander à wsl de le charger lors d'une utilisation ultérieure.

Une fois votre machine virtuelle éteinte, exécutez la commande suivante dans une invite de commande Windows : 

```bash
wsl --export Ubuntu ubuntu-dev.tar
```

Vous devriez voir apparaître un fichier `ubuntu-dev.tar` faisant quelques gigaoctets. Il s'agit du fichier à conserver dans un endroit sûr.

> Si vous travaillez sur les machines de l'université, placez ce fichier sur le réseau (lecteur **H:**) ou sur un emplacement cloud personnel. Un fichier laissé sur le lecteur **C:** ne sera pas forcément acessible lors de votre prochaine connexion.

Afin de charger votre machine virtuelle sauvegardée, lors d'une utilisation ultérieure, vous pourrez utiliser la commande suivante :

```bash
wsl --import Ubuntu-dev UbuntuDev ubuntu-dev.tar
```

> Si vous travaillez sur les machines de l'université, exécutez cette commande sur le lecteur local **C:** (par exemple dans vos documents). Il vous manquera des droits si vous cherchez à réaliser cette opération drectement sur le réseau.

Le premier paramètre de cette commande est le nom que portera la distribution dans WSL une fois importée. Le deuxième paramètre est le chemin vers le dossier dans lequel la machine virtuelle sera stockée, et le dernier argument est le nom du fichier `.tar` dans lequel la VM a été exportée par le passé.

Pour lancer la machine virtuelle importée, il vous suffira alors de taper la commande :

```bash
wsl --distribution Ubuntu-dev --user [NOM UTILISATEUR]
```

Puis tapez la commande :

```bash
cd ~
```

Pour rejoindre votre dossier personnel sur la VM (où se trouve votre projet).

<a name="jenkins" />

## Mise en place du serveur CI

Vous allez mettre en place un serveur d'automatisation des tests de votre projet avec Jenkins. Ce serveur peut être mis en place une fois par l'un des membres du groupe. En situation réelle, l'intérêt d'un tel serveur est de fonctionner jour et nuit et de scruter les changements apportés au projet en réalisant continuellement des tests. Dans votre cas, vous pouvez vous contenter dans un premier temps de mettre en place le serveur une première fois pour apprendre à le configurer.

**Ces opérations peuvent également être réalisées sur les machines de l'université, ou sur vos ordinateurs personnels selon votre choix. En cas d'utilisation de votre ordinateur, veillez à avoir activé le service WSL dans Windows.**

<a name="jenkins-wsl" />

### Configuration d'un environnement WSL

Commencez par ouvrir un terminal Windows (PowerShell), et tapez la commande suivante pour démarrer **une nouvelle machine virtuelle** Linux :

```bash
wsl --install Ubuntu-22.04
```

Une fois la machine virtuelle démarrée, il vous est demandé de choisir un nom d'utilisateur ainsi qu'un mot de passe. Choisissez des identifiants courts.

Une fois que l'invite de commande montre que vous êtes dans la machine virtuelle, exécutez les commandes suivantes pour configurer l'environnement :

> Vous pouvez avoir besoin d'exécuter les commandes suivantes une par une plutôt qu'en bloc, pour que celles-ci soient comprises par le terminal Windows.

```bash
sudo apt update
sudo apt upgrade -y
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update
sudo apt install -y jenkins fontconfig openjdk-17-jre
sudo ufw enable
sudo ufw allow 9090
sudo systemctl enable jenkins
sudo sed -i 's/Environment=\"JENKINS_PORT=8080\"/Environment=\"JENKINS_PORT=9090\"/g' /lib/systemd/system/jenkins.service
sudo systemctl daemon-reload
sudo systemctl restart jenkins
sudo apt install -y git python3 python3-pip python3-venv
```

Ces commandes ont servi à mettre à jour les logiciels de la machine virtuelle, puis à installer Git, Python et Jenkins. Elles ont également modifié la configuration du serveur web géré par Jenkins.

**À partir de maintenant, cette fenêtre doit rester ouverte puisqu'elle est liée au serveur Jenkins. Si la fenêtre est fermée, la machine virtuelle est éteinte et le serveur Jenkins est désactivé.**

<a name="jenkins-github" />

### Autorisation de Jenkins dans GitHub

L'installation de Jenkins a créé un nouvel utilisateur nommé `jenkins` sur la machine virtuelle. C'est cet utilisateur qui doit acquérir les droits de lecture du dépôt GitHub en ligne. Commencez par changer d'utilisateur. Tapez tout d'abord la commande :

```bash
sudo passwd jenkins
```

Cette commande vous permet de choisir un mot de passe pour l'utilisateur jenkins. Choisissez un mot de passe simple. Pour ce TP, vous pouvez choisir le même mot de passe que celui de l'utilisateur principal de la VM.

Ensuite, afin de changer d'utilisateur, tapez la commande :

```bash
su - jenkins
```

L'invite de commande devrait montrer un changement d'utilisateur.

Vous devez maintenant créer des identifiants SSH à l'utilisateur `jenkins`, afin que celui-ci puisse s'identifier auprès de GitHub pour collecter les modifications apportées à notre dépôt de code. Générez une nouvelle paire de clés SSH pour l'utilisateur `jenkins` avec la commande suivante :

```bash
ssh-keygen -t ed25519 -C "prenom.nom@etudiant.univ-rennes.fr"
```

Vous pouvez afficher le contenu de votre clé privée en utilisant la commande :

```bash
cat ~/.ssh/id_ed25519
```

Et afficher le contenu de votre clé publique en utilisant la commande :

```bash
cat ~/.ssh/id_ed25519.pub
```

Sur l'interface web de GitHub, naviguez jusqu'à la page de votre projet PowerGrid (celui qui est hébergé sur votre compte). En haut de la page, cliquez sur l'option **Settings**, puis choisissez l'option **Deploy keys**. Cliquez enfin sur le bouton **Add deploy key**. L'interface qui s'affiche alors doit vous permettre d'ajouter une clé publique qui identifie un utilisateur auquel sera donné le droit de lire les modifications de votre dépôt PowerGrid. Choisissez un nom pour votre nouvelle clé, par exemple **jenkins**, puis copiez dans le champ du dessous la clé publique que vous avez générée à l'étape précédente. Validez enfin l'ajout de la clé. À partir de maintenant, l'utilisateur `jenkins` de votre machine virtuelle dispose d'un accès en lecture à votre dépôt PowerGrid.

Enfin, vous devez ajouter le dépôt GitHub aux serveurs SSH connus par l'utilisateur `jenkins`. Pour ce faire, exécutez la commande suivante, et validez en tapant `yes`:

```bash
git ls-remote -h -- git@github.com:[NOM UTILISATEUR GITHUB]/PowerGridStudent.git ~/.ssh/id_ed25519.pub
```

Pensez à remplacer le nom d'utilisateur GitHub dans la commande par celui du membre du groupe ayant réalisé le fork du dépôt.

Vous pouvez maintenant reprendre l'identité de l'utilisateur principal de la vm en exécutant la commande :

```bash
exit
```

<a name="jenkins-dashboard" />

### Accès au tableau de bord Jenkins

Jenkins est un logiciel qui permet d'automatiser des tâches telles que l'exécution de tests au cours du développement de notre projet. Nous allons paramétrer Jenkins afin que tous les tests de PowerGrid soient lancés et qu'un rapport sur les réussites et les échecs soit rendu à chaque nouveau commit poussé sur la branche principale. Nous venons d'autoriser à Jenkins l'accès en lecture à notre projet sur GitHub, il suffit maintenant de le paramétrer l'exécution des tests.

En installant et en démarrant Jenkins sur la machine virtuelle, nous avons mis en place un serveur web auquel nous pouvons maintenant accéder pour paramétrer jenkins. Ce serveur web est hébergé par la machine virtuelle, nous pouvons donc y accéder en connaissant l'adresse IP de celle-ci. Pour obtenir l'adresse IP de la machine virtuelle, exécutez-y la commande suivante :

```bash
ip addr
```

Vous devriez voir apparaître plusieurs configurations d'interfaces réseau. L'adresse qui nous intéresse est l'adresse IPv4 associée à l'interface `eth0` (il peut par exemple s'agir d'une adresse ressemblant à `172.18.132.114`).

Ouvrez un navigateur web et tapez cette adresse dans la barre de recherche, suivie de `:9090` (il s'agit du port qui a été sélectionné pour le serveur web de Jenkins). Une fois que vous avez validé cette adresse, vous devriez voir apparaître une interface de connexion Jenkins. Nous avons réussi à mettre en place le panneau de commande Jenkins!

Il vous est demandé dans l'interface de déverrouiller Jenkins pour la première connexion. Retournez à votre terminal. Le mot de passe qui vous est demandé est accessible en tapant la commande :

```bash
sudo cat /var/lib/jenkins/secrets/intialAdminPassword
```

> Si cette commande ne fonctionne pas, vous pouvez également trouver le mot de passe quelque part dans la sortie de jenkins obtenue en exécutant la commande `journalctl -u jenkins`.

Copiez ce mot de passe dans le champ correspondant dans votre navigateur web, et validez. Choisissez d'installer les plugins recommandés et attendez la fin de leur configuration.

Vous pouvez maintenant créer un utilisateur administrateur pour Jenkins. Cette fois encore, choisissez des identifiants courts et faciles à retenir. Une fois les pages suivantes validées, vous devez parvenir au tableau de bord de Jenkins.

**Vous disposez maintenant d'une installation viable de Jenkins au sein d'une machine virtuelle, il vous est conseillé de penser à réaliser des sauvegardes de celle-ci en suivant les instructions dispensées dans la [section correspondante](#export-wsl)**

<a name="jenkins-pipeline" />

### Configuration du pipeline Jenkins

Jenkins permet de définir une suite d'action exécutée à un intervalle de temps défini ou lorsqu'un événement a lieu. Ces actions sont définies dans un **Pipeline**.

On définit un Pipeline Jenkins en écrivant un script qui contient une description de grandes étapes et des actions à entreprendre lors de chacune de ces étapes. Ce script doit être placé à la racine du projet dans un fichier nommé `Jenkinsfile`. Voici le contenu initial de ce fichier pour notre projet (le fichier fait déjà partie du dépôt dupliqué sur GitHub :

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps{
                sh 'python3 -m venv venv'
                sh './venv/bin/python -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'rm -rf test-reports/'
                sh './venv/bin/python -m xmlrunner -o test-reports/'
            }
            post {
                always {
                    junit '**/test-reports/*.xml' 
                }
            }
        }
    }
}

```

La première étape, `Build`, met en place un environnement Python dans lequel notre projet peut être exécuté : elle crée un environnement virtuel Python, puis installe les dépendances décrites dans le fichier `requirements.txt`.

La deuxième étape, `Test`, exécute tous les tests présents dans le projet, et crée un rapport sous forme de fichiers `.xml` interprétés par **JUnit**, un outil de tests unitaires.

Votre `Jenkinsfile` initial étant déjà implémenté, il nous reste à configurer Jenkins pour automatiser l'exécution de ce Pipeline. Sur la première page du tableau de bord Jenkins, choisissez tout d'abord l'option de création d'un **Nouvel Item**. Sur la page suivante, choisissez un nouveau nom pour le Pipeline. Vous pouvez choisir le nom **PowerGrid**, qui correspond au projet dont le Pipeline assurera l'intégration continue. Choisissez ensuite l'option **Pipeline** parmi les types d'item proposés. Appuyez enfin sur **OK** en bas de la page.

Vous accédez maintenant à une page comportant de nombreuses options pour notre **Pipeline**. La première section, comportant des options générales, ne vous intéresse pas dans le cadre de ce TP.

Dans la deuxième section, vous pouvez configurer les conditions d'exécution du Pipeline. Si vous choisissez de laisser inchangées toutes les options de cette section, l'exécution ne se fera que manuellement, en cliquant vous-même sur le bouton correspondant sur le tableau de bord de Jenkins. Vous pouvez à la place configurer l'option **Exécuter périodiquement**, qui vous permet de définir un schéma périodique d'exécution du Pipeline. Le champ qui apparaît sous l'option, une fois celle-ci sélectionnée, vous invite à préciser le planning d'exécution. Une documentation est fournie si vous cliquez sur le point d'interrogation correspondant. Vous pouvez par exemple entrer :

```
H/15 * * * *
```

Afin de configurer une exécution du Pipeline environ une fois toutes les 15 minutes.

Les options **GitHub hook trigger for GITScm polling** et **Scrutation de l'outil de gestion de version** permettent de générer des exécutions uniquement selon certaines conditions relatives aux événements sur le dépôt Git. Elles ne sont pas couvertes dans ce sujet, mais peuvent être explorées durant le TP.

Enfin, la dernière section vous permet de définir le Pipeline à exécuter. La première boîte vous invite à choisir la source de votre Pipeline. Choisissez **Pipeline Script from SCM**. La boîte suivante vous permet de choisir un gestionnaire de version. Choisissez **Git** parmi les options : de nouveaux champs apparaissent.

Dans le champ **Repository url**, entrez l'url de votre dépôt sur GitHub, qui devrait ressembler à :

```
git@github.com:[NOM UTILISATEUR GITHUB]/PowerGridStudent.git
```

Il vous faut ensuite choisir une valeur pour le champ **Credentials**. Il s'agit du champ qui doit contenir des identifiants permettant à Jenkins d'accéder en lecture à votre dépôt sur GitHub, afin de pouvoir en télécharger et tester le code. Dans le menu déroulant, il n'y a pas encore de valeur disponible à la sélection. Il vous faut ajouter un nouveau jeu d'identifiants en cliquant sur le bouton **Ajouter**, en dessous du menu déroulant. Cliquez sur le choix **Jenkins** et vous parvenez à une interface pour renseigner vos identifiants :

- Dans le champ **Type**, sélectionnez **SSH Username with private key**.
- Dans le champ **Portée**, conservez le choix par défaut **Global**.
- Dans les champs **ID** et **Description**, renseignez des informations par lesquelle vous reconnaîtrez les identifiants dans l'interface Jenkins.
- Dans le champ **Username**, choisissez un nom d'utilisateur pour ces identifiants. Choisissez un nom simple, comme **JenkinsWSL**.
- Enfin, cliquez sur le bouton **Enter directly** en-dessous de la mention **Private key**. Sur le champ qui s'ouvre en-dessous, cliquez sur le bouton **Ajouter**, puis copiez dans le cadre la clé privée de vos identifiants SSH, que vous avez générée dans une [section précédente](#jenkins-github).
- Dans le dernier champ, tapez le mot de passe que vous aviez associé à l'utilisation de ces identifiants SSH.

Validez cette fenêtre, vous revenez alors à l'interface de configuration de la pipeline. Si tout fonctionne correctement, vous ne devriez pas voir apparaître de message rouge d'erreur en-dessous du champ concernant le dépôt et les identifiants. Si vous voyez un tel message, reprenez les étapes précédentes et vérifiez que vous n'avez pas commis d'erreur.

Les champs restants concernent des réglages supplémentaires pour le Pipeline, notamment la branche du dépôt sur laquelle l'appliquer. Vous pouvez conserver les réglages par défaut et valider la création de votre Pipeline en bas de la fenêtre.

De retour à votre tableau de bord, cherchez à lancer un build de votre Pipeline pour vérifier son bon fonctionnement. Explorez ensuite l'interface pour vérifier le résultat des tests.

<a name="projet" />
 
## Appropriation du projet

Vous êtes désormais en charge du développement du projet PowerGrid, vous devez organiser votre groupe afin de remplir les différents objectifs définis lors de la spécification

<a name="projet-desc" />

### Description de PowerGrid

**PowerGrid** est un outil d'optimisation d'un réseau de distribution électrique. À partir d'un terrain donné en entrée, PowerGrid doit trouver une configuration de lignes électriques permettant d'alimenter tous les clients renseignés.

Les terrains sont des tableaux rectangulaires décrivant une zone, ainsi que des clients et des obstacles répartis sur celle-ci. La figure ci-dessous représente un terrain tel qu'il est possible d'en traiter en utilisant **PowerGrid** :

<p align="center">
  <img src="figures/terrain.png" alt="Exemple de représentation de terrain"/>
</p>

L'objectif de **PowerGrid** est de configurer un réseau électrique reliant chacun des clients (cases bleues) sur le terrain à la case d'entrée électrique (case verte) de celui-ci. Des pénalités peuvent être appliquées au réseau si celui-ci passe par des obstacles (cases rouges).

Un réseau électrique est composé d'un ensemble de noeuds reliés par des arcs. Deux noeuds reliés doivent occuper des cases voisines du terrain (en ligne ou en colonne). Voici un exemple de réseau pouvant couvrir le terrain et assurer la distribution aux clients :

<p align="center">
  <img src="figures/reseau-ex.png" alt="Exemple de réseau recouvrant un terrain"/>
</p>

**PowerGrid** est un programme Python qui inclut les fonctionnalités de gestion de différents terrains, ainsi que de configuration de réseaux électriques permettant de les couvrir.

<a name="projet-arch" />

### Architecture du projet

Le code Python du projet PowerGrid est découpé en plusieurs classes, qui sont décrites dans cette section. Dans l'état actuel des choses, certaines classes sont incomplètes, et il manque bon nombre de tests.

Vous pouvez néanmoins exécuter le script principal `PowerGrid.py` depuis votre environnement virtuel de développement Python, ou lancer les tests existants en exécutant la commande :

```bash
python -m unittest -v
```

Le projet est initialement constitué de plusieurs classes qui interagissent entre elles. Vous pouvez commencer à explorer les fichiers du dépôt pour comprendre leurs rôles.

#### Script `PowerGrid.py`

Ce script contient une démonstration des fonctionnalités de **PowerGrid**. Il charge un fichier présent sur le dépôt contenant la description d'un terrain, affiche ce terrain dans le terminal, puis crée un nouvel objet de type `Reseau`. Cet objet doit représenter une configuration d'un réseau de distribution électrique. Le script demande la génération d'une distribution à partir du `Terrain` chargé, et demande au `Reseau` de valider la configuration ainsi générée.

Le script assigne ensuite une méthode manuelle de configuration au `Reseau`, et demande à nouveau la génération d'une nouvelle configuration. Enfin, le script demande la vérification du nouveau réseau généré.

#### Classe `Terrain`

La classe est accessible dans le fichier `Terrain.py`. Elle doit contenir les informations sur un la topologie d'un terrain, l'emplacement des clients à fournir, de l'entrée et des obstacles. Elle est pour cela munie d'une liste de variables issues de l'énumération `Case` définie dans le même fichier. Une fonction `charger` permet de lire un fichier passé en paramètre, et de peupler un `Terrain` avec ces informations. Plusieurs méthodes définies dans le fichier permettent de faciliter son utilisation.

Un réseau valide généré par PowerGrid devra relier chacun des clients à l'entrée électrique, en passant le moins possible par des obstacles du terrain. 

#### Classe `Reseau`

Elle est définie dans le fichier `Reseau.py`. Cette classe doit permettre de représenter une configuration d'un réseau de distribution. Elle comporte plusieurs attributs :

- `strat` contient la stratégie actuelle pour la configuration du réseau à partir d'un `Terrain` (stratégies de configuration expliquées ci-dessous)
- `noeuds` est un dictionnaire dont les clés sont des entiers positifs correspondants aux identifiants des noeuds du réseau (les cases du terrain sur lesquelles passe le réseau), et dont les valeurs sont des tuples de deux entiers correspondants aux coordonnées des noeuds du réseau sur le `Terrain` correspondant.
- `arcs` est une liste de tuples de deux entiers. Ces tuples représentent des liaisons entre deux noeuds du réseau (deux noeuds du réseau peuvent avoir des coordonnées voisines, sans être reliés par un arc).
- `noeud_entree` est un entier correspondant au noeud du réseau placé sur l'entrée électrique du terrain. Par défaut, cet attribut prend la valeur `-1`.

La figure ci-dessous représente un réseau superposé au terrain sur lequel il doit être déployé, avec les valeurs correspondantes des attributs de la classe `Reseau` :

<p align="center">
  <img src="figures/reseau.png" alt="Exemple de représentation de réseau et des attributs correspondants."/>
</p>

Les méthodes de la classe `Reseau` permettent son utilisation pour la création d'une configuration adaptée à un `Terrain` :
- `definir_entree` permet de désigner le noeud du reseau qui correspond à l'entrée électrique du terrain.
- `ajouter_noeud` permet d'ajouter un noeud au réseau. La fonction doit vérifier que la clé du nouveau noeud est bien un entier positif, et qu'un noeud avec la même clé n'existe pas déjà.
- `ajouter_arc` permet d'ajouter un nouvel arc entre deux noeuds existants. La méthode prend les clés des deux noeuds à relier en paramètre, et doit vérifier que ces noeuds existes bien dans le réseau et ne sont pas déjà reliés.
- `set_strategie` reçoit un objet de type `StrategieReseau` qui devient la nouvelle stratégie de configuration du réseau.
- `valider_reseau` est la méthode qui vérifie que la configuration actuelle du réseau est correcte. Un réseau n'est pas valide si chacun de ses noeuds n'est pas relié au noeud d'entrée.
- `valider_distribution` permet, en utilisant un terrain, de vérifier si la configuration actuelle du réseau permet bien de distribuer de l'électricité à chacun des clients du terrain.
- `configurer` est la méthode qui fait appel à la stratégie du réseau pour trouver une nouvelle configuration.
- `afficher` permet d'afficher la configuration du réseau dans le terminal.
- `afficher_avec_terrain` permet d'afficher à la fois la configuration actuelle du réseau et le terrain auquel elle est censée être adaptée.
- `calculer_cout` permet de calculer le coût total du réseau. Dans ce TP, nous considérons qu'une case d'un terrain représente 1 kilomètre carré. Nous considérons qu'un kilomètre de ligne (un arc du réseau) coûte 1.5 million d'€. De plus, l'aménagement d'un noeud sur un obstacle coût 2M€, et sur toute autre case uniquement 1M€.

#### Fichier `StrategieReseau.py`

Ce fichier contient les différentes stratégie de configuration d'un réseau électrique à partir d'un `Terrain`.

La classe `StrategieReseau` sert de classe abstraite définissant l'interface d'utilisation d'une stratégie. La méthode `configurer` prend un terrain comme unique paramètre, et retourne des valeurs qui remplaceront les attributs du réseau : un entier correspondant à l'attribut `noeud_entree`, un dictionnaire qui devra être utilisé comme l'attribut `noeuds`, et une liste qui remplacera l'attribut `arcs` de la classe `Reseau`. Les classes dérivant de la classe `StrategieReseau` doivent réimplémenter cette méthode.

La classe `StrategieReseauAutomatique` doit déterminer une configuration pour un réseau automatiquement à partir d'un `Terrain`.

La classe `StrategieReseauManuelle` doit implémenter un processus et un affichage permettant de demander à l'utilisateur du programme de choisir lui-même la configuration de son réseau.

#### Fichiers tests

Les fichiers Python contenus dans le répertoire `test` contiennent les tests unitaires du projet. L'objectif est d'écrire des tests pour la majeure partie des fonctions implémentées dans le programme.

<a name="projet-pem" />

### Étapes de développement du projet

#### État des lieux

L'exécution des tests avec le module `unittest` montre que la plupart des tests échoue à l'heure actuelle. Certains tests réussissent même uniquement par chance. En suivant la trace des tests qui échouent, vous pouvez remonter à toutes les fonctions ou tests qui ne sont pas encore implémentés pour l'instant. En voici une liste :
- `Reseau.valider_reseau` : implémentation de la fonction permettant de valider la configuration d'un réseau
- `Reseau.valider_distribution` : implémentation de la fonction permettant de vérifier qu'un réseau couvre bien tous les clients d'un terrain
- `Reseau.afficher` : implémentation de la fonction d'affichage d'un réseau dans le terminal
- `StrategieReseauManuelle.configurer` : implémentation de la fonction qui gère la configuration manuelle d'un réseau à partir d'un terrain. L'utilisateur doit avoir l'occasion d'entrer les informations de la nouvelle configuration. Vous pouvez, par exemple, implémenter une fonction qui, dans une boucle, affiche le réseau et le terrain puis demande à l'utilisateur d'ajouter un noeud à un endroit du terrain. L'utilisateur devrait alors spécifier quels liaisons seront générées entre ce nouveau noeud et les noeuds voisins existants.
- `StrategieReseauAuto.configurer` : implémentation de la fonction qui génère automatiquement une configuration du réseau pour couvrir un terrain donné en paramètres. Dans un premier temps, pensez à des configurations très simples : 1) un réseau couvrant tout le terrain ? 2) un réseau qui couvre toutes les lignes contenant des clients, sans prendre en compte les obstacles ? Dans un second temps, vous pourrez envisager des algorithmes permettant d'optimiser le tracé du réseau.
- `TestReseau.test_definition_entree` : test de la méthode d'assignation de l'identifiant du noeud d'entrée du réseau. Il s'agit de vérifier que la modification de l'attribut correspondant de `Reseau` est bien cohérente avec l'appel à la méthode.
- `TestReseau.test_ajout_noeud` : test de la méthode d'ajout d'un nouveau noeud
- `TestReseau.test_ajout_arc` : test de la méthode d'ajout d'un nouvel arc
- `TestTerrain.test_chargement` : test du chargement d'un fichier contenant la description d'un terrain

L'intégralité de ces méthodes doit être implémenté de manière à ce que le programme soit fonctionnel.

#### Répartition des tâches

Vous formez des groupes de deux à trois étudiants, ayant chacun à disposition un poste de travail configuré pour le développement de ce projet. La plupart des tâches énumérées ci-dessus sont réalisables en parallèle. Vous pouvez chacun choisir une tâche, créer une nouvelle branche de travail sur votre dépôt Git local, et avancer de votre côté.

Essayez d'évaluer la difficulté des tâches, et de les répartir en fonction de vos compétences respectives au sein du groupe. Par exemple, l'implémentation des tests manquants devrait être une tâche assez simple, tandis que l'implémentation de la méthode `StrategieReseauAuto.configurer` demande une certaine réflexion algorithmique.

**Veillez à bien comprendre le fonctionnement du code existant avant de procéder à des développements. Lisez attentivement le code, exécutez-le, possiblement par morceaux, afin de le maîtriser et de pouvoir implémenter les mécanismes manquants.**

Une fois que la tâche choisie est réalisée, vous devez réaliser une fusion de votre branche avec la branche principale, avant de pousser vos modifications vers le dépôt en ligne sur GitHub. Avant cela, veillez à vous assurer que les modifications que vous avez apportées permettent bien de passer les tests concernés.

#### Pour aller plus loin

Une fois que les fonctionnalités énoncées plus haut ont été ajoutées, il vous reste à trouver des pistes d'amélioration du projet **PowerGrid**. Voici quelques pistes :
- Réfléchir à une méthode d'affichage graphique du résultat, préférable à l'affichage sous forme de caractères ASCII dans un terminal (on peut par exemple penser à la génération d'un fichier html, ou à la création d'une image à l'aide de `numpy` et d'`opencv-python`).
- Réfléchir à différentes implémentations d'algorithmes de configuration automatique du réseau (par exemple, un algorithme cherchant à minimiser les distances de chaque client à l'entrée, un algorithme cherchant à minimiser le coût total du réseau...).

Des améliorations peuvent également être apportées au processus d'intégration continue :
- Intégration de rapports sur la qualité du code issues d'un analyseur de syntaxe comme **PyLint**.
- Configuration du serveur pour exécuter le Pipeline lors de nouvelles modifications sur la branche principale.

Toutes les traces de recherches personnelles sur de telles améliorations du projet seront valorisées dans votre rapport.

