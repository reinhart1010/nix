---
layout: page
title: linux/beep (English)
description: "A utility to beep the PC speaker."
content_hash: 106fca5ec06d245b1a59e3bc6c70e08b40d39dff
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/beep.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/beep.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/beep.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/beep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# beep

A utility to beep the PC speaker.
More information: <https://github.com/spkr-beep/beep>.

- Play a beep:

`beep`

- Play a beep that repeats:

`beep -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repetitions</span>

- Play a beep at a specified frequency (Hz) and duration (milliseconds):

`beep -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">frequency</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">duration</span>

- Play each new frequency and duration as a distinct beep:

`beep -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">frequency</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">duration</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">frequency</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">duration</span>

- Play the C major scale:

`beep -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">262</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">294</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">330</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">349</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">392</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">440</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">494</span>` -n -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">523</span>
