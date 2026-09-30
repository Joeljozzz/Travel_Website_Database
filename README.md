# ✈️ Travel Website Database

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

A Flask-powered web application demonstrating relational database management (RDBMS) and data modeling for a travel platform. Features full CRUD operations for managing travel destinations using PostgreSQL and SQLAlchemy, paired with modular Jinja2 templates and custom CSS styling.

---

## 🌟 Key Features

- **Destination Catalog**: Browse curated travel destinations with titles, descriptions, and image previews.
- **Complete CRUD Operations**: Create, view, modify, and delete travel destinations directly from the web interface.
- **Relational Persistence**: PostgreSQL database integration powered by Flask-SQLAlchemy ORM.
- **Modular Frontend**: Responsive layout built with Jinja2 template inheritance and custom CSS styling.
- **Dual-Database Architecture Concept**: Designed to demonstrate structured transactional data modeling (RDBMS) alongside extensible unstructured data storage (NoSQL).

---

## 🏛️ System Architecture

```text
┌─────────────────────────────────────────────────────────┐
│  CLIENT TIER               [Travel Web Interface]       │
│  User interactions, search queries, and destination view│
├─────────────────────────────────────────────────────────┤
│  APPLICATION TIER          [Flask Web Server]           │
│  Routing logic, CRUD handlers, and ORM persistence      │
├─────────────────────────┬───────────────────────────────┤
│  DATA TIER (RDBMS)      │  DATA TIER (NoSQL / Concept)  │
│  [PostgreSQL]           │  [Document / Key-Value Store] │
│  Structured records     │  Reviews, logs & flexible data│
│  (Destinations, Users)  │                               │
└─────────────────────────┴───────────────────────────────┘
```

### Data Schema (`Destination`)

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | `Integer` | Primary Key, Auto-increment | Unique identifier for each destination |
| `name` | `String(80)` | Unique, Not Null | Destination name/title |
| `description` | `String(500)` | Not Null | Detailed description of the location |
| `image` | `String(200)` | Not Null | Direct URL to destination image asset |

---

## 📁 Project Structure

```text
Travel_Website_Database/
├── static/
│   └── css/
│       └── styles.css          # Application layout and component styling
├── templates/
│   ├── base.html               # Base layout with navigation and footer
│   ├── home.html               # Landing page
│   ├── destinations.html       # Destination gallery with edit/delete actions
│   ├── add_destination.html    # Form to create new destinations
│   ├── edit_destination.html   # Form to update existing destinations
│   ├── delete_destination.html # Confirmation template for destination removal
│   ├── about.html              # About Us information page
│   └── contact.html            # Contact inquiry form
├── app.py                      # Flask application, routing, and SQLAlchemy models
├── App.docx                    # Project documentation & design report
├── LICENSE                     # MIT License
└── README.md                   # Repository documentation
```

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Joeljozzz/Travel_Website_Database.git
   cd Travel_Website_Database
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # On macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate

   # On Windows:
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install required packages:**
   ```bash
   pip install Flask Flask-SQLAlchemy psycopg2-binary
   ```

4. **Configure PostgreSQL Database:**
   Ensure PostgreSQL is running locally and create a database:
   ```sql
   CREATE DATABASE traveldb;
   ```
   Update the database URI in `app.py` with your credentials:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://<username>:<password>@localhost:5432/traveldb'
   ```

5. **Initialize Database Tables:**
   ```bash
   python -c "from app import app, db; app.app_context().push(); db.create_all()"
   ```

6. **Run the Application:**
   ```bash
   python app.py
   ```
   Open your browser and navigate to `http://localhost:5000`.

---

## 🧭 Routes & Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | `GET` | Home landing page |
| `/destinations` | `GET` | List all destination cards |
| `/add_destination` | `GET`, `POST` | Form and submission handler for new destinations |
| `/edit_destination/<id>` | `GET`, `POST` | Form and submission handler for updating a destination |
| `/delete_destination/<id>` | `GET` | Remove a destination by ID and redirect |
| `/about` | `GET` | About page |
| `/contact` | `GET` | Contact inquiry form |

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
