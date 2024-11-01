---
layout: page
title: common/yolo (한국어)
description: "YOLO 명령줄 인터페이스는 다양한 작업과 버전에서 모델을 간단하게 학습, 검증 또는 추론할 수 있게 해줍니다."
content_hash: 534b5bcb567e337fcf198e9d9807037b038d6e30
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/yolo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/yolo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># yolo

YOLO 명령줄 인터페이스는 다양한 작업과 버전에서 모델을 간단하게 학습, 검증 또는 추론할 수 있게 해줍니다.
더 많은 정보: <https://docs.ultralytics.com/cli/>.

- 현재 작업 디렉토리에 기본 설정의 복사본 생성:

`yolo task=init`

- 지정된 설정 파일로 객체 탐지, 인스턴스 분할, 또는 분류 모델 학습:

`yolo task=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">detect|segment|classify</span>` mode=train cfg=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/config.yaml</span>
