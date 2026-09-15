# gVisor

## Objective and eligible scenarios

Escape a container sandboxed by the latest stable gVisor `runsc` runtime and compromise the host by executing `/flag.sh gvisor` on the host or reading `/flag`. gVisor Sentry, Gofer, platform, and runtime flaws are eligible. Generic host Linux-kernel flaws are excluded.

- **User-image scenario:** `sudo docker run --rm -it --runtime=runsc <image>`.
- **Arbitrary-payload scenario:** the payload is copied into an organizer-selected image:

```bash
sudo docker create --name zdc-gvisor-payload --runtime=runsc ubuntu:latest sleep infinity
sudo docker start zdc-gvisor-payload
sudo docker cp ./payload zdc-gvisor-payload:/tmp/payload
sudo docker exec zdc-gvisor-payload chmod 0755 /tmp/payload
sudo docker exec -it zdc-gvisor-payload /tmp/payload
sudo docker rm -f zdc-gvisor-payload
```

No privileged mode, host namespace, added capability, runtime socket, or host mount is supplied.

## Local testing environment

On Ubuntu 24.04 with current Docker Engine:

```bash
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
curl -fsSL https://gvisor.dev/archive.key \
  | sudo gpg --dearmor --yes -o /usr/share/keyrings/gvisor-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/gvisor-archive-keyring.gpg] https://storage.googleapis.com/gvisor/releases release main" \
  | sudo tee /etc/apt/sources.list.d/gvisor.list >/dev/null
sudo apt-get update
sudo apt-get install -y runsc
sudo runsc install
sudo systemctl restart docker
sudo docker run --rm --runtime=runsc hello-world
```
