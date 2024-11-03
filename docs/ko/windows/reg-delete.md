---
layout: page
title: windows/reg-delete (한국어)
description: "레지스트리에서 키 또는 해당 값을 삭제."
content_hash: 798deb3c5812a32afbb11dc5609928f6312a5574
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/reg-delete.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/reg-delete.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg delete

레지스트리에서 키 또는 해당 값을 삭제.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-delete>.

- 특정 레지스트리 키 삭제:

`reg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>

- 특정 키 아래의 [v]alue 삭제:

`reg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` /v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 지정된 키 아래의 모든 [v]alue를 재귀적으로 삭제:

`reg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` /va`

- 프롬프트 없이 강제로 특정 키 아래의 모든 [v]alue를 재귀적으로 삭제:

`reg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` /f /va`
