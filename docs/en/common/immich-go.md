---
layout: page
title: common/immich-go (English)
description: "Immich-Go is an open-source tool designed to streamline uploading large photo collections to your self-hosted Immich server."
content_hash: 788d9445e60e390129621d8aabca99f7b899d01f
last_modified_at: 2024-05-06
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/immich-go.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># immich-go

Immich-Go is an open-source tool designed to streamline uploading large photo collections to your self-hosted Immich server.
See also: `immich-cli`.
More information: <https://github.com/simulot/immich-go>.

- Upload a Google Photos takeout file to Immich server:

`immich-go -server=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_url</span>` -key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_key</span>` upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/takeout_file.zip</span>

- Import photos captured on June 2019, while auto-generating albums:

`immich-go -server=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_url</span>` -key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_key</span>` upload -create-albums -google-photos -date=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2019-06</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/takeout_file.zip</span>

- Upload a takeout file using server and key from a config file:

`immich-go -use-configuration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">~/.immich-go/immich-go.json</span>` upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/takeout_file.zip</span>

- Examine Immich server content, remove less quality images, and preserve albums:

`immich-go -server=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_url</span>` -key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_key</span>` duplicate -yes`

- Delete all albums created with the pattern "YYYY-MM-DD":

`immich-go -server=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_url</span>` -key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_key</span>` tool album delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\d{4}-\d{2}-\d{2}</span>
