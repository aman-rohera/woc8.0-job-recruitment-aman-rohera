🎃 CareerSphere: The Haunted Recruitment Portal
Winter of Code 8.0 – Django Category

CareerSphere is a recruitment platform connecting Employers (Dungeon Masters) and Job Seekers (Wandering Specters). Built with Django, this project blends robust backend logic with a unique Halloween-themed aesthetic, transforming the mundane task of job hunting into a thrilling journey through the afterlife.

👻 Project Overview
CareerSphere re-imagines the hiring process. Instead of standard user roles, we have Cursed Users; instead of resumes, we handle Resurrection Scrolls. The platform is fully functional for recruitment but "horror-fied" to meet the Winter of Code thematic challenges.

🌟 Key Features
🧟 For Job Seekers ("Wandering Specters")
Profile Creation: Build a SoulProfile with skills ("Dark Arts") and contact info ("Telepathy Frequency").

Resume Upload: Securely upload CVs as Resurrection Scrolls.

Includes custom validation to ensure only ancient scrolls (PDFs) are accepted.

Job Hunting: Browse the graveyard of opportunities and apply to open positions.

🧛‍♀️ For Employers ("Dungeon Masters")
Coven Management: Create and manage company profiles with detailed descriptions.

Summon Minions: Post job listings with requirements, salary ranges, and descriptions.

Soul Binding: Track applications and review the "souls" (candidates) that have applied to your dungeon.

🕸️ Admin & Security
Secure Authentication: Built on Django’s robust auth system, customized with AbstractUser to handle role-based access control.

Graveyard Dashboard: A custom-styled admin panel for managing users, listings, and content.

🛠 Tech Stack
Core Framework: Django 5.0+ (Python 3.8+)

Database: SQLite (Development) / PostgreSQL (Production ready)

Frontend: HTML5, CSS3 (Custom "Creepster" Fonts & Halloween Color Palette)

File Handling: Django FileField with PDF Validation

🎃 The "Horror-fication" Logic
This project implements the "Code Horror-fication" challenge where backend logic mirrors the spooky theme without sacrificing readability:

App Name: User management is handled by the souls app.

Models:

CursedUser: Handles login and role assignment.

SoulProfile: Stores user details (Address → Crypt Location, Experience → Years of Decay).

Readability: All spooky variable names are mapped to standard meanings using Django's verbose_name, ensuring the Admin Panel remains user-friendly (e.g., "Resurrection Scroll" is clearly labeled as "Resume").

🔮 Installation & Setup
Follow these steps to summon the project locally:

Clone the Repository

Bash

git clone https://github.com/<your-username>/woc8.0-job-recruitment-<your-name>.git
cd woc8.0-job-recruitment-<your-name>
Summon the Environment (Virtual Env)

Bash

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Install Dependencies

Bash

pip install django
Cast Spells (Migrations) Initialize the database with the custom CursedUser models:

Bash

python manage.py makemigrations
python manage.py migrate
Create an Overlord (Superuser) Access the admin panel by creating a superuser:

Bash

python manage.py createsuperuser
Open the Portal

Bash

python manage.py runserver
Visit http://127.0.0.1:8000/ to enter the portal.