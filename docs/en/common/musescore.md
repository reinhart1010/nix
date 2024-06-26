---
layout: page
title: common/musescore (English)
description: "MuseScore 3 sheet music editor."
content_hash: 73e5e6771b8a680467b2daedafbacdf54f1695bd
last_modified_at: 2024-04-04
related_topics:
  - title: Deutsch version
    url: /de/common/musescore.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/musescore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# musescore

MuseScore 3 sheet music editor.
See also: `lilypond`.
More information: <https://musescore.org/en/handbook/3/command-line-options>.

- Use a specific audio driver:

`musescore --audio-driver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jack|alsa|portaudio|pulse</span>

- Set the MP3 output bitrate in kbit/s:

`musescore --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bitrate</span>

- Start MuseScore in debug mode:

`musescore --debug`

- Enable experimental features, such as layers:

`musescore --experimental`

- Export the given file to the specified output file. The file type depends on the given extension:

`musescore --export-to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>

- Print a diff between the given scores:

`musescore --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>

- Specify a MIDI import operations file:

`musescore --midi-operations `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
