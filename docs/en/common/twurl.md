---
layout: page
title: common/twurl (English)
description: "Curl-like command but tailored specifically for the Twitter API."
content_hash: afe8a5e28fb17a104c33b42000efe2c77d77cc19
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# twurl

Curl-like command but tailored specifically for the Twitter API.
More information: <https://github.com/twitter/twurl>.

- Authorize `twurl` to access a Twitter account:

`twurl authorize --consumer-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">twitter_api_key</span>` --consumer-secret `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">twitter_api_secret</span>

- Make a GET request to an API endpoint:

`twurl -X GET `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">twitter_api_endpoint</span>

- Make a POST request to an API endpoint:

`twurl -X POST -d '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endpoint_params</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">twitter_api_endpoint</span>

- Upload media to Twitter:

`twurl -H "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">twitter_upload_url</span>`" -X POST "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">twitter_upload_endpoint</span>`" --file "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/media.jpg</span>`" --file-field "media"`

- Access a different Twitter API host:

`twurl -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">twitter_api_url</span>` -X GET `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">twitter_api_endpoint</span>

- Create an alias for a requested resource:

`twurl alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alias_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">resource</span>
