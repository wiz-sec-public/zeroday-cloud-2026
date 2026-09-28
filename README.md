# zeroday.cloud 2026 Live Hacking Competition

This repository contains setup instructions and local testing environments for targets participating in the zeroday.cloud 2026 live hacking competition.

For more information about the event, check out the [official event page](https://zeroday.cloud).

## Host code execution and file-read rewards

For [Docker](docker/README.md), [containerd](containerd/README.md), [gVisor](gvisor/README.md), [Firecracker](firecracker/README.md), and [NVIDIA Container Toolkit](nvidia-container-toolkit/README.md), the **full advertised target prize requires code execution on the host**, demonstrated by executing the target's `/flag.sh` command on the host.

Reading the host's `/flag` without achieving host code execution remains eligible for a **separate, lower reward tier**. The reward amounts for this tier have not yet been finalized and will be announced separately. All target-specific eligibility requirements still apply.

Earlier versions of these instructions incorrectly listed reading `/flag` as an alternative way to satisfy the full-prize objective. That wording was a mistake on our side; a host file read alone does not qualify for the full advertised target prize. Contact the organizers at zerodaycloud@wiz.io with questions about file-read submissions.

## Database eligibility

The [PostgreSQL](postgresql/README.md), [MariaDB](mariadb/README.md), and [Redis](redis/README.md) targets are **pre-authentication only**. Entries must achieve remote code execution without credentials or an authenticated session, with authentication enabled on the target service. Authenticated (post-auth) database scenarios are not eligible.

Credentials and authenticated commands provided in these local environments are for setup, health checks, and administration only, not eligible starting points for competition entries. See each target's README for its specific requirements.


## Disclaimer

**This repository and its contents are subject to changes without prior notice.** The configurations provided here are offered as a courtesy to researchers to help them prepare for the competition. While we strive to maintain consistency between these testing environments and the actual demo day setups, there may be differences.


## Contact

For questions about target eligibility, exploit requirements, or competition rules, contact: zerodaycloud@wiz.io

If your exploit requires non-standard configurations or specific prerequisites, contact the organizers in advance to ensure eligibility for scoring.
