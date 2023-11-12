---
layout: page
title: common/wpscan (English)
description: "WordPress vulnerability scanner."
content_hash: c0242eeceae5edac2a77ce206fc59d099ebf679d
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# wpscan

WordPress vulnerability scanner.
More information: <https://github.com/wpscanteam/wpscan>.

- Update the vulnerability database:

`wpscan --update`

- Scan a WordPress website:

`wpscan --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Scan a WordPress website, using random user agents and passive detection:

`wpscan --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --stealthy`

- Scan a WordPress website, checking for vulnerable plugins and specifying the path to the `wp-content` directory:

`wpscan --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --enumerate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vp</span>` --wp-content-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote/path/to/wp-content</span>

- Scan a WordPress website through a proxy:

`wpscan --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">protocol://ip:port</span>` --proxy-auth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username:password</span>

- Perform user identifiers enumeration on a WordPress website:

`wpscan --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --enumerate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">u</span>

- Execute a password guessing attack on a WordPress website:

`wpscan --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --usernames `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username|path/to/usernames.txt</span>` --passwords `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/passwords.txt</span>` threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20</span>

- Scan a WordPress website, collecting vulnerability data from the WPVulnDB (<https://wpvulndb.com/>):

`wpscan --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` --api-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>
