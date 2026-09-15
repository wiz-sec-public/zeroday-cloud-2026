# Ubuntu Kernel

## Objective and eligible scenario

Exploit a previously unknown Ubuntu Linux-kernel vulnerability from a standard Docker container and compromise the host by executing `/flag.sh ubuntu` on the host. The flaw must be unknown to Ubuntu and upstream Linux maintainers, with no available unmerged or merged patch. Userspace-runtime flaws are not eligible for this target.

Contestants provide an image, launched without extra privilege:

```bash
sudo docker run --rm -it <image>
```

No privileged mode, host namespace, added capability, Docker socket, or host mount is supplied.

## Target Configuration Options

- **Architecture:** `amd64` or `arm64`.
- **Processor:** Intel or AMD for `amd64`.
- **Ubuntu version:** Any release still in Canonical's **standard security maintenance** window on demo day.
- **Kernel:** The latest fully updated generic kernel distributed for the selected Ubuntu release. Ubuntu mainline builds and held-back security updates are not eligible.

See the [Ubuntu release cycle](https://ubuntu.com/about/release-cycle) for currently supported releases.

## Local testing environment

Install the selected release normally, keep its supported generic-kernel meta-package installed, and apply every published update immediately before testing:

```bash
sudo apt-get update
sudo apt-get install -y --install-recommends linux-generic
sudo apt-get full-upgrade -y
sudo reboot
```

After reboot, record the exact updated build:

```bash
uname -a
apt-cache policy linux-generic
```

Install Docker Engine through `https://get.docker.com`.
