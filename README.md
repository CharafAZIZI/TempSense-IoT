# 🌡️ Système IoT de Surveillance de la Température et de l'Humidité

## 📌 Présentation du projet

Ce projet consiste à développer une application IoT (Internet of Things) permettant de mesurer, transmettre, enregistrer et visualiser les données de température et d'humidité d'un environnement à l'aide d'un microcontrôleur **ESP8266 NodeMCU** associé à un capteur **DHT11**.

Les mesures collectées sont transmises via Wi-Fi à un serveur web développé avec **Django**. Elles sont ensuite enregistrées dans une base de données SQLite et accessibles à travers un tableau de bord web.

L'objectif est de proposer une solution simple et efficace pour assurer le suivi des conditions environnementales et faciliter la consultation de l'historique des mesures.

## 🎯 Objectifs

- Mesurer la température et l'humidité à l'aide d'un capteur DHT11.
- Collecter les données à travers un ESP8266 NodeMCU.
- Transmettre automatiquement les mesures via une connexion Wi-Fi.
- Développer une API REST pour recevoir et consulter les données.
- Stocker les mesures dans une base de données SQLite.
- Afficher les dernières mesures sur un tableau de bord web.
- Consulter l'historique des relevés environnementaux.

## 🛠️ Technologies utilisées

| Technologie | Utilisation |
|---|---|
| ESP8266 NodeMCU | Acquisition et transmission des données |
| DHT11 | Mesure de la température et de l'humidité |
| Arduino IDE | Programmation du microcontrôleur |
| C/C++ | Développement du firmware ESP8266 |
| Python | Langage du backend |
| Django | Développement de l'application web |
| Django REST Framework | Création de l'API REST |
| SQLite | Stockage des mesures |
| HTML / CSS / JavaScript | Interface utilisateur |
| Tailwind CSS | Mise en forme du tableau de bord |

## 🏗️ Architecture du système

Le système repose sur une architecture composée de trois parties principales :

1. **Couche matérielle :** le capteur DHT11 mesure la température et l'humidité. L'ESP8266 récupère les valeurs et les transmet au serveur via Wi-Fi.
2. **Couche backend :** Django REST Framework expose des endpoints API permettant de recevoir et de consulter les mesures. Les données sont enregistrées dans SQLite.
3. **Couche présentation :** le tableau de bord web affiche les dernières mesures ainsi que l'historique des relevés.

### Schéma de fonctionnement

```text
      ┌─────────────────────┐
      │      Capteur        │
      │       DHT11         │
      └──────────┬──────────┘
                 │
                 ▼
      ┌─────────────────────┐
      │    ESP8266 NodeMCU  │
      │  Acquisition + Wi-Fi│
      └──────────┬──────────┘
                 │
                 │ HTTP / JSON
                 ▼
      ┌─────────────────────┐
      │   Django REST API   │
      │      Backend        │
      └──────────┬──────────┘
                 │
                 ▼
      ┌─────────────────────┐
      │    Base SQLite      │
      │  Stockage des       │
      │      mesures        │
      └──────────┬──────────┘
                 │
                 ▼
      ┌─────────────────────┐
      │  Tableau de bord    │
      │  Web Django         │
      └─────────────────────┘
```

## 📂 Structure du projet

```text
IOT-Project/
│
├── DHT/
│   ├── migrations/
│   ├── templates/
│   │   └── DHT/
│   │       └── dashboard.html
│   ├── admin.py
│   ├── api.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── projet/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── firmware/
│   └── ESP8266_DHT11/
│       ├── ESP8266_DHT11.ino
│       ├── secrets.example.h
│       └── secrets.h
│
├── .env.example
├── .gitignore
├── manage.py
└── requirements.txt
```

*Remarque : les fichiers `.env` et `secrets.h` contiennent des informations privées et ne doivent pas être publiés sur GitHub.*

## ⚙️ Installation et configuration

### 1. Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- Python 3.10 ou supérieur.
- Arduino IDE.
- Git.
- Les pilotes USB adaptés à votre carte ESP8266.
- Une connexion Wi-Fi.

