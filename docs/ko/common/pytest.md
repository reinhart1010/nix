---
layout: page
title: common/pytest (한국어)
description: "Python 테스트 실행."
content_hash: 89463377469fe9e093e737e5ca5c9a9ff0a6c8f6
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pytest.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pytest.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pytest

Python 테스트 실행.
더 많은 정보: <https://docs.pytest.org/>.

- 특정 파일에서 테스트 실행:

`pytest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/테스트_파일1.py 경로/대상/테스트_파일2.py ...</span>

- 특정 [k]eyword 표현식과 일치하는 테스트 실행:

`pytest -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">표현식</span>

- 테스트가 실패하거나 오류가 발생하면 즉시 종료:

`pytest --exitfirst`

- 마커와 일치하거나 제외하는 테스트 실행:

`pytest -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마커_이름1 and not 마커_이름2</span>

- 마지막 실패 테스트부터 계속해서 테스트 실패까지 실행:

`pytest --stepwise`

- 출력을 캡처하지 않고 테스트 실행:

`pytest --capture=no`
