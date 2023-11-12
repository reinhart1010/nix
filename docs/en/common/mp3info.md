---
layout: page
title: common/mp3info (English)
description: "Viewer/editor for ID3v1 (but not ID3v2) tags of MP3 files."
content_hash: 59dafae3167354d05a0867ebcb867d657877034e
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mp3info

Viewer/editor for ID3v1 (but not ID3v2) tags of MP3 files.
More information: <http://www.ibiblio.org/mp3info>.

- Show all ID3v1 tags of a specific MP3 file:

`mp3info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mp3</span>

- Edit ID3v1 tags interactively:

`mp3info -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mp3</span>

- Set values for ID3v1 tags in a specific MP3 file:

`mp3info -a "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">artist_name</span>`" -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">song_title</span>`" -l "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">album_title</span>`" -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">year</span>` -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comment_text</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mp3</span>

- Set the number of the track in the album for a specific MP3 file:

`mp3info -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">track_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mp3</span>

- Print a list of valid genres and their numeric codes:

`mp3info -G`

- Set the music genre for a specific MP3 file:

`mp3info -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">genre_number</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mp3</span>
