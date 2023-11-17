---
layout: page
title: linux/systemd-id128 (English)
description: "Generate and print sd-128 identifiers."
content_hash: 645d194488b88498ebb075248145709cea8dc91a
last_modified_at: 2023-11-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-id128.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-id128

Generate and print sd-128 identifiers.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-id128.html>.

- Generate a new random identifier:

`systemd-id128 new`

- Print the identifier of the current machine:

`systemd-id128 machine-id`

- Print the identifier of the current boot:

`systemd-id128 boot-id`

- Print the identifier of the current service invocation (this is available in systemd services):

`systemd-id128 invocation-id`

- Generate a new random identifier and print it as an UUID (five groups of digits separated by hyphens):

`systemd-id128 new --uuid`
