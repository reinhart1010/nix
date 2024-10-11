---
layout: page
title: common/delta (한국어)
description: "Git 및 diff 출력 전용 뷰어."
content_hash: 48f1ab0fa4213277600df81f17f0af12a6a85e9f
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/delta.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/delta.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># delta

Git 및 diff 출력 전용 뷰어.
더 많은 정보: <https://github.com/dandavison/delta>.

- 파일 또는 디렉터리 비교:

`delta `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/오래된_파일_또는_디렉터리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운_파일_또는_디렉터리</span>

- 줄 번호를 표시하여 파일이나 디렉터리를 비교:

`delta --line-numbers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/오래된_파일_또는_디렉터리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운_파일_또는_디렉터리</span>

- 파일이나 디렉터리를 비교하여 차이점을 나란히 표시:

`delta --side-by-side `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/오래된_파일_또는_디렉터리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운_파일_또는_디렉터리</span>

- Git 구성 설정을 무시하고 파일이나 디렉터리를 비교:

`delta --no-gitconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/오래된_파일_또는_디렉터리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운_파일_또는_디렉터리</span>

- 터미널 에뮬레이터의 하이퍼링크 사양에 따라 커밋 해시, 파일 이름 및 줄 번호를 하이퍼링크로 비교하고 렌더링:

`delta --hyperlinks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/오래된_파일_또는_디렉터리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/새로운_파일_또는_디렉터리</span>

- 현재 설정을 표시:

`delta --show-config`

- 지원되는 언어 및 관련 파일 확장자를 표시:

`delta --list-languages`
