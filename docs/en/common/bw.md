---
layout: page
title: common/bw (English)
description: "A CLI to access and manage a Bitwarden vault."
content_hash: b0d218b8e49df4a26a79fef24a98372593c676f6
related_topics:
  - title: italiano version
    url: /it/common/bw.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bw.html
    icon: bi bi-globe
---
# bw

A CLI to access and manage a Bitwarden vault.
More information: <https://help.bitwarden.com/article/cli/>.

- Log in to a Bitwarden user account:

`bw login`

- Log out of a Bitwarden user account:

`bw logout`

- Search and display items from Bitwarden vault:

`bw list items --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github</span>

- Display a particular item from Bitwarden vault:

`bw get item `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">github</span>

- Create a folder in Bitwarden vault:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo -n '{"name":"My Folder1"}' | base64</span>` | bw create folder`
