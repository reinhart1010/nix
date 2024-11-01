---
layout: page
title: common/zapier-init (한국어)
description: "새 Zapier 통합을 초기화."
content_hash: d6d718c4ea274056e369c50ff39ada99f63da90b
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zapier-init.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zapier-init.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zapier init

새 Zapier 통합을 초기화.
더 많은 정보: <https://platform.zapier.com/reference/cli#init>.

- 새 Zapier 통합 초기화:

`zapier init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 특정 템플릿으로 새 Zapier 통합 초기화:

`zapier init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--template</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">basic-auth|callback|custom-auth|digest-auth|dynamic-dropdown|files|minimal|oauth1-trello|oauth2|search-or-create|session-auth|typescript</span>

- 추가 디버깅 출력 표시:

`zapier init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>
