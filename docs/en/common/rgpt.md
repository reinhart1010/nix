---
layout: page
title: common/rgpt (English)
description: "An automated code review tool that uses GPT you can use straight from your terminal."
content_hash: d2d0588976902435de23953d94ef340b914c81dc
last_modified_at: 2023-04-10
---
# rgpt

An automated code review tool that uses GPT you can use straight from your terminal.
More information: <https://github.com/vibovenkat123/review-gpt>.

- Ask GPT to improve the code with no extra options:

`rgpt --i "$(git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`)"`

- Get a more detailed verbose output from `rgpt` while reviewing the code:

`rgpt --v --i "$(git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`)"`

- Ask GPT to improve the code and limit it to a certain amount of GPT3 tokens:

`rgpt --max `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300</span>` --i "$(git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`)"`

- Ask GPT for a more unique result using a float value between 0 and 2. (higher = more unique):

`rgpt --pres `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2</span>` --i "$(git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`)"`

- Ask GPT to review your code using a specific model:

`rgpt --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">davinci</span>` --i "$(git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`)"`

- Make `rgpt` use a JSON output:

`rgpt --json --i "$(git diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>`)"`
