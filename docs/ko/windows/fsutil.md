---
layout: page
title: windows/fsutil (한국어)
description: "파일 시스템 볼륨에 대한 정보를 표시."
content_hash: f3fd3d470c2d1cc0c0e0c1ba959c3db8e78cc634
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/fsutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fsutil

파일 시스템 볼륨에 대한 정보를 표시.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/fsutil>.

- 볼륨 목록 표시:

`fsutil volume list`

- 볼륨의 파일 시스템 정보 표시:

`fsutil fsInfo volumeInfo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">드라이브_문자|볼륨_경로</span>

- 모든 볼륨의 파일 시스템 자동 복구 현재 상태 표시:

`fsutil repair state`

- 모든 볼륨의 더티 비트 상태 표시:

`fsutil dirty query`

- 볼륨의 더티 비트 상태 설정:

`fsutil dirty set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">드라이브_문자|볼륨_경로</span>
