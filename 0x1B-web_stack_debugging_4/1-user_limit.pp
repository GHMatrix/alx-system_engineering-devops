# Changing OS configuration for login with user, holberton and opening file without errors.
exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }
