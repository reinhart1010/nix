---
layout: page
title: linux/dpkg-deb (English)
description: "Pack, unpack and provide information about Debian archives."
content_hash: 2f8b81c170fb1625c00b69028b96d7448eae0739
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/linux/dpkg-deb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dpkg-deb

Pack, unpack and provide information about Debian archives.
More information: <https://manpages.debian.org/latest/dpkg/dpkg-deb.html>.

- Display information about a package:

`dpkg-deb --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.deb</span>

- Display the package's name and version on one line:

`dpkg-deb --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.deb</span>

- List the package's contents:

`dpkg-deb --contents `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.deb</span>

- Extract package's contents into a directory:

`dpkg-deb --extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.deb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Create a package from a specified directory:

`dpkg-deb --build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
