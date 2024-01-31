---
layout: page
title: common/clamscan (English)
description: "A command-line virus scanner."
content_hash: 2a6fe8ff6ecb1edf99239b206fd5220773129581
last_modified_at: 2024-01-31
related_topics:
  - title: Indonesia version
    url: /id/common/clamscan.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/clamscan.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clamscan.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/clamscan.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/clamscan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# clamscan

A command-line virus scanner.
More information: <https://docs.clamav.net/manual/Usage/Scanning.html#clamscan>.

- Scan a file for vulnerabilities:

`clamscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Scan all files recursively in a specific directory:

`clamscan -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Scan data from `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | clamscan -`

- Specify a virus database file or directory of files:

`clamscan --database `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_file_or_directory</span>

- Scan the current directory and output only infected files:

`clamscan --infected`

- Print the scan report to a log file:

`clamscan --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/log_file</span>

- Move infected files to a specific directory:

`clamscan --move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/quarantine_directory</span>

- Remove infected files:

`clamscan --remove yes`
