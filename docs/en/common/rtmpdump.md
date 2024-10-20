---
layout: page
title: common/rtmpdump (English)
description: "Dump media content streamed over the RTMP protocol."
content_hash: 9c23e78fa36cec6ee568e65aecdc735d46073e9f
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# rtmpdump

Dump media content streamed over the RTMP protocol.
More information: <https://rtmpdump.mplayerhq.hu/>.

- Download a file:

`rtmpdump --rtmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rtmp://example.com/path/to/video</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>

- Download a file from a Flash player:

`rtmpdump --rtmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rtmp://example.com/path/to/video</span>` --swfVfy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/player</span>` --flashVer "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LNX 10,0,32,18</span>`" -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>

- Specify connection parameters if they are not detected correctly:

`rtmpdump --rtmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rtmp://example.com/path/to/video</span>` --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app_name</span>` --playpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/video</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>

- Download a file from a server that requires a referrer:

`rtmpdump --rtmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rtmp://example.com/path/to/video</span>` --pageUrl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/webpage</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.ext</span>
