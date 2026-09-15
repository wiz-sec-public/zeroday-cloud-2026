# containerd

## Objective and eligible scenarios

Escape a containerd container and compromise the Ubuntu host by executing `/flag.sh containerd` on the host or reading the host file `/flag`. Generic Linux-kernel vulnerabilities are excluded.

- **User-image scenario:** `sudo nerdctl run --rm -it <image>`.
- **Arbitrary-payload scenario:** the payload is copied into an organizer-selected `ubuntu:latest` container:

```bash
sudo nerdctl create --name zdc-containerd-payload ubuntu:latest sleep infinity
sudo nerdctl start zdc-containerd-payload
sudo nerdctl cp ./payload zdc-containerd-payload:/tmp/payload
sudo nerdctl exec zdc-containerd-payload chmod 0755 /tmp/payload
sudo nerdctl exec -it zdc-containerd-payload /tmp/payload
sudo nerdctl rm -f zdc-containerd-payload
```

No privileged mode, host namespace, added capability, runtime socket, or host mount is supplied.

## Local testing environment

On demo day, we will use Ubuntu 24.04 with the latest versions of containerd and nerdctl downloaded from their official GitHub repositories:

- containerd: https://github.com/containerd/containerd
- nerdctl: https://github.com/containerd/nerdctl
