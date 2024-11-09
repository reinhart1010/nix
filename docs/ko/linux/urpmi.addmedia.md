---
layout: page
title: linux/urpmi.addmedia (한국어)
description: "Mageia에 미디어 추가."
content_hash: 10f02b8288e93c599156e5d16ed289576873771f
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/urpmi.addmedia.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/urpmi.addmedia.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># urpmi.addmedia

Mageia에 미디어 추가.
참고: Mageia 문서에서는 미디엄과 저장소를 동의어로 사용합니다.
같이 보기: `urpmi`, `urpmi.update`, `urpme`, `urpmi.removemedia`, `urpmf`, `urpmq`.
더 많은 정보: <https://wiki.mageia.org/en/URPMI#urpme>.

- 미디엄 추가:

`sudo urpmi.addmedia `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">미디엄</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp://ftp.site.com/path/to/Mageia/RPMS</span>

- 하드 드라이브에서 미디엄 추가 (먼저 해당 디렉터리에서 `genhdlist2` 실행):

`sudo urpmi.addmedia --distrib HD file:/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/저장소</span>

- 선택한 미러에서 중요한 미디어 추가:

`sudo urpmi.addmedia --distrib ftp://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">미러_웹사이트</span>`/mirror/mageia/distrib/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아키텍처</span>

- 미러 목록에서 자동으로 미러 선택:

`sudo urpmi.addmedia --distrib --mirrorlist `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">미러리스트</span>
