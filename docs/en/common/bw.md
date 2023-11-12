---
layout: page
title: common/bw (English)
description: "Access and manage a Bitwarden vault."
content_hash: dcf7f4bf7c409831943d1e3e9bd75d1a8c9631d6
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/bw.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bw.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bw

Access and manage a Bitwarden vault.
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
