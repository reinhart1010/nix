---
layout: page
title: common/chmod (中文)
description: "修改文件或目录的访问权限。"
content_hash: 62db19b725dd9b42728d01f4dbf424520e96b592
related_topics:
  - title: Deutsch version
    url: /de/common/chmod.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chmod.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/chmod.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chmod.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chmod.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chmod.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chmod.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chmod.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/chmod.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/chmod.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># chmod

修改文件或目录的访问权限。
更多信息：<https://www.gnu.org/software/coreutils/chmod>.

- 授予所有者［u］执行［x］文件的权限：

`chmod u+x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 授予所有者［u］读［r］和写［w］文件或目录的权限：

`chmod u+rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件或目录</span>

- 移除用户组［g］的文件执行［x］权限：

`chmod g-x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 授予所有用户［a］读［r］以及执行［x］文件的权限：

`chmod a+rx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 授予其他用户［o］（不在所有者用户组）和用户组［g］同样的权限：

`chmod o=g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 移除其他用户［o］的所有权限：

`chmod o= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 递归授予用户组［g］和其他用户［o］目录下所有文件和子目录的写［w］权限：

`chmod -R g+w,o+w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录</span>

- 递归授予所有用户［a］目录下文件的读［r］权限和子目录的执行［X］权限：

`chmod -R a+rX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目录</span>
