---
layout: page
title: common/doppler-secrets (English)
description: "Manage your Doppler project's secrets."
content_hash: 4398e9d4b69af250732852dcd560f0ff15bbd76a
last_modified_at: 2024-08-04
tldri18n_status: 2
---
# doppler secrets

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
