---
layout: page
title: common/flac (English)
description: "Encodes, decodes and tests FLAC files."
content_hash: 2444aec7d287f81dc968683cc9dbb70955c50b42
related_topics:
  - title: italiano version
    url: /it/common/flac.html
    icon: bi bi-globe
---
# flac

Encodes, decodes and tests FLAC files.
More information: <https://xiph.org/flac>.

- Encode a WAV file to FLAC (this will create a FLAC file in the same location as the WAV file):

`flac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>

- Encode a WAV file to FLAC, specifying the output file:

`flac -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.flac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>

- Decode a FLAC file to WAV, specifying the output file:

`flac -d -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.wav</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.flac</span>

- Test a FLAC file for the correct encoding:

`flac -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.flac</span>
