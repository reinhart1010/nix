---
layout: page
title: common/liquidctl (한국어)
description: "수냉 쿨러 제어."
content_hash: 85ee8f4b81c2627b9acb0da22cce61c175a08cc2
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/liquidctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/liquidctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># liquidctl

수냉 쿨러 제어.
더 많은 정보: <https://github.com/liquidctl/liquidctl>.

- 사용 가능한 장치 나열:

`liquidctl list`

- 지원되는 모든 장치 초기화:

`sudo liquidctl initialize all`

- 사용 가능한 수냉 쿨러의 상태 출력:

`liquidctl status`

- 제품 이름에서 문자열을 일치시켜 장치를 선택하고 팬 속도를 20°C에서 0%, 50°C에서 50%, 70°C에서 100%로 설정:

`liquidctl --match `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>` set fan speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20 0 50 50 70 100</span>
