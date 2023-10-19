# Puppet Manifest for Web Server Configuration

# Ensure all files end with a new line
file_line { 'ensure_newline_at_eof':
  path => '/etc/nginx/nginx.conf',
  line => '\n',
}

# Install Nginx package and ensure it's running
package { 'nginx':
  ensure => installed,
  before => Service['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
}
