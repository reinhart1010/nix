---
layout: page
title: linux/instaloader (English)
description: "Download pictures, videos, captions, and other metadata from Instagram."
content_hash: dc2dfa18ebf55b150da21d13f2ba751b6e97f015
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# instaloader

Download pictures, videos, captions, and other metadata from Instagram.
Note: You will need to provide Instagram login information if you want high-quality media downloads.
More information: <https://instaloader.github.io>.

- Download a profile:

`instaloader `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- Download highlights:

`instaloader --highlights `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- Download posts with geotags (if available), suppressing any user interaction:

`instaloader --quiet --geotags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- Specify a user agent for HTTP requests:

`instaloader --user-agent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_agent</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- Specify login info and download posts (useful for private profiles):

`instaloader --login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- Skip a target if the first downloaded file has been found (useful for updating Instagram archives):

`instaloader --fast-update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- Download stories and IGTV videos (login required):

`instaloader --login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` --stories --igtv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>

- Download all types of posts (login required):

`instaloader --login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` --stories --igtv --highlights `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>
