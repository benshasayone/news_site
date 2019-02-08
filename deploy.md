# Deploy docs
### Install the EB CLI:
```sh
pip install awsebcli --upgrade --user
```
### To initialize an EB CLI project
```sh
eb init -i
```
> Select the default AWS region: us-east-1 : US East (N. Virginia)
> Setup your credentials:
>- aws-access-id
>- aws-secret-key
> Select an application to use: 2 (for production)
1. afcms-staging
2. afcms-dev
3. afcms
4. [ Create new Application ]
> It appears you are using Docker. Is this correct? (Y/n): Y
> Select a platform version: 1
> Do you wish to continue with CodeCommit?: n
> Do you want to set up SSH for your instances? (Y/n): Y
> Select a keypair: 1 (afcms-dev)

### To Deploy your changes to the selected eb environment:
first commit the changes to git:
```sh
git commit -m "commit message"
```
Then run the following command to deploy the changes to elastic beanstalk from the project folder:
```sh
eb deploy
```
### Check the current beanstalk environment and application:
```sh
 eb status
```
### To Revert Back to Previous Application Version In Elastic Beanstalk:
- Open the Elastic Beanstalk console.
- Choose an application.
- In the navigation pane, choose Application Versions.
- Select the application version that you want to deploy.
- Choose an environment and then choose Deploy.


### To Create A New Environment In Elastic Beanstalk:
- Open the Elastic Beanstalk console.
- Choose the application.
- From the Actions menu in the upper right corner, choose Create environment.
- Choose the Web server environment.
- Choose a Platform: Generic Docker
- For application code select an existing version.
- Choose Create environment.

```sh
pip install virtualenv
```
Create virtual environment using Python3:
```sh
virtualenv -p python3 env
```
Activate it:
```sh
source env/bin/activate
```
Install project dependencies:
```sh
cd afcms/afcms && pip install -r requirements.txt
```
Install Nodejs
```sh
curl -sL https://deb.nodesource.com/setup_8.x | bash - && sudo apt-get install -y nodejs
```
Run `collectstatic` command:
```sh
python manage.py collectstatic
```
Create media folder and copy media files to it:
```sh
mkdir -p media && cp -a fixtures_media/. media/
```
Install node_modules and build bundle files form static files in the project
```sh
npm install && npm run build
```
## Warning! This deploy doc is in unfinished state and contains some commented parts.
<!---
##########################################################################################
TODO: commented for now, needs to be updated with actual staging deploying steps!
##########################################################################################

Run the PostgreSQL interactive terminal:
```sh
sudo -u postgres psql
```
Create database and user ('default' password is used for local development only):
```sh
CREATE DATABASE agfunder;
CREATE ROLE agfunder WITH LOGIN PASSWORD 'default';
```
Grant all privileges to user agfunder on agfunder DB. Then exit psql.
```sh
GRANT ALL PRIVILEGES ON DATABASE agfunder TO agfunder;
Ctrl+D
```
Run migrations:
```sh
python manage.py migrate
```
Create admin account (you'll be prompted to enter login/password):
```sh
python manage.py createsuperuser
```
Remove default nginx conf file
```sh
sudo rm /etc/nginx/sites-enabled/default
```
Copy nginx conf file to the nginx directory:
```sh
sudo cp afcms/nginx_vales.conf /etc/nginx/sites-enabled/
```
Copy uwsgi conf file to the uwsgi directory:
```sh
sudo cp afcms/uwsgi_vales.ini /etc/uwsgi/apps-enabled/
```
Restart postgres, nginx, uwsgi services:
```sh
sudo service postgresql restart
sudo service uwsgi restart
sudo service nginx restart
```
--->
