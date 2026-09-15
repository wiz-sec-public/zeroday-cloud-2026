#!/bin/sh
set -eu

runtime_config=/tmp/zdc-httpd.conf
cp /usr/local/apache2/conf/httpd.conf "$runtime_config"
sed -i -E \
  -e 's/^#(LoadModule ssl_module modules\/mod_ssl\.so)/\1/' \
  -e 's/^#(LoadModule socache_shmcb_module modules\/mod_socache_shmcb\.so)/\1/' \
  "$runtime_config"
printf '\nInclude conf/extra/zdc-ssl.conf\n' >> "$runtime_config"

exec httpd-foreground -f "$runtime_config"
