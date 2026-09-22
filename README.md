# zeroday.cloud 2026 Live Hacking Competition

This repository contains setup instructions and local testing environments for targets participating in the zeroday.cloud 2026 live hacking competition.

For more information about the event, check out the [official event page](https://zeroday.cloud).

## Database eligibility

The [PostgreSQL](postgresql/README.md), [MariaDB](mariadb/README.md), and [Redis](redis/README.md) targets are **pre-authentication only**. Entries must achieve remote code execution without credentials or an authenticated session, with authentication enabled on the target service. Authenticated (post-auth) database scenarios are not eligible.

Credentials and authenticated commands provided in these local environments are for setup, health checks, and administration only, not eligible starting points for competition entries. See each target's README for its specific requirements.


## Disclaimer

**This repository and its contents are subject to changes without prior notice.** The configurations provided here are offered as a courtesy to researchers to help them prepare for the competition. While we strive to maintain consistency between these testing environments and the actual demo day setups, there may be differences.


## Contact

For questions about target eligibility, exploit requirements, or competition rules, contact: zerodaycloud@wiz.io

If your exploit requires non-standard configurations or specific prerequisites, contact the organizers in advance to ensure eligibility for scoring.
