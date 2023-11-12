---
layout: page
title: common/mediainfo (English)
description: "Display metadata from video and audio files."
content_hash: ceac1e36b7abefcc9c77a39df2efc0f7df370f84
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mediainfo

Display metadata from video and audio files.
More information: <https://mediaarea.net/MediaInfo>.

- Display metadata for a given file in the console:

`mediainfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Store the output to a given file along with displaying in the console:

`mediainfo --Logfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">out.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Display the list of metadata attributes that can be extracted:

`mediainfo --Info-Parameters`
