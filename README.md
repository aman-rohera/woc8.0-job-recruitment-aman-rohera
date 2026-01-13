# 🎃 CareerSphere: The Haunted Recruitment Portal

**CareerSphere** is a recruitment platform connecting **Employers (Dungeon Masters)** and **Job Seekers (Wandering Specters)**. Built for the **Winter of Code 8.0**, this project re-imagines the hiring process through a "Horror" lens. It connects users in a fully functional, yet spookily themed, web application where "Resumes" become "Resurrection Scrolls" and "Addresses" become "Crypt Locations".

## Installation

Instructions on how to summon the project and get it running on your local machine.

### Prerequisites

_Before casting spells, ensure you have the following tools installed:_

* **Python 3.8+**: The core language.
* **Git**: For version control.
* **Pip**: Package installer (usually comes with Python).

### Step-by-Step Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/](https://github.com/)<aman-rohera>/woc8.0-job-recruitment-<aman-rohera>.git
    cd woc8.0-job-recruitment-<aman-rohera>
    ```

2.  **Summon the Virtual Environment (The Graveyard)**
    ```bash
    python -m venv venv
    
    # Windows
    .\venv\Scripts\activate
    
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install django
    ```

4.  **Cast Spells (Database Migrations)**
    Initialize the database with the custom `CursedUser` models.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create an Overlord (Superuser)**
    Create an admin account to manage the portal.
    ```bash
    python manage.py createsuperuser
    ```

## Usage

Once installed, you can launch the portal to test the recruitment features.

1.  **Start the Server**
    ```bash
    python manage.py runserver
    ```

2.  **Access the Portal**
    * Open your browser and visit: `http://127.0.0.1:8000/`
    * **Job Seekers:** Sign up as a "Wandering Specter" to upload your "Resurrection Scroll" (Resume).
    * **Employers:** Sign up as a "Dungeon Master" to post new job listings.

3.  **Access the Admin Panel**
    * Visit: `http://127.0.0.1:8000/admin/`
    * Log in with your Superuser account to manage Users and Profiles.
    * Note that all fields use "Spooky" variable names in the code but have clear labels in the admin panel (e.g., *Resurrection Scroll* is labeled as *Resume*).

## Technologies

_The dark arts used to build this project:_

* [Python](https://www.python.org/) - The spell language (Backend Logic).
* [Django](https://www.djangoproject.com/) - The web framework.
* [SQLite](https://www.sqlite.org/index.html) - Development Database.
* **HTML/CSS** - Custom Halloween UI with "Creepster" fonts.

## Contributing

If you wish to add more horror features to this project:

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## Documentation

* **Project Specs**: Refer to the Winter of Code 8.0 documentation for strict requirements.
* **Django Docs**: [Official Django Documentation](https://docs.djangoproject.com/).
