---
layout: page
title: common/projucer (한국어)
description: "JUCE 프레임워크 애플리케이션을 위한 프로젝트 관리자."
content_hash: 2250fe3a1b7a743f40ad1a0fccbd319fa5a78276
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/projucer.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/projucer.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Projucer

JUCE 프레임워크 애플리케이션을 위한 프로젝트 관리자.
더 많은 정보: <https://juce.com/discover/stories/projucer-manual#10.4-command-line-tools>.

- 프로젝트에 대한 정보 표시:

`Projucer --status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_파일</span>

- 프로젝트의 모든 파일 및 리소스 다시 저장:

`Projucer --resave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_파일</span>

- 프로젝트의 버전 번호 업데이트:

`Projucer --set-version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_파일</span>

- PIP 파일에서 JUCE 프로젝트 생성:

`Projucer --create-project-from-pip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/PIP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력</span>

- 모든 JUCE 스타일 주석 (`//=====`, `//-----` 또는 `///////`) 제거:

`Projucer --tidy-divider-comments `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_폴더</span>

- 도움말 표시:

`Projucer --help`
