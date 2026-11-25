FROM curlimages/curl:latest AS downloader

# Update Envoy to the latest stable GitHub release.
RUN set -eux; \
    url="$(curl -fsSL --retry 3 -o /dev/null -w '%{url_effective}' \
      https://github.com/envoyproxy/envoy/releases/latest)"; \
    release="${url##*/}"; \
    version="${release#v}"; \
    curl -fsSL --retry 3 \
      "https://github.com/envoyproxy/envoy/releases/download/${release}/envoy-${version}-linux-x86_64" \
      -o /tmp/envoy; \
    chmod 0755 /tmp/envoy; \
    printf '%s\n' "${version}" > /tmp/VERSION.txt

FROM envoyproxy/envoy:google-vrp-dev

COPY --from=downloader /tmp/envoy /usr/local/bin/envoy
COPY --from=downloader /tmp/VERSION.txt /etc/envoy/VERSION.txt

RUN cd /etc/envoy \
 && envoy --mode validate -c envoy-edge.yaml \
 && envoy --mode validate -c envoy-origin.yaml
