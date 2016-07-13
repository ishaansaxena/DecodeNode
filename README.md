# DecodeNode
An upcoming online Cryptic Hunt; currently in development.

### Usage
1. Clone the repository:
`git clone https://github.com/ishaansaxena/DecodeNode.git`
2. Move into project folder:
`cd DecodeNode`
3. Start database server [NOTE: Database settings must be adjusted in ./DecodeNode/settings.py]
4. Migrate to Database:
`python manage.py makemigrations` and then
`python manage.py migrate`
5. Create Super User
`python managepy createsuperuser`, followed by providing Username, Email and Password
6. Start development server
`python manage.py runserver [0.0.0.0:8080]` [NOTE: Address 0.0.0.0 can be used for cross device testing]
7. Create Levels for Cryptic Hunt at localhost:[port]/admin
8. Login and Play
