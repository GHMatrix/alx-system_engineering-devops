exec { 'kill_killmenow_process':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
}
