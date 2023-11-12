---
layout: page
title: common/http-server-upload (English)
description: "Zero-configuration command-line HTTP server which provides a lightweight interface to upload files."
content_hash: 9c614f7f1238f14cb8da144888da65ec26f6aae4
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# http-server-upload

Zero-configuration command-line HTTP server which provides a lightweight interface to upload files.
More information: <https://github.com/crycode-de/http-server-upload>.

- Start an HTTP server on the default port to upload files to the current directory:

`http-server-upload`

- Start an HTTP server with the specified maximum allowed file size for uploads in MiB (defaults to 200 MiB):

`MAX_FILE_SIZE=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size_in_megabytes</span>` http-server-upload`

- Start an HTTP server on a specific port to upload files to the current directory:

`PORT=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` http-server-upload`

- Start an HTTP server, storing the uploaded files in a specific directory:

`UPLOAD_DIR=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` http-server-upload`

- Start an HTTP server using a specific directory to temporarily store files during the upload process:

`UPLOAD_TMP_DIR=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` http-server-upload`

- Start an HTTP server accepting uploads with a specific token field in the HTTP post:

`TOKEN=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret</span>` http-server-upload`
