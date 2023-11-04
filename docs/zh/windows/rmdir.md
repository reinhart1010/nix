---
layout: page
title: windows/rmdir (中文)
description: "删除一个目录和其中的内容。"
content_hash: b57fd29256706985b955c18bea0490ee05b9b93b
last_modified_at: 2023-11-04
related_topics:
  - title: العربية version
    url: /ar/windows/rmdir.html
    icon: bi bi-globe
  - title: বাংলা version
    url: /bn/windows/rmdir.html
    icon: bi bi-globe
  - title: bosanski version
    url: /bs/windows/rmdir.html
    icon: bi bi-globe
  - title: català version
    url: /ca/windows/rmdir.html
    icon: bi bi-globe
  - title: čeština version
    url: /cs/windows/rmdir.html
    icon: bi bi-globe
  - title: dansk version
    url: /da/windows/rmdir.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/rmdir.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/rmdir.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/rmdir.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/windows/rmdir.html
    icon: bi bi-globe
  - title: suomi version
    url: /fi/windows/rmdir.html
    icon: bi bi-globe
  - title: français version
    url: /fr/windows/rmdir.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/rmdir.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/rmdir.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/rmdir.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/rmdir.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/rmdir.html
    icon: bi bi-globe
  - title: ລາວ version
    url: /lo/windows/rmdir.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/windows/rmdir.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/windows/rmdir.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/rmdir.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/windows/rmdir.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/rmdir.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/rmdir.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/windows/rmdir.html
    icon: bi bi-globe
  - title: română version
    url: /ro/windows/rmdir.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/rmdir.html
    icon: bi bi-globe
  - title: српски version
    url: /sr/windows/rmdir.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/windows/rmdir.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/rmdir.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/rmdir.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/windows/rmdir.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/windows/rmdir.html
    icon: bi bi-globe
  - title: o‘zbek version
    url: /uz/windows/rmdir.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/rmdir.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/rmdir.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rmdir

删除一个目录和其中的内容。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/rmdir>.

- 删除一个空目录：

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录的路径</span>

- 递归删除一个目录及其中的内容：

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录的路径</span>` /s`

- 在没有提示的情况下递归删除目录及其内容：

`rmdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` /s /q`
