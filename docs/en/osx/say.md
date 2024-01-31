---
layout: page
title: osx/say (English)
description: "Converts text to speech."
content_hash: 1cc8c30391c855a7ba222596288e50d70bd4c6af
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/say.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/say.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/say.html
    icon: bi bi-globe
tldri18n_status: 2
---
# say

Converts text to speech.
More information: <https://keith.github.io/xcode-man-pages/say.1.html>.

- Say a phrase aloud:

`say "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">I like to ride my bike.</span>`"`

- Read a file aloud:

`say --input-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.txt</span>

- Say a phrase with a custom voice and speech rate:

`say --voice=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voice</span>` --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">words_per_minute</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">I'm sorry Dave, I can't let you do that.</span>`"`

- List the available voices (different voices speak in different languages):

`say --voice="?"`

- Say something in Polish:

`say --voice=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Zosia</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Litwo, ojczyzno moja!</span>`"`

- Create an audio file of the spoken text:

`say --output-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.aiff</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Here's to the Crazy Ones.</span>`"`
