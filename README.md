🛠️ Smart Debugger
Agent de debugging autonome basé sur Groq + Streamlit
<p align="left"> <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" /> <img src="https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit" /> <img src="https://img.shields.io/badge/Groq-API-orange?logo=bolt" /> <img src="https://img.shields.io/badge/AI-Powered-brightgreen?logo=githubcopilot" /> <img src="https://img.shields.io/badge/Status-Active-success" /> </p>
📌 Description

Smart Debugger est un agent autonome capable de :

détecter automatiquement les erreurs dans un script Python

analyser l’erreur via un modèle Groq LLaMA

appliquer la correction directement dans le fichier source

afficher les informations et corrections via une interface Streamlit


📂 Structure du projet
smart_debugger/
│
├── app.py                # Interface Streamlit
├── main.py               # Logique principale d'exécution et de correction
├── debugger_agent.py     # Appel Groq + gestion des prompts
├── json_utils.py         # Extraction et parsing JSON du LLM
├── patch_utils.py        # Correction in-place du script
├── config.py             # Chargement de la clé GROQ_API_KEY
│
├── prompt.txt            # Instructions strictes pour le LLM
├── context.txt           # Contexte additionnel
│
├── bug.py                # Script volontairement buggé (exemple)
├── requirements.txt      # Dépendances Python
└── README.md             # Documentation

🚀 Installation
1️⃣ Cloner le dépôt
git clone https://github.com/tonusername/smart_debugger.git
cd smart_debugger

2️⃣ Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.\.venv\Scripts\activate    # Windows

3️⃣ Installer les dépendances
pip install -r requirements.txt

4️⃣ Ajouter la clé API Groq

Crée un fichier .env :

GROQ_API_KEY="ta_cle_api_groq_ici"

⚡ Usage : ligne de commande

Pour analyser et corriger automatiquement bug.py :

python main.py


💡 Le script :

exécute bug.py

détecte l’erreur

envoie l’erreur au LLM

parse la réponse JSON

corrige directement dans le fichier source

ré-affiche le code corrigé

🖥️ Interface graphique (Streamlit)

Lancer l’interface :

streamlit run app.py


Interface :

🗂 Sélection du fichier Python

🖨️ Affichage du code source

❌ Affichage de l’erreur

🔧 Proposition de correction

✔ Application automatique

📄 Visualisation du code corrigé

Aucun JSON brut n’est affiché pour ne pas perturber l’utilisateur.

🧠 Fonctionnement de l’agent IA

Le LLM doit renvoyer strictement ce JSON :

{
  "error_summary": "",
  "explanation": "",
  "diagnostic_steps": [],
  "proposed_fix": "",
  "line_number": 0,
  "fixed_line": "",
  "fixed_code": ""
}


Seul :

line_number

fixed_line

sont utilisés dans la version actuelle.

✨ Correction mono-ligne, propre et minimale.

🔧 Exemple de correction automatique

Script buggé :

def parler(messagee):
    print(messagee)

parler("salut")


Résultat produite par l’IA :

line_number: 2
fixed_line: print(message)


Script corrigé :

def parler(message):
    print(message)

parler("salut")


Sans intervention humaine 🤖

📌 Limitations actuelles
Limitation	Explication
Correction uniquement mono-ligne	Pensé pour éviter les risques d'hallucination du LLM
Pas encore de mode multi-lignes sécurisé	Peut être ajouté ultérieurement
Pas de backup automatique	(Peut être ajouté)
Pas d’affichage de diff	(Option future possible)
🔮 Améliorations futures

Support des corrections multi-lignes

Système de backup automatique (bug_backup.py)

Comparaison avant/après (diff)

Analyse de plusieurs erreurs successives

Historique des corrections appliquées

Choix du modèle Groq dans l’UI

Édition du code directement dans Streamlit

👨‍💻 Auteur

Projet réalisé par Cheickna

Agents autonomes

Debugging intelligent

Intégration API Groq

Streamlit

Parsing JSON robuste

Correction automatique de code
