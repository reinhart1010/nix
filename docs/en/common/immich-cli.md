---
layout: page
title: common/immich-cli (English)
description: "Immich has a command line interface (CLI) that allows you to perform certain actions from the command line."
content_hash: 3de64a1bd867879444c21644780dbbc8eba956b7
last_modified_at: 2024-05-07
related_topics:
  - title: español version
    url: /es/common/immich-cli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# immich-cli

Immich has a command line interface (CLI) that allows you to perform certain actions from the command line.
See also: `immich-go`.
More information: <https://immich.app/docs/features/command-line-interface/>.

- Authenticate to Immich server:

`immich login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_url/api</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server_key</span>

- Upload some image files:

`immich upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1.jpg file2.jpg</span>

- Upload a directory including subdirectories:

`immich upload --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Create an album based on a directory:

`immich upload --album-name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">My summer holiday</span>`" --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Skip assets matching a glob pattern:

`immich upload --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">**/Raw/** **/*.tif</span>` --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Include hidden files:

`immich upload --include-hidden --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
