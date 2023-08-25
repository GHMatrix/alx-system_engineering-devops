# Puppet Manifest to Install a Package
package { 'flask':
  ensure => '2.1.0',
  provider => 'pip3',
}
