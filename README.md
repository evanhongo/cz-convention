# Intro

## What is it

**cz-convention** is a plugin for [commitizen](https://github.com/commitizen-tools/commitizen)

## What it do

Create links to commits & author info in the CHANGELOG.md

## Installation

```sh
pip install cz-convention
cz init
```

## Config sample

cz.json

```json
{
  "commitizen": {
    "name": "cz_convention",
    "version": "0.0.1",
    "tag_format": "v$version",
    "git_provider": "github",
    "repo_url": "https://github.com/superman/super-project"
  }
}
```

.pre-commit-config.yaml

```yaml
repos:
  - repo: https://github.com/commitizen-tools/commitizen
    rev: v2.38.0
    hooks:
      - id: commitizen
        stages: [commit-msg]
        additional_dependencies: [cz-convention]
```