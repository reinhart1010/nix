---
layout: page
title: common/gobuster (English)
description: "Brute-forces hidden paths on web servers and more."
content_hash: 1a9f188d2c3fca24e5496030a69d978857f01d10
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/gobuster.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gobuster

Brute-forces hidden paths on web servers and more.
More information: <https://github.com/OJ/gobuster>.

- Discover directories and files that match in the wordlist:

`gobuster dir --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/</span>` --wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Discover subdomains:

`gobuster dns --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` --wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Discover Amazon S3 buckets:

`gobuster s3 --wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Discover other virtual hosts on the server:

`gobuster vhost --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/</span>` --wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Fuzz the value of a parameter:

`gobuster fuzz --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/?parameter=FUZZ</span>` --wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Fuzz the name of a parameter:

`gobuster fuzz --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/?FUZZ=value</span>` --wordlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
