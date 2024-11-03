---
layout: page
title: openbsd/pkg_delete (हिन्दी)
description: "OpenBSD में पैकेज हटाएँ।"
content_hash: 74b0ba3a51ff191ad433b6b90889e99c5192072a
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/openbsd/pkg_delete.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/openbsd/pkg_delete.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/openbsd/pkg_delete.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/openbsd/pkg_delete.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/openbsd/pkg_delete.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pkg_delete

OpenBSD में पैकेज हटाएँ।
देखें: `pkg_add`, `pkg_info`।
अधिक जानकारी: <https://man.openbsd.org/pkg_delete>।

- एक पैकेज हटाएँ:

`pkg_delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- एक पैकेज हटाएँ, इसके अप्रयुक्त निर्भरताओं सहित:

`pkg_delete -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>

- एक पैकेज का ड्राई-रन हटाना:

`pkg_delete -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">पैकेज</span>
