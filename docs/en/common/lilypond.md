---
layout: page
title: common/lilypond (English)
description: "Typeset music and/or produce MIDI from file."
content_hash: 918313fa0381c01ecb0b67c9f308fcb430f79f73
last_modified_at: 2024-04-04
tldri18n_status: 2
---
# lilypond

Typeset music and/or produce MIDI from file.
See also: `musescore`.
More information: <https://lilypond.org>.

- Compile a lilypond file into a PDF:

`lilypond `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compile into the specified format:

`lilypond --formats=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">format_dump</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compile the specified file, suppressing progress updates:

`lilypond -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Compile the specified file, and also specify the output filename:

`lilypond --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>

- Show the current version of lilypond:

`lilypond --version`
