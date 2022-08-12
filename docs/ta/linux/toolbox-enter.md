---
layout: page
title: linux/toolbox-enter (தமிழ்)
description: "ஊடாடும் பயன்பாட்டிற்கு `toolbox` கொள்கலனை உள்ளிடவும்."
content_hash: 714a9e27f5c24181154762d97cabdb4d66ccd903
related_topics:
  - title: English version
    url: /en/linux/toolbox-enter.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># toolbox enter

ஊடாடும் பயன்பாட்டிற்கு `toolbox` கொள்கலனை உள்ளிடவும்.
மேலும் பார்க்கவும்: `toolbox run`.
மேலும் விவரத்திற்கு: <https://manned.org/toolbox-enter.1>.

- குறிப்பிட்ட விநியோகத்தின் இயல்புப் படத்தைப் பயன்படுத்தி `toolbox` கொள்கலனை உள்ளிடவும்:

`toolbox enter --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">விநியோகம்</span>

- தற்போதைய விநியோகத்தின் குறிப்பிட்ட வெளியீட்டின் இயல்புநிலை படத்தைப் பயன்படுத்தி `toolbox` கொள்கலனை உள்ளிடவும்:

`toolbox enter --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வெளியீடு</span>

- ஃபெடோரா 36 க்கான இயல்புநிலை படத்தைப் பயன்படுத்தி ஒரு கருவிப்பெட்டி கொள்கலனை உள்ளிடவும்:

`toolbox enter --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f36</span>
