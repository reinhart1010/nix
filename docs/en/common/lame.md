---
layout: page
title: common/lame (English)
description: "Encode WAV to MP3 files."
content_hash: 69013e95899b094ed079bf429611b03a81dc941b
last_modified_at: 2025-03-02
tldri18n_status: 2
---
# lame

Encode WAV to MP3 files.
More information: <https://svn.code.sf.net/p/lame/svn/trunk/lame/USAGE>.

- Encode an audio file to MP3 using CBR 320 kbit/second:

`lame -b 320 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.wav `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>`.mp3`

- Encode an audio file to MP3 using the V0 preset:

`lame -V 0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.wav `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>`.mp3`

- Encode an audio file to AAC:

`lame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`.wav `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>`.aac`
