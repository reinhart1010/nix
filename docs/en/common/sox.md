---
layout: page
title: common/sox (English)
description: "Sound eXchange: play, record and convert audio files."
content_hash: eedb3081399de9cf079b488638bdaa1820949037
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# sox

Sound eXchange: play, record and convert audio files.
Audio formats are identified by the extension.
More information: <http://sox.sourceforge.net>.

- Merge two audio files into one:

`sox -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_audiofile1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_audiofile2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_audiofile</span>

- Trim an audio file to the specified times:

`sox `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_audiofile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_audiofile</span>` trim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">end</span>

- Normalize an audio file (adjust volume to the maximum peak level, without clipping):

`sox --norm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_audiofile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_audiofile</span>

- Reverse and save an audio file:

`sox `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_audiofile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_audiofile</span>` reverse`

- Print statistical data of an audio file:

`sox `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_audiofile</span>` -n stat`

- Increase the volume of an audio file by 2x:

`sox -v 2.0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_audiofile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_audiofile</span>
