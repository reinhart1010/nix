---
layout: page
title: common/wrangler (English)
description: "Cloudflare Workers command-line tool."
content_hash: e5768e755e3c9379a7e96eda10161794c35c5d7b
---
# wrangler

Cloudflare Workers command-line tool.
More information: <https://developers.cloudflare.com/workers/>.

- Initialize a project with a skeleton configuration:

`wrangler init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>

- Authenticate with Cloudflare:

`wrangler login`

- Start a local development server:

`wrangler dev --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>

- Publish the worker script:

`wrangler publish`

- Aggregate logs from the production worker:

`wrangler tail`
