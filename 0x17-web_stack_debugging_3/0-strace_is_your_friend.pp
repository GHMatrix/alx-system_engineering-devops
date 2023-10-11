# Puppet manifest to fix Apache 500 errori

class apache_fix {
  # Ensuring  correct file exists
  file { '/var/www/html/wp-settings.php':
    ensure => file,
    notify => Exec['modify_wp_settings'],
  }

  # Replacing "phpp" with "php" in wp-settings.php
  exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
  }
}
