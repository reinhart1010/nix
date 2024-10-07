---
layout: page
title: common/redshift (English)
description: "Adjust the color temperature of your screen according to your surroundings."
content_hash: 69d49edafbf8bc5c962468fcbba7b166ab75b95b
last_modified_at: 2024-10-07
tldri18n_status: 2
---
# redshift

Adjust the color temperature of your screen according to your surroundings.
More information: <http://jonls.dk/redshift>.

- Turn on Redshift with a specific [t]emperature during day (e.g., 5700K) and at night (e.g., 3600K):

`redshift -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5700</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- Turn on Redshift with a manually specified custom [l]ocation:

`redshift -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">latitude</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">longitude</span>

- Turn on Redshift with a specific screen [b]rightness during the day (e.g, 70%) and at night (e.g., 40%):

`redshift -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.7</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.4</span>

- Turn on Redshift with custom [g]amma levels (between 0 and 1):

`redshift -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">red</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">green</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blue</span>

- [P]urge existing temperature changes and set a constant unchanging color temperature in [O]ne-shot mode:

`redshift -PO `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">temperature</span>
