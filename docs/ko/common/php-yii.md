---
layout: page
title: common/php-yii (한국어)
description: "Yii 프레임워크의 명령줄 인터페이스."
content_hash: efb481d73787520eca3cb4cf3d6bc570f86d4646
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/php-yii.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/php-yii.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># php yii

Yii 프레임워크의 명령줄 인터페이스.
더 많은 정보: <https://yiiframework.com>.

- 현재 Yii 애플리케이션을 위해 PHP 내장 웹 서버 시작:

`php yii `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">serve</span>

- 지정된 모델 클래스에 대한 CRUD 작업을 위한 컨트롤러, 뷰 및 관련 파일 생성:

`php yii `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gii/crud</span>` --modelClass=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모델명</span>` --controllerClass=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨트롤러명</span>

- 도움말 표시:

`php yii `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">help</span>
