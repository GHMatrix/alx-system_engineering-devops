# Puppet manifest to fix Apache 500 errori

class apache_fix {
  # Ensuring  correct file exists
  file { '/var/www/html/wp-settings.php':
    ensure => file,
    notify => Exec['modify_wp_settings'],
  }

  # Replacing "phpp" with "php" in wp-settings.php
  exec { 'modify_wp_settings':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/',
    require => File['/var/www/html/wp-settings.php'],
  }

  # Ensuring Apache is running with right config
  service { 'apache2':
    ensure => 'running',
    enable => true,
    require => Exec['modify_wp_settings'],
  }
}
