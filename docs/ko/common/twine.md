---
layout: page
title: common/twine (한국어)
description: "Python 패키지를 PyPI에 배포하는 도구."
content_hash: ac3c59d6dcee48680197f610396cd304601baab2
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/twine.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/twine.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># twine

Python 패키지를 PyPI에 배포하는 도구.
더 많은 정보: <https://twine.readthedocs.io/en/stable/#commands>.

- PyPI에 업로드:

`twine upload dist/*`

- Test PyPI 저장소에 업로드하여 검증:

`twine upload -r testpypi dist/*`

- 지정된 사용자 이름과 비밀번호로 PyPI에 업로드:

`twine upload -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` dist/*`

- 대체 저장소 URL로 업로드:

`twine upload --repository-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_URL</span>` dist/*`

- 배포의 긴 설명이 PyPI에서 올바르게 렌더링되는지 확인:

`twine check dist/*`

- 특정 pypirc 설정 파일을 사용하여 업로드:

`twine upload --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설정_파일</span>` dist/*`

- 파일이 이미 존재할 경우 업로드 계속 (PyPI에 업로드할 때만 유효):

`twine upload --skip-existing dist/*`

- 자세한 정보를 표시하며 PyPI에 업로드:

`twine upload --verbose dist/*`
