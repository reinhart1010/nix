---
layout: page
title: common/id3tag (English)
description: "Read, write, and manipulate ID3v1 and ID3v2 tags of MP3 files."
content_hash: edc03e5fa7eed19c9a321e59ce8c2f5bfe85035d
last_modified_at: 2024-10-13
related_topics:
  - title: italiano version
    url: /it/common/id3tag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# id3tag

Read, write, and manipulate ID3v1 and ID3v2 tags of MP3 files.
More information: <https://manned.org/id3tag>.

- Set artist and song title tag of an MP3 file:

`id3tag --artist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">artist</span>` --song `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">song_title</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mp3</span>

- Set album title of all MP3 files in the current directory:

`id3tag --album `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">album</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.mp3</span>

- Display help:

`id3tag --help`
