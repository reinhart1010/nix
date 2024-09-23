---
layout: page
title: linux/mt (English)
description: "Control magnetic tape drive operation (commonly LTO tape)."
content_hash: 7c196337a9b92cc300892f3107809596c7f6f7e9
last_modified_at: 2024-09-23
tldri18n_status: 2
---
# mt

Control magnetic tape drive operation (commonly LTO tape).
More information: <https://manned.org/mt>.

- Check the status of a tape drive:

`mt -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/nstX</span>` status`

- Rewind the tape to beginning:

`mt -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/nstX</span>` rewind`

- Move forward a given files, then position the tape on first block of next file:

`mt -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/nstX</span>` fsf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>

- Rewind the tape, then position the tape at beginning of the given file:

`mt -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/nstX</span>` asf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>

- Position the tape at the end of valid data:

`mt -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/nstX</span>` eod`

- Rewind the tape and unload/eject it:

`mt -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/nstX</span>` eject`

- Write EOF (End-of-file) mark at the current position:

`mt -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/nstX</span>` eof`