### 2. Cloner le repository

```bash
git clone https://github.com/VOTRE-UTILISATEUR/iot-surveillance-temperature-humidite.git
cd iot-surveillance-temperature-humidite
```

### 3. Créer un environnement virtuel

```bash
python -m venv .venv
```

Activer l'environnement virtuel sous Windows :

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Installer les dépendances

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Configurer les variables d'environnement

Créer un fichier `.env` à la racine du projet à partir de `.env.example`.

Renseigner notamment :

```env
DJANGO_SECRET_KEY=votre_cle_secrete
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_LANGUAGE_CODE=fr-fr
DJANGO_TIME_ZONE=Africa/Casablanca
```

Générer une clé secrète Django :

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Remplacer ensuite `votre_cle_secrete` par la clé générée.

### 6. Initialiser la base de données

```bash
python manage.py migrate
```

### 7. Lancer le serveur Django

Pour un accès local :

```bash
python manage.py runserver
```

Pour permettre à l'ESP8266 ou à un autre appareil du réseau local de communiquer avec le serveur :

```bash
python manage.py runserver 0.0.0.0:8000
```

Le tableau de bord sera accessible à l'adresse :

```text
http://127.0.0.1:8000/
```

## 🔌 Configuration de l'ESP8266

Dans le dossier `firmware/ESP8266_DHT11/`, créer un fichier local `secrets.h` à partir de `secrets.example.h`.

Renseigner les informations de connexion :

```cpp
#define WIFI_SSID "NOM_DU_WIFI"
#define WIFI_PASSWORD "MOT_DE_PASSE_WIFI"
#define SERVER_URL "http://ADRESSE_IP_PC:8000/api/post/"
```

Remplacer `ADRESSE_IP_PC` par l'adresse IPv4 de l'ordinateur hébergeant Django.

Ensuite :

1. Ouvrir le fichier `ESP8266_DHT11.ino` dans Arduino IDE.
2. Sélectionner la carte ESP8266 NodeMCU.
3. Vérifier les branchements du capteur DHT11.
4. Compiler et téléverser le programme.
5. Ouvrir le moniteur série pour vérifier les mesures et la transmission.

## 🔗 API REST

L'application expose les endpoints suivants :

| Méthode | Endpoint | Description |
|---|---|---|
| GET | `/api/get/` | Récupérer les mesures enregistrées |
| POST | `/api/post/` | Envoyer une nouvelle mesure |

### Exemple de données JSON

```json
{
    "temperature": 25.5,
    "humidity": 60.0
}
```

## 📊 Tableau de bord

Le tableau de bord permet notamment de :

- Consulter la dernière température mesurée.
- Consulter le dernier taux d'humidité.
- Visualiser les dernières mesures enregistrées.
- Suivre l'évolution des données collectées grâce à l'actualisation périodique de l'interface.

## 🔐 Sécurité

Quelques bonnes pratiques sont appliquées :

- Utilisation d'un fichier `.env` pour les paramètres sensibles de Django.
- Exclusion des fichiers contenant les identifiants Wi-Fi du dépôt Git.
- Utilisation d'un fichier `.gitignore` pour protéger les fichiers locaux et temporaires.

**Important :** cette version est destinée à un environnement de développement ou à un réseau local. Une authentification des appareils IoT et une configuration sécurisée sont nécessaires avant toute exposition publique.

## 🚀 Améliorations possibles

- Ajouter des graphiques pour visualiser l'évolution de la température et de l'humidité.
- Ajouter des seuils configurables et des alertes en cas de dépassement.
- Prendre en charge plusieurs capteurs.
- Ajouter un historique filtrable par date.
- Déployer l'application sur un serveur accessible à distance.

## 👨‍💻 Auteur

**Charaf AZIZI**

Projet académique réalisé dans le cadre de l'apprentissage de l'Internet des objets (IoT), du développement web et de la communication entre systèmes embarqués et applications backend.

---

⭐ Si ce projet vous intéresse, n'hésitez pas à explorer le repository et à proposer des améliorations.