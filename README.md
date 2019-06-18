# mvr-fe
Front End Application

## Features
- User authentication i.e Registration, Login and Logout
- Dashboard i.e Availale Coupens, Available Special Deals
- Points History i.e Earning History,Spend History
- User Profile 
- Contact Us

- ----------------------------------------------------------------------------------------------
## Skip this steps for now
- Go to the project directory
  ```bash
  cd mvr-fe
  ```
- Build the Docker image
  ```bash
  docker build .
  ```
- Build the Docker image using docker-compose
  ```bash
  docker-compose build
  ```
- Migrate the models to database
  ```bash
  docker-compose run --rm app sh -c 'python manage.py makemigrations'
  docker-compose run --rm app sh -c 'python manage.py migrate'
  ```


#### To run the server
-   ```bash
    docker-compose up
    ```
#### To create a superuser
- ```bash
  docker-compose run --rm app sh -c 'python manage.py createsuperuser'
  ```
- Login to admin page
  <http://localhost:8000/admin/>


#### To run the tests
- ```bash
  docker-compose run --rm app sh -c 'python manage.py test'
  ```
- --------------------------------------------------------------------------
## Start with this steps

#### clone this repository by 
- ```bash
  git clone [link for this repo]
  ```
#### Go inside cloned repo and make virtual environment by (for windows)
- ```bash
  virtualenv [name]
  ```
  
 #### activate virtual env by(for windows)
- ```bash
  [virtual env name]\scripts\activate
  ```
 
 #### install required packages by
- ```bash
  pip install -r requirements.txt
  ```
  
 #### Go to 'app' directory and Run local server by
- ```bash
  python manage.py runserver
  ```
- and go to 
  <http://127.0.0.1:8000> 
- ----------------------------------------------------------------------------------

- --------------------------------------------------------------------------

#### Links
- HomePage: <http://localhost:8000/>
- Register: <http://localhost:8000/register/>
- Login: <http://localhost:8000/login/>
- Logout: <http://localhost:8000/logout/>
- Change Password: <http://localhost:8000/password_change/>
- Forgot Password: <http://localhost:8000/password_reset/>
- -----------------------------------------------------------
- All Available Coupen: <http://127.0.0.1:8000/coupens/>
- Special Deals for User : <http://127.0.0.1:8000/deals/>
- Points Earning History Of User : <http://127.0.0.1:8000/earn_history/>
- Points Spending History Of User : <http://127.0.0.1:8000/spend_history/>
- Contact Us : <http://127.0.0.1:8000/contact_us/>
- User Profile: <http://127.0.0.1:8000/profile/>
  - Enter the link given in terminal to browser
 
