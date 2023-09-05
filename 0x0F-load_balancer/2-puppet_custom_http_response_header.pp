# configure nginx webserver

exec { 'update system':
  command  => 'sudo apt-get update',
  provider => shell,
 }

exec { 'installing web_server':}
  command  => 'sudo apt-get -y install nginx; sudo ufw allow "Nginx HTTP"',
  provider => shell,
} 

exec { 'configure server':
  command  => 'sudo sed -i  "0,/location \/ {/s//location \/ {\n\t\tadd_header X-Served-By \'03-$(hostname | cut -c 8-)\ ';',
  provider => shell,
}

exec  { 'restart server':
  command  => 'sudo service nginx restart',
  provider => shell,
}

