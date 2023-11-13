---
layout: page
title: linux/toolbox-create (தமிழ்)
description: "புதிய `toolbox` கொள்கலனை உருவாக்கவும்."
content_hash: d65ca04d7bbd5b8b557bc1870ce771e7462bcd8b
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/linux/toolbox-create.html
    icon: bi bi-globe
tldri18n_status: 2
---
# toolbox create

புதிய `toolbox` கொள்கலனை உருவாக்கவும்.
மேலும் விவரத்திற்கு: <https://manned.org/toolbox-create.1>.

- ஒரு குறிப்பிட்ட விநியோகத்திற்காக `toolbox` கொள்கலனை உருவாக்கவும்:

`toolbox create --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">விநியோகம்</span>

- தற்போதைய விநியோகத்தின் குறிப்பிட்ட வெளியீட்டிற்கு `toolbox` கொள்கலனை உருவாக்கவும்:

`toolbox create --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">வெளியீடு</span>

- தனிப்பயன் படத்துடன் `toolbox` கொள்கலனை உருவாக்கவும்:

`toolbox create --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பெயர்</span>

- தனிப்பயன் ஃபெடோரா படத்திலிருந்து `toolbox` கொள்கலனை உருவாக்கவும்:

`toolbox create --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry.fedoraproject.org/fedora-toolbox:39</span>

- ஃபெடோரா 39க்கான இயல்புநிலை படத்தைப் பயன்படுத்தி `toolbox` கொள்கலனை உருவாக்கவும்:

`toolbox create --distro `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora</span>` --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f39</span>
