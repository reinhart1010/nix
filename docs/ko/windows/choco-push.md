---
layout: page
title: windows/choco-push (한국어)
description: "컴파일된 NuGet 패키지(`nupkg`)를 패키지 피드에 푸시합니다."
content_hash: a21471c8f4d26bed40ca664b3f963a86a10a8356
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/windows/choco-push.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/choco-push.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco-push

컴파일된 NuGet 패키지(`nupkg`)를 패키지 피드에 푸시합니다.
더 많은 정보: <https://docs.chocolatey.org/en-us/create/commands/push>.

- 컴파일된 `nupkg`를 지정된 피드에 푸시:

`choco push --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://push.chocolatey.org/</span>

- 지정된 피드에 컴파일된 `nupkg`를 푸시하며, 초 단위로 타임아웃 설정 (기본값은 2700):

`choco push --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://push.chocolatey.org/</span>` --execution-timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">500</span>
