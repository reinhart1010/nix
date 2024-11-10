---
layout: page
title: common/stdbuf (हिन्दी)
description: "एक कमांड को उसके मानक स्ट्रीम के लिए संशोधित बफरिंग ऑपरेशनों के साथ चलाएं।"
content_hash: 2f7413f2e97eefb84a561051fc2673c07c8cec23
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/stdbuf.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/stdbuf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/stdbuf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stdbuf

एक कमांड को उसके मानक स्ट्रीम के लिए संशोधित बफरिंग ऑपरेशनों के साथ चलाएं।
अधिक जानकारी: <https://www.gnu.org/software/coreutils/stdbuf>।

- `stdin` बफर का आकार 512 KiB में बदलें:

`stdbuf --input=512K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>

- `stdout` बफर को लाइन-बफर्ड में बदलें:

`stdbuf --output=L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>

- `stderr` बफर को अनबफर्ड में बदलें:

`stdbuf --error=0 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">आदेश</span>
