---
layout: page
title: common/amass-db (English)
description: "Interact with an Amass database."
content_hash: 08787f759e8f21d474961793d1c9a1976cfd20d9
last_modified_at: 2024-02-09
related_topics:
  - title: español version
    url: /es/common/amass-db.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/amass-db.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/amass-db.html
    icon: bi bi-globe
tldri18n_status: 2
---
# amass db

Interact with an Amass database.
More information: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-db-subcommand>.

- List all performed enumerations in the database:

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_directory</span>` -list`

- Show results for a specified enumeration index and [d]omain name:

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_directory</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>` -enum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index_from_list</span>` -show`

- List all found subdomains of a [d]omain within an enumeration:

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_directory</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>` -enum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index_from_list</span>` -names`

- Show a summary of the found subdomains within an enumeration:

`amass db -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/database_directory</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>` -enum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index_from_list</span>` -summary`
