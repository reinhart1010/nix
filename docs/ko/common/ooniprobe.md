---
layout: page
title: common/ooniprobe (한국어)
description: "네트워크 간섭의 열린 관측소 (OONI)."
content_hash: 0ffded346f10162c357b755547b6dfcc86af8e88
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/ooniprobe.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ooniprobe.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ooniprobe

네트워크 간섭의 열린 관측소 (OONI).
웹사이트 및 앱 차단 여부를 테스트하세요. 네트워크의 속도 및 성능을 측정하세요.
더 많은 정보: <https://ooni.org/support/ooni-probe-cli/>.

- 수행된 모든 테스트 나열:

`ooniprobe list`

- 특정 테스트에 대한 정보 표시:

`ooniprobe list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>

- 사용 가능한 모든 테스트 실행:

`ooniprobe run all`

- 특정 테스트 수행:

`ooniprobe run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">performance</span>

- 특정 웹사이트의 가용성 확인:

`ooniprobe run websites --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://ooni.org/</span>

- 파일에 나열된 모든 웹사이트의 가용성 확인:

`ooniprobe run websites --input-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/my-websites.txt</span>

- JSON 형식으로 테스트에 대한 자세한 정보 표시:

`ooniprobe show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9</span>
