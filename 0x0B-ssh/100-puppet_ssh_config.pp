# SSH configuration file
file { '/home/your_username/.ssh/config':
  ensure  => present,
  owner   => 'your_username',
  group   => 'your_username_group',
  mode    => '0600',
  content => "
Host 228879-web-01
    HostName 54.166.128.19
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
",
}
