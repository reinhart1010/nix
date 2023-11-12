---
layout: page
title: linux/toolbox-run (தமிழ்)
description: "ஏற்கனவே உள்ள `toolbox` கொள்கலனுக்குள் கட்டளையை இயக்கவும்."
content_hash: 248aac6bd39387c43e585cd0e211c67dd0150cfb
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/toolbox-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# toolbox run

ஏற்கனவே உள்ள `toolbox` கொள்கலனுக்குள் கட்டளையை இயக்கவும்.
மேலும் பார்க்கவும்: `toolbox enter`.
மேலும் விவரத்திற்கு: <https://manned.org/toolbox-run>.

- ஒரு குறிப்பிட்ட `toolbox` கொள்கலனுக்குள் ஒரு கட்டளையை இயக்கவும்:

`toolbox run --container `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கொள்கலன்_பெயர்</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>

- விநியோகத்தின் குறிப்பிட்ட வெளியீட்டிற்கு `toolbox` கொள்கலனுக்குள் கட்டளையை இயக்கவும்:

`toolbox run --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">விநியோகம்</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வெளியீடு</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>

- ஃபெடோரா 38க்கான இயல்புநிலை படத்தைப் பயன்படுத்தி `toolbox` கொள்கலனுக்குள் `emacs` ஐ இயக்கவும்:

`toolbox run --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f38</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">emacs</span>
