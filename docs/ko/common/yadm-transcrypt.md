---
layout: page
title: common/yadm-transcrypt (한국어)
description: "`transcrypt`가 설치된 경우, 이 명령을 통해 `transcrypt`에 직접 옵션을 전달할 수 있습니다."
content_hash: 9c378eb60824a218ccd86630d2a621e76335fe4b
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/yadm-transcrypt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/yadm-transcrypt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># yadm-transcrypt

`transcrypt`가 설치된 경우, 이 명령을 통해 `transcrypt`에 직접 옵션을 전달할 수 있습니다.
yadm 저장소를 사용하도록 환경이 구성되어 있습니다.
Transcrypt는 Git 저장소의 파일에 대해 투명한 암호화 및 복호화를 지원합니다.
더 많은 정보: <https://github.com/elasticdog/transcrypt>.

- 암호화에 사용할 대칭 암호 설정:

`yadm transcrypt --cipher=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호</span>

- 키를 유도할 암호 전달:

`yadm transcrypt --password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호</span>

- 예를 가정하고 지정되지 않은 옵션에 대해 기본값 수락:

`yadm transcrypt --yes`

- 현재 저장소의 암호와 암호 표시:

`yadm transcrypt --display`

- 새로운 자격 증명을 사용하여 모든 암호화된 파일을 다시 암호화:

`yadm transcrypt --rekey`
