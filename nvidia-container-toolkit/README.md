# NVIDIA Container Toolkit

## Objective and eligible scenario

Escape an NVIDIA-enabled Docker container and achieve code execution on the host, demonstrated by executing `/flag.sh nct` on the host. Vulnerabilities in NVIDIA Container Toolkit components and NVIDIA driver components exposed to the container are eligible. Generic Linux-kernel vulnerabilities are excluded.

The full advertised target prize requires host code execution. Reading the host's `/flag` without host code execution is eligible for a separate, lower reward tier, with the amount pending. See the [host code execution and file-read reward clarification](../README.md#host-code-execution-and-file-read-rewards).

Contestants provide their own container image, launched as:

```bash
sudo docker run --rm -it --runtime=nvidia --gpus all <image>
```

No privileged mode, host namespace, added capability, Docker socket, or host mount is supplied.

## Local testing environment

On demo day, the environment will be Ubuntu 24.04 with Docker and the NVIDIA Container Toolkit installed from their official releases.

- NVIDIA Container Toolkit: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html
