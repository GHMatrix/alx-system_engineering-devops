# Puppet manifest on how to install Nginx
# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure => present,
  content => "
server {
  listen 80;
  server_name _;
  
  location /redirect_me {
    return 301 http://example.com/;
  }

  location / {
    root   /var/www/html;
    index  index.html;
  }
}
",
  require => Package['nginx'],
  notify => Service['nginx'],
}

# Create HTML directory and index file
file { '/var/www/html':
  ensure => directory,
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
  require => File['/var/www/html'],
}

# Start and enable Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}
