---
layout: page
title: common/shasum (தமிழ்)
description: "SHA மறையீட்டு சரிகாண்தொகைகளைக் கணி அல்லது சரிபார்."
content_hash: 2f526f5e0035b9f50319907a5913ff0476a58fb0
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/shasum.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/shasum.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># shasum

SHA மறையீட்டு சரிகாண்தொகைகளைக் கணி அல்லது சரிபார்.
மேலும் விவரத்திற்கு: <https://manned.org/shasum>.

- கோப்பின் SHA1 சரிகாண்தொகையைக் கணி:

`shasum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு</span>

- கோப்பின் SHA256 சரிகாண்தொகையைக் கணி:

`shasum --algorithm 256 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு</span>

- பலக் கோப்புகளின் SHA512 சரிகாண்தொகைகளைக் கணி:

`shasum --algorithm 512 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு2</span>

- SHA256 சரிகாண்தொகைகளைக் கணித்துக் கோப்பில் எழுது:

`shasum --algorithm 256 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு.sha256</span>

- சரிகாண்தொகைகளுடைய கோப்பைப் படித்து கோப்புகளைச் சரிபார்:

`shasum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு</span>

- சரிகாண்தொகைகளைச் சரிபார்த்துப் பிழையுற்ற கோப்புகளை மட்டும் காட்டு:

`shasum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கோப்பு</span>

- இயல் உள்ளீட்டின் SHA1 சரிகாண்தொகையைக் கணி:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">கட்டளை</span>` | shasum`
