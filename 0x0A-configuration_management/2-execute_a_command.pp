# Puppet Manifest to Execute a command
exec { 'kill_killmenow_process':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
  path    => ['/bin', '/usr/bin', '/usr/local/bin']
}
