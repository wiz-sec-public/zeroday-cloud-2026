# Docker

## Objective and eligible scenarios

Escape a Docker container and compromise the Ubuntu host by executing `/flag.sh docker` on the host or reading the host file `/flag`. Generic Linux-kernel vulnerabilities are excluded.

- **User-image scenario:** provide an image, launched as `docker run --rm -it <image>`.
- **Arbitrary-payload scenario:** provide a shell script or executable. It is copied into an organizer-selected, unprivileged `ubuntu:latest` container and executed as shown below. Contestants do not choose this scenario's image.

```bash
docker create --name zdc-docker-payload ubuntu:latest sleep infinity
docker start zdc-docker-payload
docker cp ./payload zdc-docker-payload:/tmp/payload
docker exec zdc-docker-payload chmod 0755 /tmp/payload
docker exec -it zdc-docker-payload /tmp/payload
docker rm -f zdc-docker-payload
```

The containers receive no privileged mode, host namespace, host socket, added capability, or host filesystem mount.

## Local testing environment

Use Ubuntu 24.04 and install the latest stable Docker Engine through Docker's official installer:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo systemctl enable --now docker
sudo docker version
```
