---
layout: page
title: freebsd/cal (हिन्दी)
description: "वर्तमान दिन को हाइलाइट करते हुए एक कैलेंडर दिखाएँ।"
content_hash: e5fe7dfac61cfc16bf92cb3662bb17705942d541
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/freebsd/cal.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/freebsd/cal.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/cal.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/cal.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/freebsd/cal.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/freebsd/cal.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cal

वर्तमान दिन को हाइलाइट करते हुए एक कैलेंडर दिखाएँ।
अधिक जानकारी: <https://man.freebsd.org/cgi/man.cgi?cal>।

- वर्तमान महीने का कैलेंडर दिखाएँ:

`cal`

- एक विशेष वर्ष का कैलेंडर दिखाएँ:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">साल</span>

- एक विशेष महीने और वर्ष का कैलेंडर दिखाएँ:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">महीना</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">साल</span>

- वर्तमान वर्ष का पूरा कैलेंडर दिखाएँ:

`cal -y`

- आज को [h]हाइलाइट न करें और [3] महीनों को दिखाएँ जो तारीख को कवर करते हैं:

`cal -h -3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">महीना</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">साल</span>

- वर्तमान वर्ष के एक विशेष [m]हीने के लिए [B]पहले 2 महीने और [A]बाद में 3 महीने दिखाएँ:

`cal -A 3 -B 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">महीना</span>

- [j]जूलियन दिन दिखाएँ (एक से शुरू होकर, 1 जनवरी से नंबरित):

`cal -j`
