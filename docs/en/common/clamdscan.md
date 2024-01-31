---
layout: page
title: common/clamdscan (English)
description: "A command-line virus scanner using the ClamAV Daemon."
content_hash: 8cac9c03804a6db80373217b7052bad9b443e6da
last_modified_at: 2024-01-31
related_topics:
  - title: Indonesia version
    url: /id/common/clamdscan.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/clamdscan.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/clamdscan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clamdscan

A command-line virus scanner using the ClamAV Daemon.
More information: <https://docs.clamav.net/manual/Usage/Scanning.html#clamdscan>.

- Scan a file or directory for vulnerabilities:

`clamdscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Scan data from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | clamdscan -`

- Scan the current directory and output only infected files:

`clamdscan --infected`

- Print the scan report to a log file:

`clamdscan --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/log_file</span>

- Move infected files to a specific directory:

`clamdscan --move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/quarantine_directory</span>

- Remove infected files:

`clamdscan --remove`

- Use multiple threads to scan a directory:

`clamdscan --multiscan`

- Pass the file descriptor instead of streaming the file to the daemon:

`clamdscan --fdpass`
