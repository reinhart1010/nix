---
layout: page
title: common/amass-db (English)
description: "Interact with an Amass database."
content_hash: d892fd10fb57a5ce583a066a42495fe685fa59c9
---
# amass db

Interact with an Amass database.
More information: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-db-subcommand>.

- List all performed enumerations in the database:

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_directory</span>` -list`

- Show results for a specified enumeration index and domain name:

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_directory</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>` -enum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index_from_list</span>` -show`

- List all found subdomains of a domain within an enumeration:

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_directory</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>` -enum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index_from_list</span>` -names`

- Show a summary of the found subdomains within an enumeration:

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_directory</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>` -enum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index_from_list</span>` -summary`
