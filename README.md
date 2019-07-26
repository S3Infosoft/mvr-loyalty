# s3-loyalty-webapp
Loyalty Web App

## Features
- User authentication i.e Registration, Login and Logout
- Dashboard i.e Availale Coupens, Available Special Deals
- Points History i.e Earning History,Spend History
- User Profile 
- Contact Us
- Purchase Points(NEW)
- Cart(NEW)
- Redeem(NEW)

- ----------------------------------------------------------------------------------------------
## Start with this steps

#### clone this repository by 

- ```bash
  git clone [link for this repo]
  ```
 
 ### NOTE: 
 - .env file is updated in document whose link was shared before
 - save .env file into config file where the settings.py resides
 

  
- Go to the project directory
  ```bash
  cd s3-loyalty-webapp
  ```
- Build the Docker image
  ```bash
  docker build -t [image name]:[tag name] .      or just    docker build .
  ```
- Build the Docker image using docker-compose
  ```bash
  docker-compose build
  ```
#### To run the server
-   ```bash
    docker-compose up
    ```
 #### check your all images
-   ```bash
    docker images
    ```
 #### check your all containers and running containers by
 
-   ```bash
    docker ps -a     and   docker ps
    ```
 
- --------------------------------------------------------------------------

At this point, your Django app should be running at port 9000 on your Docker host. On Docker Desktop for Mac and Docker Desktop for Windows, go to http://localhost:9000 on a web browser to see the website. If you are using Docker Machine, then docker-machine ip MACHINE_VM returns the Docker host IP address, to which you can append the port (<Docker-Host-IP>:9000).
  
- ---------------------------------------------------------------------------------------

#### website will be available now at above url
- login with email id = "test1234@gmail.com" and password= "test@1234"
- Django administration page will be appear,click on "view site " 
## NOTE: 
- don't delete db.sqlite3 
- first go your loyalty web app repo-->app-->payment_tracker_app-->views.py---->callapi() method
- now change BASE_URL attribute inside callapi() to your loyalty web URL e.g "http://192.168.99.100:9000/" 
- remove this 2 lines        #locally
-                            BASE_URL='http://127.0.0.1:8000/'
- save file
- make sure you have that .env file where settings.py resides in loyalty app,make sure that you have "recipient"= "your email id" to get emails
- now run both loyalty and tracker containers
- first go to loyalty website and go to admin panel ,just look at how many Users you have their in loyalty app database
- also look at Guest,Profile,Reservation database,bcoz after sync new entries would be there.
- go to payment-tracker website homepage
- click on sync botton to sync reservation into loyalty app
- resrvation will be shown into "already sync" section after successful sync
- check your Users,Profile,Gust,Reservation database again ,new entries would have been created
- check your email ,email will have email id and password for login

- --------------------------------------------------------------------------
  
 ## Functionality -----> 

 - on clicking view site you will redirect to actual page
 - there will be 2 sections 1.resrvation which are not sync to loyalty web app 2. which are already synced
 - every detail of particular reservation will be shown with "sync" button
 
 
 
 

- ----------------------------------------------------------------------------------


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
 

Redeem -> Checkout
RedeemQueue: User (FK), RI (12M), SD (12M), CD, Status(Pending/Rejected/Completed), Comments(TF)


