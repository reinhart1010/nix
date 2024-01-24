---
layout: page
title: common/mid3v2 (English)
description: "Edit audio tags."
content_hash: 56041e580aaf88eca92d753d75621f262aa5ce04
last_modified_at: 2024-01-24
related_topics:
  - title: español version
    url: /es/common/mid3v2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mid3v2

Edit audio tags.
See also: `id3v2`.
More information: <https://mutagen.readthedocs.io/en/latest/man/mid3v2.html>.

- List all supported ID3v2.3 or ID3v2.4 frames and their meanings:

`id3v2 --list-frames `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.mp3 path/to/file2.mp3 ...</span>

- List all supported ID3v1 numeric genres:

`id3v2 --list-genres `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.mp3 path/to/file2.mp3 ...</span>

- List all tags in specific files:

`id3v2 --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.mp3 path/to/file2.mp3 ...</span>

- Set specific artist, album, or song information:

`id3v2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--artist|--album|--song</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.mp3 path/to/file2.mp3 ...</span>

- Set specific picture information:

`id3v2 --picture=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename:description:image_type:mime_type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.mp3 path/to/file2.mp3 ...</span>

- Set specific year information:

`id3v2 --year=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.mp3 path/to/file2.mp3 ...</span>

- Set specific date information:

`id3v2 --date=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.mp3 path/to/file2.mp3 ...</span>
