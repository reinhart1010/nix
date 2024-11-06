---
layout: page
title: windows/chkdsk (한국어)
description: "파일 시스템 및 볼륨 메타데이터의 오류를 검사."
content_hash: ba2e11a04855f400dc76a3372fdd87eeedf9e946
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/chkdsk.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/chkdsk.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/chkdsk.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/chkdsk.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/chkdsk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chkdsk

파일 시스템 및 볼륨 메타데이터의 오류를 검사.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/chkdsk>.

- 검사할 드라이브 문자(콜론 포함), 마운트 지점 또는 볼륨 이름 지정:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨</span>

- 특정 볼륨의 오류 수정:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨</span>` /f`

- 검사 전에 특정 볼륨을 마운트 해제:

`chkdsk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨</span>` /x`

- 로그 파일 크기를 특정 크기로 변경 (NTFS 전용):

`chkdsk /l`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">크기</span>
