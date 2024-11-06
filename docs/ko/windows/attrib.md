---
layout: page
title: windows/attrib (한국어)
description: "파일 또는 디렉터리의 속성을 표시하거나 변경."
content_hash: 7496630e2cb7d3a920b268cde6e8606d42224853
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/attrib.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/attrib.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/attrib.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/attrib.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/attrib.html
    icon: bi bi-globe
tldri18n_status: 2
---
# attrib

파일 또는 디렉터리의 속성을 표시하거나 변경.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/attrib>.

- 현재 디렉터리의 파일에 설정된 모든 속성 표시:

`attrib`

- 특정 디렉터리의 파일에 설정된 모든 속성 표시:

`attrib `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉터리</span>

- 현재 디렉터리의 파일과 [d]디렉터리에 설정된 모든 속성 표시:

`attrib /d`

- 현재 디렉터리와 [s]하위 디렉터리의 파일에 설정된 모든 속성 표시:

`attrib /s`

- 파일 또는 디렉터리에 `[r]읽기 전용`, `[a]보관`, `[s]시스템`, `[h]숨김`, `콘텐츠 [i]인덱싱 안 함` 속성 추가:

`attrib +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">r|a|s|h|i</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일_또는_디렉터리1 경로\대상\파일_또는_디렉터리2 ...</span>

- 파일 또는 디렉터리의 특정 속성 제거:

`attrib -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">r|a|s|h|i</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일_또는_디렉터리1 경로\대상\파일_또는_디렉터리2 ...</span>
