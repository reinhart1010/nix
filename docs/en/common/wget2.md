---
layout: page
title: common/wget2 (English)
description: "An improved version of `wget` for downloading files from the web."
content_hash: 0d0a5e27ed65e09565af0e39f92c72486dc6e48c
last_modified_at: 2024-10-08
tldri18n_status: 2
---
# wget2

An improved version of `wget` for downloading files from the web.
Supports HTTP, HTTPS, and HTTP/2 protocols with enhanced performance.
By default, `wget2` uses multiple threads for faster downloads.
More information: <https://gitlab.com/gnuwget/wget2>.

- Download the contents of a URL to a file using multiple threads (default behavior differs from `wget`):

`wget2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/foo</span>

- Limit the number of threads used for downloading (default is 5 threads):

`wget2 --max-threads=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/foo</span>

- Download a single web page and all its resources (scripts, stylesheets, images, etc.):

`wget2 --page-requisites --convert-links `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/somepage.html</span>

- Mirror a website, but do not ascend to the parent directory (does not download embedded page elements):

`wget2 --mirror --no-parent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/somepath/</span>

- Limit the download speed and the number of connection retries:

`wget2 --limit-rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300k</span>` --tries=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/somepath/</span>

- Continue an incomplete download (behavior is consistent with `wget`):

`wget2 --continue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Download all URLs stored in a text file to a specific directory:

`wget2 --directory-prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --input-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URLs.txt</span>

- Download a file from an HTTP server using Basic Auth (also works for HTTPS):

`wget2 --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>
