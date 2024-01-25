---
layout: page
title: common/deemix (English)
description: "A barebone deezer downloader library built from the ashes of Deezloader Remix."
content_hash: 9fcc7e690c49a0150b68a9939cacc51370619750
last_modified_at: 2024-01-25
tldri18n_status: 2
---
# deemix

A barebone deezer downloader library built from the ashes of Deezloader Remix.
It can be used as a standalone CLI app or implemented in a UI using the API.
More information: <https://deemix.app>.

- Download a track or playlist:

`deemix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.deezer.com/us/track/00000000</span>

- Download track/playlist at a specific bitrate:

`deemix --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FLAC|MP3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Download to a specific path:

`deemix --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bitrate</span>` --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Create a portable deemix configuration file in the current directory:

`deemix --portable --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bitrate</span>` --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
