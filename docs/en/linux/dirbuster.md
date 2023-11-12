---
layout: page
title: linux/dirbuster (English)
description: "Brute force directories and filenames on servers."
content_hash: 3526ef43d0de3bfbd8773ab8f0818b4008d376be
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# dirbuster

Brute force directories and filenames on servers.
More information: <https://www.kali.org/tools/dirbuster/>.

- Start in GUI mode:

`dirbuster -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- Start in headless (no GUI) mode:

`dirbuster -H -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- Set the file extension list:

`dirbuster -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt,html</span>

- Enable verbose output:

`dirbuster -v`

- Set the report location:

`dirbuster -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/report.txt</span>
