# access-log-app
# Introduction

Create a react based web application that renders a user interface through which any user can query the fastAPI server, with input parameters and read the access logs of the web proxy set up by us earlier

## Installation + Environment Setup

Used VirtualBox hypervisor to set up linux based VM on my laptop by following the documentation guide. Working with Ubuntu 22.04.3. Found this [video guide](https://youtu.be/-CIepTSsaNE?si=hgXYRCr4Qvt3FW8y) useful.

## Configuring apache2 as my reverse proxy

```sudo apt-get update
sudo apt-get install apache2
sudo apache2ctl configtest
sudo nano /etc/apache2/apache2.conf
```


In the above code insert ServerName <ip_address> (ip adress found by ip a)


```sudo systemctl restart apache2

sudo ufw allow in "Apache Full"

sudo a2enmod proxy
sudo a2enmod proxy_http
sudo a2enmod proxy_balancer
sudo a2enmod lbmethod_byrequests

sudo systemctl restart apache2
```

```
sudo nano /etc/apache2/sites-available/000-default.conf
```

The file content:


```<VirtualHost *:80>
      
        ServerName 127.0.0.1


        ProxyPass / http://localhost:8080/
        ProxyPassReverse / http://localhost:8080/

        RedirectMatch ^/$ /index.html

        <Location "/index.html">
            OptionS -Indexes
            ErrorDocument 200 "OK"
        </Location>

        <Proxy *>
            Order deny,allow
            Allow from all
        </Proxy>
```

```sudo systemctl restart apache2
```

### Apache benchmark

```
ab -n 1000 -c 100 http://127.0.0.1/
```
### Check access log 

```
tail -f /var/log/apache2/access.log
```
### Set up React app

```
npx create-react-app access-log-app
cd access-log-app
npm start
```






