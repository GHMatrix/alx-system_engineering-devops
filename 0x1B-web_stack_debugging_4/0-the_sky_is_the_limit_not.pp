# Fix for failed requests
exec { 'nginx-fix':
  command => "sudo sed -i 's/worker_processes 4;/worker_processes 7;/g' /etc/nginx/nginx.conf && sudo service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
}
