# Firecracker

## Objective and eligible scenario

Escape from a standard Firecracker microVM guest and compromise the Linux host by executing `/flag.sh firecracker` on the host or reading `/flag`. The attacker starts as root inside the guest. Vulnerabilities in Firecracker and its jailer are eligible; generic KVM, host-kernel, and guest-kernel vulnerabilities are excluded.

The competition microVM uses the current Firecracker defaults, a read/write ext4 root drive, one network interface, and no host filesystem sharing or additional host devices. Firecracker is launched through the supplied `jailer` with its default seccomp filters. There is no network service port: the attack begins inside the microVM.

## Local testing environment

Use a bare-metal or nested-virtualization-capable Ubuntu 24.04 host with `/dev/kvm`:

```bash
sudo apt-get update
sudo apt-get install -y ca-certificates curl tar acl jq openssh-client squashfs-tools e2fsprogs
test -r /dev/kvm && test -w /dev/kvm

case "$(uname -m)" in
  x86_64|aarch64) firecracker_arch="$(uname -m)" ;;
  *) echo "unsupported architecture" >&2; exit 1 ;;
esac

release_root=https://github.com/firecracker-microvm/firecracker/releases
firecracker_tag="$(basename "$(curl -fsSLI -o /dev/null -w '%{url_effective}' "${release_root}/latest")")"
firecracker_tmp="$(mktemp -d)"
curl -fsSL "${release_root}/download/${firecracker_tag}/firecracker-${firecracker_tag}-${firecracker_arch}.tgz" \
  -o "${firecracker_tmp}/firecracker.tgz"
tar -C "${firecracker_tmp}" -xzf "${firecracker_tmp}/firecracker.tgz"
sudo install -m 0755 "${firecracker_tmp}/release-${firecracker_tag}-${firecracker_arch}/firecracker-${firecracker_tag}-${firecracker_arch}" /usr/local/bin/firecracker
sudo install -m 0755 "${firecracker_tmp}/release-${firecracker_tag}-${firecracker_arch}/jailer-${firecracker_tag}-${firecracker_arch}" /usr/local/bin/jailer
rm -rf "${firecracker_tmp}"
firecracker --version
jailer --version
```

Build the guest kernel/rootfs and configure the jailed VM using the matching release's [Getting Started guide](https://github.com/firecracker-microvm/firecracker/blob/main/docs/getting-started.md) and [jailer documentation](https://github.com/firecracker-microvm/firecracker/blob/main/docs/jailer.md).
