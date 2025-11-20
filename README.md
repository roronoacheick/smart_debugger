🛠️ Smart Debugger — Agent de Debugging Automatique (Groq + Streamlit)

Smart Debugger est un agent autonome capable de :

détecter automatiquement les erreurs d’un script Python

analyser l’erreur

demander une correction au modèle Groq (LLaMA)

appliquer la correction directement dans le fichier source

fournir une interface utilisateur simple et propre via Streamlit


🚀 Fonctionnalités

✔ Exécution d’un script Python en sous-processus
✔ Récupération de l’erreur (stderr)
✔ Appel à l’API Groq pour analyse et correction
✔ Réponse garantie au format JSON strict
✔ Correction automatique en remplaçant uniquement la ligne erronée
✔ Interface Streamlit intuitive :

affichage du code source

affichage de l’erreur

proposition de correction

application automatique
✔ Aucun fichier temporaire / duplicata n’est créé
✔ Utilisation simplifiée pour les débutants

📦 Arborescence du projet
smart_debugger/
│
├── app.py                 # Interface Streamlit
├── main.py                # Logique principale d'exécution et de correction
├── debugger_agent.py      # Gestion de l’appel Groq + prompts
├── json_utils.py          # Extraction et parsing JSON du LLM
├── patch_utils.py         # Correction in-place du code Python
├── config.py              # Chargement de la clé API Groq
│
├── prompt.txt             # Prompt strict envoyé au modèle IA
├── context.txt            # Contexte supplémentaire pour guider le modèle
│
├── bug.py                 # Exemple de script volontairement buggé
│
├── requirements.txt       # Bibliothèques Python nécessaires
└── README.md              # Documentation du projet

⚙️ Installation
1. Cloner le dépôt
git clone https://github.com/ton-utilisateur/smart_debugger.git
cd smart_debugger

2. Créer et activer un environnement virtuel
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# OU
.\.venv\Scripts\activate    # Windows

3. Installer les dépendances
pip install -r requirements.txt

4. Ajouter votre clé API Groq dans un .env

Crée un fichier .env :

GROQ_API_KEY="ta_cle_api_icI"

🧠 Utilisation en ligne de commande

Pour analyser et corriger automatiquement bug.py :

python main.py


Le programme :

exécute bug.py

détecte une erreur

envoie l’erreur et le code à Groq

parse la réponse JSON

corrige directement la ligne erronée dans bug.py

réaffiche le code corrigé

🖥️ Interface graphique (Streamlit)

Lancer l’interface :

streamlit run app.py


L’interface permet :

de sélectionner un fichier Python

de visualiser le code source

d’exécuter le script

de voir l’erreur détectée

de recevoir la correction IA

d’appliquer automatiquement la correction

de visualiser le fichier mis à jour

🤖 Fonctionnement de l’agent IA

L’agent utilise deux fichiers :

prompt.txt → instructions strictes au modèle

context.txt → garde-fous, style d’écriture, contraintes

L’IA est forcée de renvoyer un JSON du type :

{
  "error_summary": "",
  "explanation": "",
  "diagnostic_steps": [],
  "proposed_fix": "",
  "line_number": 0,
  "fixed_line": "",
  "fixed_code": ""
}


Seul fixed_line est utilisé dans cette version (correction mono-ligne).

🧪 Exemple d’erreur corrigée

Script buggé :

def parler(messagee):
    print(messagee)

parler("bonjour")


L’IA détecte :

line_number: 2
fixed_line: print(message)


Après correction :

def parler(message):
    print(message)

parler("bonjour")

📌 Limitations actuelles

version actuelle : correction d’une seule ligne

pas encore de correction multi-lignes

dépend d’un prompt strict pour éviter les hallucinations du LLM

nécessite une clé API Groq

(Des améliorations sont possibles, voir section suivante.)

🔮 Améliorations futures possibles

Correction multi-lignes sécurisée

Système de backup automatique avant patch

Affichage du diff (avant/après)

UI Streamlit plus complète (thème, onglets…)

Historique des corrections

Re-exécution automatique après correction

📝 Auteur

Projet réalisé par Cheickna
Dans le cadre d’un TP visant à apprendre :
Débogage automatique, LLM, Groq API, Streamlit et IA appliquée au code.
