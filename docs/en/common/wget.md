---
layout: page
title: common/wget (English)
description: "Download files from the Web."
content_hash: f5e4f812069707eeeb91d269b734b6a0f4ec61ca
related_topics:
  - title: italiano version
    url: /it/common/wget.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/wget.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/wget.html
    icon: bi bi-globe
---
# wget

Download files from the Web.
Supports HTTP, HTTPS, and FTP.
More information: <https://www.gnu.org/software/wget>.

- Download the contents of a URL to a file (named "foo" in this case):

`wget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/foo</span>

- Download the contents of a URL to a file (named "bar" in this case):

`wget --output-document `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/foo</span>

- Download a single web page and all its resources with 3-second intervals between requests (scripts, stylesheets, images, etc.):

`wget --page-requisites --convert-links --wait=3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/somepage.html</span>

- Download all listed files within a directory and its sub-directories (does not download embedded page elements):

`wget --mirror --no-parent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/somepath/</span>

- Limit the download speed and the number of connection retries:

`wget --limit-rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300k</span>` --tries=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/somepath/</span>

- Download a file from an HTTP server using Basic Auth (also works for FTP):

`wget --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Continue an incomplete download:

`wget --continue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Download all URLs stored in a text file to a specific directory:

`wget --directory-prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --input-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URLs.txt</span>
