---
layout: page
title: common/duplicity (한국어)
description: "증분, 압축, 암호화 및 버전별 백업을 생성."
content_hash: 1d4e0a38e9ec09f6aedf83ab824a65bbb9641108
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/duplicity.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/duplicity.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/duplicity.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># duplicity

증분, 압축, 암호화 및 버전별 백업을 생성.
다양한 백엔드 서비스에 백업을 업로드할 수도 있음.
버전에 따라 일부 옵션을 사용하지 못할 수도 있음 (예: 2.0.0의 `--gio`).
더 많은 정보: <https://duplicity.gitlab.io>.

- FTPS를 통해 디렉터리를 원격 시스템에 백업하고, 비밀번호로 암호화:

`FTP_PASSWORD=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp_로그인_비밀번호</span>` PASSPHRASE=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호_비밀번호</span>` duplicity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스/디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftps://사용자@호스트명/타겟/디렉토리/경로/</span>

- 매월 전체 백업을 수행하여 Amazon S3에 디렉터리를 백업:

`duplicity --full-if-older-than `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1M</span>` s3://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버킷_이름[/접두사]</span>

- WebDAV 공유에 저장된 백업에서 1년이 넘은 버전을 삭제:

`FTP_PASSWORD=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">webdav_로그인_비밀번호</span>` duplicity remove-older-than `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1Y</span>` --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">webdav[s]://사용자@호스트명[:포트]/일부_디렉토리</span>

- 사용 가능한 백업을 나열:

`duplicity collection-status "file://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">절대/경로/대상/백업/디렉토리</span>`"`

- SSH를 통해 원격 시스템에 저장된 백업의 파일을 나열:

`duplicity list-current-files --time `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYY-MM-DD</span>` scp://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자@호스트명</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/백업/디렉토리</span>

- GnuPG로 암호화된 로컬 백업의 하위 디렉토리를 지정된 위치로 복원:

`PASSPHRASE=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpg_키_비밀번호</span>` duplicity restore --encrypt-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpg_키_아이디</span>` --path-to-restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">상대/경로/복원된디렉토리</span>` file://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">절대/경로/대상/백업/디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리/대상/복원/대상</span>
