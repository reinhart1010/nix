---
layout: page
title: common/gammastep (English)
description: "Adjust the screen's color temperature according to the time of day."
content_hash: 8d1004f3df78c13d593602ba0e9f529b165aa17d
last_modified_at: 2024-02-09
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gammastep.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Gammastep

Adjust the screen's color temperature according to the time of day.
More information: <https://gitlab.com/chinstrap/gammastep>.

- Turn on Gammastep with a specific [t]emperature during the day (e.g. 5700k) and at night (e.g. 3600k):

`gammastep -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5700</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- Turn on Gammastep with a manually specified custom [l]ocation:

`gammastep -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">latitude</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">longitude</span>

- Turn on Gammastep with a specific screen [b]rightness during the day (e.g. 70%) and at night (e.g. 40%), with minimum brightness 10% and maximum brightness 100%:

`gammastep -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.7</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.4</span>

- Turn on Gammastep with custom [g]amma levels (between 0 and 1):

`gammastep -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">green</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue</span>

- Turn on Gammastep with a c[O]nstant unchanging color temperature:

`gammastep -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">temperature</span>

- Reset temperature adjustments applied by Gammastep:

`gammastep -x`
