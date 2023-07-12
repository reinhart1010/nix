---
layout: page
title: common/gallery-dl (English)
description: "Download image galleries and collections from several image hosting sites."
content_hash: f5116c7e5d4c21f655630c56d2b5d975640deb30
last_modified_at: 2023-07-12
---
# gallery-dl

Download image galleries and collections from several image hosting sites.
More information: <https://github.com/mikf/gallery-dl>.

- Download images from the specified URL:

`gallery-dl "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`"`

- Retrieve pre-existing cookies from your web browser (useful for sites that require login):

`gallery-dl --cookies-from-browser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">browser</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`"`

- Get the direct URL of an image from a site supporting authentication with username and password:

`gallery-dl --get-urls --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`"`

- Filter manga chapters by chapter number and language:

`gallery-dl --chapter-filter "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10 <= chapter < 20</span>`" --option "lang=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">language_code</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`"`
