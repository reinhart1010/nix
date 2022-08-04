---
layout: page
title: common/vercel (English)
description: "Deploy and manage your Vercel deployments."
content_hash: aed73e67ebc165bd239ed16be3649152dd5620b7
---
# vercel

Deploy and manage your Vercel deployments.
More information: <https://vercel.com/docs/cli>.

- Deploy the current directory:

`vercel`

- Deploy the current directory to production:

`vercel --prod`

- Deploy a directory:

`vercel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/project</span>

- Initialize an example project:

`vercel init`

- Deploy with Environment Variables:

`vercel --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ENV</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">var</span>

- Build with Environment Variables:

`vercel --build-env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ENV</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">var</span>

- Set default regions to enable the deployment on:

`vercel --regions `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">region_id</span>

- Remove a deployment:

`vercel remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">project_name</span>
