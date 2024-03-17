---
layout: page
title: common/amass-enum (English)
description: "Find subdomains of a domain."
content_hash: dad1157e287e33bea5a0b285424fa9e7c2cc4336
last_modified_at: 2024-03-17
related_topics:
  - title: español version
    url: /es/common/amass-enum.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/amass-enum.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/amass-enum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# amass enum

Find subdomains of a domain.
More information: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- Find (passively) subdomains of a [d]omain:

`amass enum -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>

- Find subdomains of a [d]omain and actively verify them attempting to resolve the found subdomains:

`amass enum -active -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80,443,8080</span>

- Do a brute force search for sub[d]omains:

`amass enum -brute -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>

- Save the results to a text file:

`amass enum -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>

- Save terminal output to a file and other detailed output to a directory:

`amass enum -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>` -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>

- List all available data sources:

`amass enum -list`
