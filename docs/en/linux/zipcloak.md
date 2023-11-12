---
layout: page
title: linux/zipcloak (English)
description: "Encrypt the contents within a zipfile."
content_hash: 3217131f46925c9257463b197a5decc823ca308d
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/linux/zipcloak.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zipcloak

Encrypt the contents within a zipfile.
More information: <https://manned.org/zipcloak>.

- Encrypt the contents of a zipfile:

`zipcloak `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.zip</span>

- [d]ecrypt the contents of a zipfile:

`zipcloak -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.zip</span>

- [O]utput the encrypted contents into a new zipfile:

`zipcloak `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.zip</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/encrypted.zip</span>
