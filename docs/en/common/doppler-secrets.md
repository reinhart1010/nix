---
layout: page
title: common/doppler-secrets (English)
description: "Manage your Doppler project's secrets."
content_hash: 4398e9d4b69af250732852dcd560f0ff15bbd76a
last_modified_at: 2024-08-03
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/doppler-secrets.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># doppler secrets

Manage your Doppler project's secrets.
More information: <https://docs.doppler.com/docs/accessing-secrets>.

- Get all secrets:

`doppler secrets`

- Get value(s) of one or more secrets:

`doppler secrets get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secrets</span>

- Upload a secrets file:

`doppler secrets upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.env</span>

- Delete value(s) of one or more secrets:

`doppler secrets delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secrets</span>

- Download secrets as `.env`:

`doppler secrets download --format=env --no-file > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/.env</span>
