---
layout: page
title: linux/gpasswd (English)
description: "Administer `/etc/group` and `/etc/gshadow`."
content_hash: 6af4d558cb8b68fb2246ba1fcdfdbd778bc8eea7
last_modified_at: 2023-11-12
related_topics:
  - title: العربية version
    url: /ar/linux/gpasswd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gpasswd

Administer `/etc/group` and `/etc/gshadow`.
More information: <https://manned.org/gpasswd>.

- Define group administrators:

`sudo gpasswd -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user1,user2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>

- Set the list of group members:

`sudo gpasswd -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user1,user2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>

- Create a password for the named group:

`gpasswd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>

- Add a user to the named group:

`gpasswd -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>

- Remove a user from the named group:

`gpasswd -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group</span>
