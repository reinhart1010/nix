---
layout: page
title: linux/libreoffice (English)
description: "CLI for the powerful and free office suite LibreOffice."
content_hash: 0c5ac762e8a6e4a6e584fbba6ccc839f23130a17
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# libreoffice

CLI for the powerful and free office suite LibreOffice.
More information: <https://www.libreoffice.org/>.

- Open one or more files in read-only mode:

`libreoffice --view `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Display the content of one or more files:

`libreoffice --cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Print files using a specific printer:

`libreoffice --pt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">printer_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Convert all `.doc` files in current directory to PDF:

`libreoffice --convert-to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.doc</span>
