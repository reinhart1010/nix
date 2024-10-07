---
layout: page
title: common/git-feature (한국어)
description: "기능 브랜치를 생성하거나 병합."
content_hash: 789210121514c6a7512643423eff2146d5f777bc
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-feature.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-feature.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git feature

기능 브랜치를 생성하거나 병합.
기능 브랜치는 feature/<이름> 형식을 따릅니다.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-feature>.

- 새 기능 브랜치를 생성하고 전환:

`git feature `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기능_브랜치</span>

- 기능 브랜치를 병합 커밋을 생성하며 현재 브랜치에 병합:

`git feature finish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기능_브랜치</span>

- 기능 브랜치를 하나의 커밋으로 합쳐서 현재 브랜치에 병합:

`git feature finish --squash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기능_브랜치</span>

- 특정 기능 브랜치의 변경 사항을 원격 대응 브랜치로 전송:

`git feature `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기능_브랜치</span>` --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>
