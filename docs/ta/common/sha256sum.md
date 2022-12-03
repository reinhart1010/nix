---
layout: page
title: common/sha256sum (தமிழ்)
description: "SHA256 மறையீட்டு சரிகாண்தொகையைக் கணி."
content_hash: d32f88a381c5a5a6a4f047552d256b8ae1bb54aa
last_modified_at: 2022-12-03
related_topics:
  - title: English version
    url: /en/common/sha256sum.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/sha256sum.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sha256sum.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sha256sum

SHA256 மறையீட்டு சரிகாண்தொகையைக் கணி.
மேலும் விவரத்திற்கு: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- கோப்பின் SHA256 சரிகாண்தொகையைக் கணி:

`sha256sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு</span>

- பலக் கோப்புகளின் SHA256 சரிகாண்தொகையைக் கணி:

`sha256sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு2</span>

- SHA256 சரிகாண்தொகைகளைக் கணித்து கோப்பில் எழுது:

`sha256sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.sha256</span>

- SHA256 சரிகாண்தொகைகளுடைய கோப்பைப் படித்து கோப்புகளைச் சரிபார்:

`sha256sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.sha256</span>

- பிழையுற்ற கோப்புகளை மட்டும் காட்டு:

`sha256sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.sha256</span>

- விடுபட்ட கோப்புகளைப் புறக்கணித்து, சரிபார்ப்பு தோல்வியுற்ற கோப்புகளுக்கான செய்தியை மட்டும் காட்டவும்:

`sha256sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">பாதை/டு/கோப்பு.sha256</span>
