---
layout: page
title: common/locust (한국어)
description: "시스템이 처리할 수 있는 동시 사용자 수를 결정하는 부하 테스트 도구."
content_hash: 13fd2fca60399af9d6340e8d9263575a2b6fd067
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/locust.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/locust.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># locust

시스템이 처리할 수 있는 동시 사용자 수를 결정하는 부하 테스트 도구.
더 많은 정보: <https://locust.io>.

- locustfile.py를 사용하여 "example.com"에 웹 인터페이스로 부하 테스트:

`locust --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- 다른 테스트 파일 사용:

`locust --locustfile=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테스트_파일.py</span>` --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- 웹 인터페이스 없이 테스트 실행, 1초에 1명의 사용자를 추가하여 100명의 사용자가 될 때까지:

`locust --no-web --clients=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` --hatch-rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- Locust를 마스터 모드로 시작:

`locust --master --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- Locust 슬레이브를 마스터에 연결:

`locust --slave --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- 다른 기기에 있는 마스터에 Locust 슬레이브 연결:

`locust --slave --master-host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마스터_호스트명</span>` --host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>
