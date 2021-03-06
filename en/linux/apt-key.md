---
layout: page
title: linux/apt-key (English)
description: "Key management utility for the APT Package Manager on Debian and Ubuntu."
content_hash: 03b2ed2e6a14084a715aef2cdb417c0c59275894
related_topics:
  - title: Deutsch version
    url: /de/linux/apt-key.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-key.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-key.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-key.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-key.html
    icon: bi bi-globe
---
# apt-key

Key management utility for the APT Package Manager on Debian and Ubuntu.
Note: `apt-key` is now deprecated (except for the use of `apt-key del` in maintainer scripts).
More information: <https://manpages.debian.org/latest/apt/apt-key.8.html>.

- List trusted keys:

`apt-key list`

- Add a key to the trusted keystore:

`apt-key add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public_key_file.asc</span>

- Delete a key from the trusted keystore:

`apt-key del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_id</span>

- Add a remote key to the trusted keystore:

`wget -qO - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://host.tld/filename.key</span>` | apt-key add -`

- Add a key from keyserver with only key id:

`apt-key adv --keyserver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pgp.mit.edu</span>` --recv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">KEYID</span>
