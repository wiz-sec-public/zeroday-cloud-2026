#!/bin/sh
set -eu

keystore_file="${CATALINA_HOME}/conf/keystore.p12"

if [ ! -s "$keystore_file" ]; then
  keytool -genkeypair -noprompt \
    -alias tomcat \
    -keyalg RSA \
    -storetype PKCS12 \
    -keystore "$keystore_file" \
    -storepass changeit \
    -keypass changeit \
    -validity 365 \
    -dname "CN=localhost, OU=zeroday.cloud, O=zeroday.cloud, C=US" \
    -ext "SAN=dns:localhost,ip:127.0.0.1"
fi

exec "${CATALINA_HOME}/bin/catalina.sh" run
