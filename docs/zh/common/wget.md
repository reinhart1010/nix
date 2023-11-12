---
layout: page
title: common/wget (中文)
description: "从网络上下载文件。"
content_hash: 1ae4949a41f64e633e4e2161e9e75860af253ad5
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/wget.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/wget.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/wget.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/wget.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/wget.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wget

从网络上下载文件。
支持 HTTP, HTTPS, 和 FTP.
更多信息：<https://www.gnu.org/software/wget>.

- 将该 URL 的内容下载到文件中（在这个例子中文件名为 "foo"）：

`wget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/foo</span>

- 将该 URL 的内容下载到文件中（在这个例子中文件名为 "bar"）：

`wget --output-document `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/foo</span>

- 以每三秒一个请求的速度下载一个网页和其所有资源（脚本，样式表，图片等等）：

`wget --page-requisites --convert-links --wait=3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/somepage.html</span>

- 从一个目录中下载所有列出的文件和其所有子文件夹（不下载内嵌网页）：

`wget --mirror --no-parent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/somepath/</span>

- 限制下载速度和重试次数：

`wget --limit-rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300k</span>` --tries=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/somepath/</span>

- 使用基本授权来从 HTTP/FTP 服务器中下载文件：

`wget --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 继续一个未完成的下载任务：

`wget --continue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 将指定文件中所有列出的 URL 下载到一个目录中：

`wget --directory-prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --input-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URLs.txt</span>
