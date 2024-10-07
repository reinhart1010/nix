---
layout: page
title: linux/speaker-test (English)
description: "Speaker test tone generator for ALSA."
content_hash: 6038002b31558048ba6a787480741faa7ad43a6b
last_modified_at: 2024-10-07
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/speaker-test.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># speaker-test

Speaker test tone generator for ALSA.
See also: `aplay`, `arecord`, `amixer`.
More information: <https://manned.org/speaker-test>.

- Test the default speakers with pink noise:

`speaker-test`

- Test the default speakers with a sine wave:

`speaker-test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--test</span>` sine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--frequency</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">frequency</span>

- Test the default speakers with a predefined WAV file:

`speaker-test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--test</span>` wav`

- Test the default speakers with a WAV file:

`speaker-test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--test</span>` wav `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-w|--wavfile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
