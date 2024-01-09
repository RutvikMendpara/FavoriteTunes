# My Favourite Tunes

## Setup and Run

1. Install Django:

   ```bash
   pip install django
   ```

2. Clone the repository:

   ```bash
   git clone <repository-url>
   cd FavoriteTunes
   ```

3. Run migrations:

   ```bash
   python manage.py migrate
   ```

4. Create a superuser to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the admin panel at `http://127.0.0.1:8000/admin/` and add your favorite tunes and artists.

7. View your song list at `http://127.0.0.1:8000/`.
