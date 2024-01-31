---
layout: page
title: common/mediainfo (English)
description: "Display metadata from video and audio files."
content_hash: e80f7b72a4234f14f9357431fe98590a3ce3cbc6
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# mediainfo

Display metadata from video and audio files.
More information: <https://mediaarea.net/MediaInfo>.

- Display metadata for a given file in the console:

`mediainfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Store the output to a given file along with displaying in the console:

`mediainfo --Logfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">out.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- List metadata attributes that can be extracted:

`mediainfo --Info-Parameters`
