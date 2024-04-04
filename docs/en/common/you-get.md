---
layout: page
title: common/you-get (English)
description: "Download media contents (videos, audios, images) from the Web."
content_hash: 3bffb4d531c52483dbf3f744a69a135ee029a85b
last_modified_at: 2024-04-04
related_topics:
  - title: فارسی version
    url: /fa/common/you-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# you-get

Download media contents (videos, audios, images) from the Web.
See also: `yt-dlp`, `youtube-viewer`, `instaloader`.
More information: <https://you-get.org>.

- Print media information about a specific media on the web:

`you-get --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/video?id=value</span>

- Download a media from a specific URL:

`you-get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/video?id=value</span>

- Search on Google Videos and download:

`you-get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">keywords</span>

- Download a media to a specific location:

`you-get --output-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --output-filename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/watch?v=value</span>

- Download a media using a proxy:

`you-get --http-proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proxy_server</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/watch?v=value</span>
