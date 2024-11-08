---
layout: page
title: linux/createrepo (한국어)
description: "디렉터리에 RPM 저장소를 초기화하고 모든 XML 및 SQLite 파일을 포함합니다."
content_hash: ace985ddee01f1d74fa4334f055a0851b52e1b99
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/createrepo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/createrepo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># createrepo

디렉터리에 RPM 저장소를 초기화하고 모든 XML 및 SQLite 파일을 포함합니다.
더 많은 정보: <https://manned.org/createrepo>.

- 기본 저장소를 디렉터리에서 초기화:

`createrepo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 저장소를 초기화하고, 테스트 RPM을 제외하고, 자세한 로그를 표시:

`createrepo -v -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">test_*.rpm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- SHA1을 체크섬 알고리즘으로 사용하고, 심볼릭 링크를 무시하여 저장소를 초기화:

`createrepo -S -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sha1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
