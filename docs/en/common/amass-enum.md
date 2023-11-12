---
layout: page
title: common/amass-enum (English)
description: "Find subdomains of a domain."
content_hash: 44da1971441e79c80e0d0fb5e70294196e80aa9c
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/amass-enum.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/amass-enum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# amass enum

Find subdomains of a domain.
More information: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- Passively find subdomains of a domain:

`amass enum -passive -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>

- Find subdomains of a domain and actively verify them attempting to resolve the found subdomains:

`amass enum -active -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80,443,8080</span>

- Do a brute force search for subdomains:

`amass enum -brute -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>

- Save the results to a text file:

`amass enum -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>

- Save the results to a database:

`amass enum -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>` -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_directory</span>
