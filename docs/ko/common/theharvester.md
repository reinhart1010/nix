---
layout: page
title: common/theharvester (한국어)
description: "침투 테스트의 초기 단계에서 사용하도록 설계된 도구."
content_hash: 54af2fbfd5fdf3d049f9b295dc6617cba1a8388e
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/theharvester.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/theharvester.html
    icon: bi bi-globe
tldri18n_status: 2
---
# theHarvester

침투 테스트의 초기 단계에서 사용하도록 설계된 도구.
더 많은 정보: <https://github.com/laramies/theHarvester>.

- Google을 사용하여 도메인에 대한 정보 수집:

`theHarvester --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_이름</span>` --source google`

- 여러 소스를 사용하여 도메인에 대한 정보 수집:

`theHarvester --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_이름</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">duckduckgo,bing,crtsh</span>

- 결과 제한 변경:

`theHarvester --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_이름</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">google</span>` --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>

- XML 및 HTML 형식으로 출력 파일 두 개로 저장:

`theHarvester --domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_이름</span>` --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">google</span>` --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일_이름</span>

- 도움말 표시:

`theHarvester --help`
