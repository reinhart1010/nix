---
layout: page
title: windows/reg-load (한국어)
description: "저장된 하위 키를 레지스트리의 다른 하위 키로 불러오기."
content_hash: 74f1f0065881c8689fa88f87cc7c9add833d6b34
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/reg-load.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/reg-load.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg load

저장된 하위 키를 레지스트리의 다른 하위 키로 불러오기.
참고: 이는 문제 해결 및 임시 키를 위해 사용됩니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-load>.

- 백업 파일을 지정된 키로 불러오기:

`reg load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.hiv</span>
