---
layout: page
title: linux/eyed3 (English)
description: "Read and manipulate metadata of MP3 files."
content_hash: 786fde2b27b3508a971b50056854b6fcc91609d8
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/eyed3.html
    icon: bi bi-globe
tldri18n_status: 2
---
# eyeD3

Read and manipulate metadata of MP3 files.
More information: <https://eyed3.readthedocs.io>.

- View information about an MP3 file:

`eyeD3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.mp3</span>

- Set the title of an MP3 file:

`eyeD3 --title "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A Title</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.mp3</span>

- Set the album of all the MP3 files in a directory:

`eyeD3 --album "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Album Name</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.mp3</span>

- Set the front cover art for an MP3 file:

`eyeD3 --add-image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">front_cover.jpeg</span>`:FRONT_COVER: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.mp3</span>
