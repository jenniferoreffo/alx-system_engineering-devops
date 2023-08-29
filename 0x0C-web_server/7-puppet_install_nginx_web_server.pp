# add stable version of nginx
exec { 'add nginx stable repo':
  command => 'sudo add-apt-repository ppa:nginx/stable',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# update software packaged list
exec { 'update packages':
  command => 'apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# install nginx
package { 'nginx':
  ensure    => 'installed',
}

# allow HTTP
exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => '! dpkg -l nginx | egrep \'ii.*nginx\'  > /dev/null 2>&1',
}

# change folder rights
exec { 'chmod www folder':
  command => 'chmod -R 755 /var/www',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# creat index file
file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

#create index file
file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n"
}

#add redirection and ereor page
file { ' Nginx default confilr file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content =>
"server {
        listen 80 default_server;
        listen [::]:80 default_server;
               root /var/ww/html;
        # Add index php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;
        server_name_;
        location / {
                #first attempt to serve request as file, then as directory, the fall back to displaying 404. try_files \usr \$uri/ =404;}
        }
        error_page 404 /404.html:
        location /404.html {
            internal;
        }
        if (\$request_filename ~ redirect_me){            rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        }
}
",
}
     
# restart nginx
exec { 'restart service':
  command => 'service ngnix restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}

# start service nginx
service { 'nginx': 
  ensure  => running,
  require => package['nginx'],
}
