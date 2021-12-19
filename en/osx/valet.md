---
layout: page
title: osx/valet (English)
description: "A Laravel development environment that allows hosting sites via local tunnels on `http://<example>.test`."
content_hash: a1cc0f851243e460ce9a2410cfa4927588abd93f
---
# valet

A Laravel development environment that allows hosting sites via local tunnels on `http://<example>.test`.
More information: <https://laravel.com/docs/8.x/valet>.

- Start the valet daemon:

`valet start`

- Register the current working directory as a path that Valet should search for sites:

`valet park`

- View 'parked' paths:

`valet paths`

- Serve a single site instead of an entire directory:

`valet link app-name`

- Share a project via an Ngrok tunnel:

`valet share`
