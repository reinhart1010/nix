---
layout: page
title: common/yadm-clone (한국어)
description: "`git clone`과 유사하게 작동하며, 추가 플래그를 통해 저장소를 구성할 수 있습니다."
content_hash: da2d1843f09a5f0f8462ffdf9cdadc259454f67b
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/yadm-clone.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/yadm-clone.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># yadm-clone

`git clone`과 유사하게 작동하며, 추가 플래그를 통해 저장소를 구성할 수 있습니다.
저장소에 부트스트랩 파일이 있으면 실행 여부를 묻습니다.
같이 보기: `git clone`.
더 많은 정보: <https://yadm.io/docs/common_commands>.

- 기존 저장소 복제:

`yadm clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_저장소_위치</span>

- 기존 저장소를 복제하고 부트스트랩 파일 실행:

`yadm clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_저장소_위치</span>` --bootstrap`

- 기존 저장소를 복제한 후 부트스트랩 파일을 실행하지 않음:

`yadm clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_저장소_위치</span>` --no-bootstrap`

- 복제 중 `yadm`이 사용할 작업 트리 변경:

`yadm clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_저장소_위치</span>` --w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_트리_파일</span>

- `yadm`이 파일을 가져오는 분기 변경:

`yadm clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_저장소_위치</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">분기</span>

- 기존 저장소 로컬 분기 덮어쓰기:

`yadm clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_저장소_위치</span>` -f`
