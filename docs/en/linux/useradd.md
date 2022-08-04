---
layout: page
title: linux/useradd (English)
description: "Create a new user."
content_hash: ca4959633d81bbbf6b0854bf9014cbe0bd1af989
related_topics:
  - title: español version
    url: /es/linux/useradd.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/useradd.html
    icon: bi bi-globe
---
# useradd

Create a new user.
See also: `users`, `userdel`, `usermod`.
More information: <https://manned.org/useradd>.

- Create a new user:

`sudo useradd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Create a new user with the specified user id:

`sudo useradd --uid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Create a new user with the specified shell:

`sudo useradd --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Create a new user belonging to additional groups (mind the lack of whitespace):

`sudo useradd --groups `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group1,group2,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Create a new user with the default home directory:

`sudo useradd --create-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Create a new user with the home directory filled by template directory files:

`sudo useradd --skel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/template_directory</span>` --create-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Create a new system user without the home directory:

`sudo useradd --system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>
