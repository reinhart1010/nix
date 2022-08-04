---
layout: page
title: linux/logwatch (English)
description: "Summarizes many different logs for common services (e.g. apache, pam_unix, sshd, etc.) in a single report."
content_hash: 854c3bf774e55f0f99d6e5c5ca81105a882e1855
related_topics:
  - title: Deutsch version
    url: /de/linux/logwatch.html
    icon: bi bi-globe
---
# logwatch

Summarizes many different logs for common services (e.g. apache, pam_unix, sshd, etc.) in a single report.
More information: <https://manned.org/logwatch>.

- Analyze logs for a range of dates at a certain level of detail:

`logwatch --range `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yesterday|today|all|help</span>` --detail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">low|medium|others</span>`'`

- Restrict report to only include information for a selected service:

`logwatch --range `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all</span>` --service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apache|pam_unix|etc</span>
