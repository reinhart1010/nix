---
layout: page
title: common/git-reauthor (한국어)
description: "작성자 신원에 대한 세부 정보를 변경합니다. 이 명령은 Git 기록을 재작성하므로 다음 푸시 시 `--force`가 필요합니다."
content_hash: f97a84e5b725a745dc1d404aa7b34d0cbe10a77e
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-reauthor.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-reauthor.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git reauthor

작성자 신원에 대한 세부 정보를 변경합니다. 이 명령은 Git 기록을 재작성하므로 다음 푸시 시 `--force`가 필요합니다.
`git-extras`의 일부입니다.
더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-reauthor>.

- Git 저장소 전체에서 작성자의 이메일과 이름 변경:

`git reauthor --old-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old@example.com</span>` --correct-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new@example.com</span>` --correct-name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`"`

- Git 설정에 정의된 이메일과 이름으로 변경:

`git reauthor --old-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old@example.com</span>` --use-config`

- 원래 작성자와 관계없이 모든 커밋의 이메일과 이름 변경:

`git reauthor --all --correct-email `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name@example.com</span>` --correct-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
