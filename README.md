# mvr-fe
Front End Application

## Features
- User authentication i.e Registration, Login and Logout
- Dashboard i.e Availale Coupens, Available Special Deals
- Points History i.e Earning History,Spend History
- User Profile 
- Contact Us
-Purchase Points(NEW)

- ----------------------------------------------------------------------------------------------
## Start with this steps

#### clone this repository by 
- ```bash
  git clone [link for this repo]
  ```
  
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

At this point, your Django app should be running at port 8000 on your Docker host. On Docker Desktop for Mac and Docker Desktop for Windows, go to http://localhost:8000 on a web browser to see the website. If you are using Docker Machine, then docker-machine ip MACHINE_VM returns the Docker host IP address, to which you can append the port (<Docker-Host-IP>:8000).
- ---------------------------------------------------------------------------------------
  
 ## NEW FEATURE -----> PURCHASE POINTS
 
 - .env file containing razorpay credential are not include in this repo
 - whats app me for .env file 
 - paste .env file into config file where the settings.py resides
 - the again build your image by
 -   ```bash
    docker-compose up --build
    ```
 - website will be live ,go to purchase points button in navbar any complete your payment

 
- ----------------------------------------------------------------------------------
#### website will be available now at above url
- login with email id = "test1234@gmail.com" and password= "test@1234"
- visit all features mentioned in 'features section' ABOVE by clicking the link/buttons available at navigation bar
- for profile click on circlular image and click on profile
- now you can see your profile and can change email id,profile pic etc
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
 
