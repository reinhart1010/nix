---
layout: page
title: common/react-native-start (English)
description: "Command-line tools to start the React Native server."
content_hash: fd2aabcdd093fe6fbe01bee269de4001bfd05783
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# react-native start

Command-line tools to start the React Native server.
More information: <https://github.com/react-native-community/cli/blob/master/docs/commands.md#start>.

- Start the server that communicates with connected devices:

`react-native start`

- Start the metro bundler with a clean cache:

`react-native start --reset-cache`

- Start the server in a custom port (defaults to 8081):

`react-native start --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3000</span>

- Start the server in verbose mode:

`react-native start --verbose`

- Specify the maximum number of workers for transforming files (default is the number of CPU cores):

`react-native start --max-workers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>

- Disable interactive mode:

`react-native start --no-interactive`
