---
layout: page
title: common/knotc (한국어)
description: "Knot DNS 서버 제어."
content_hash: a42e3c862da8d62135e7331fb1aa5749d1b2f368
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/knotc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/knotc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/knotc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># knotc

Knot DNS 서버 제어.
더 많은 정보: <https://www.knot-dns.cz/docs/latest/html/man_knotc.html>.

- zone 편집 시작:

`knotc zone-begin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zone</span>

- TTL이 3600인 A 레코드 설정:

`knotc zone-set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zone</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서브도메인</span>` 3600 A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_주소</span>

- zone 편집 완료:

`knotc zone-commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zone</span>

- 현재 zone 데이터 얻기:

`knotc zone-read `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zone</span>

- 현재 서버 구성 가져오기:

`knotc conf-read server`
