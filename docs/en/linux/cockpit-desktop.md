---
layout: page
title: linux/cockpit-desktop (English)
description: "Securely access Cockpit pages in a running session."
content_hash: 9547aad4443c5335647d4b7453a5d9d19230bafa
last_modified_at: 2024-04-26
tldri18n_status: 2
---
# cockpit-desktop

Securely access Cockpit pages in a running session.
It starts `cockpit-ws` and a web browser in an isolated network space and a `cockpit-bridge` in a running user session.
More information: <https://cockpit-project.org/guide/latest/cockpit-desktop.1.html>.

- Open a page:

`cockpit-desktop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SSH_host</span>

- Open storage page:

`cockpit-desktop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/cockpit/@localhost/storage/index.html</span>
