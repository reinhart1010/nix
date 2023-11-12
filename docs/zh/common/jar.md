---
layout: page
title: common/jar (中文)
description: "Java 应用程序 / 类库打包程序。"
content_hash: 9ae7efcae70fef4887a5026ecf6343b3b4fdc3e2
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/jar.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jar.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/jar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jar

Java 应用程序 / 类库打包程序。
更多信息：<https://docs.oracle.com/javase/tutorial/deployment/jar/basicsindex.html>.

- 将当前目录中的所有文件递归归档到 `.jar` 文件中：

`jar cf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.jar</span>` *`

- 将 `.jar` / `.war` 文件解压缩到当前目录：

`jar -xvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.jar</span>

- 列出 `.jar` / `.war` 文件内容：

`jar tf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jar</span>

- 列出带有详细输出的 `.jar` / `.war` 文件内容：

`jar tvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.jar</span>
