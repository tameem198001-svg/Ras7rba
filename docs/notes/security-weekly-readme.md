# Weekly security scan workflow
# Branch: ci/add-security-weekly-20260727

This workflow runs Bandit and Safety weekly and uploads reports as artifacts. If findings exist it will attempt to create an issue (requires GH CLI auth for the runner).