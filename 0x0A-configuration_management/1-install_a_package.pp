# Puppet Manifest to Install Flask 2.1.0 using pip3

package { 'pip3':
  ensure => 'installed',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
