---
layout: page
title: common/dirsearch (English)
description: "Web path scanner."
content_hash: d7da1d683e14b1c0baf5062c839416c996fc322c
related_topics:
  - title: Türkçe version
    url: /tr/common/dirsearch.html
    icon: bi bi-globe
---
# dirsearch

Web path scanner.
More information: <https://github.com/maurosoria/dirsearch>.

- Scan a web server for common paths with common extensions:

`dirsearch --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --extensions-list`

- Scan a list of web servers for common paths with the `.php` extension:

`dirsearch --url-list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/url-list.txt</span>` --extensions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php</span>

- Scan a web server for user-defined paths with common extensions:

`dirsearch --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --extensions-list --wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/url-paths.txt</span>

- Scan a web server using a cookie:

`dirsearch --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --extensions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php</span>` --cookie `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cookie</span>

- Scan a web server using the `HEAD` HTTP method:

`dirsearch --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --extensions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php</span>` --http-method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Scan a web server, saving the results to a `.json` file:

`dirsearch --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --extensions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">php</span>` --json-report `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/report.json</span>
