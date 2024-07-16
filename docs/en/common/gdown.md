---
layout: page
title: common/gdown (English)
description: "Download files from Google Drive and other URLs."
content_hash: f5753f16279b6cb41f11d4cdcc97502e0a217b10
last_modified_at: 2024-07-16
tldri18n_status: 2
---
# gdown

Download files from Google Drive and other URLs.
More information: <https://github.com/wkentaro/gdown>.

- Download a file from a URL:

`gdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Download using a file ID:

`gdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_id</span>

- Download with fuzzy file ID extraction (also works with <https://docs.google.com> links):

`gdown --fuzzy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Download a folder using its ID or the full URL:

`gdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">folder_id|url</span>` -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_directory</span>` --folder`

- Download a tar archive, write it to `stdout` and extract it:

`gdown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tar_url</span>` -O - --quiet | tar xvf -`
