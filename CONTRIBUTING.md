# Contributing

Thanks for helping keep this list useful.

## Entry Criteria

An entry should be relevant to embodied AI, robot learning, imitation learning,
teleoperation, manipulation, navigation, or related robot datasets.

Each dataset entry should include:

- 📄 Paper
- 💻 Project page or code repository
- ⬇️ Original / canonical data location
- 🤖 LeRobot-format availability
- 📦 Dataset size, when known
- ⏱️ Dataset duration, when known
- ⚖️ License or access restrictions, when known
- ✅ Verification note

## LeRobot Format Status

Use one of these statuses:

- `native`: The dataset is released directly in LeRobot format.
- `community`: A third-party conversion exists.
- `official-conversion`: The dataset owner or LeRobot maintainers publish the
  conversion.
- `planned`: A public issue, PR, or roadmap mentions a conversion.
- `unknown`: No LeRobot-format version has been verified.

Avoid presenting an unverified conversion as available. If only a search result
or discussion thread exists, link it in the notes and mark the status as
`unknown` or `planned`.

## Suggested Entry Template

```markdown
### Dataset Name

- 📄 Paper: [Title](https://...)
- 💻 Project / repo: [name](https://...)
- ⬇️ Original / canonical data: [location](https://...)
- 🤖 LeRobot format: status; [dataset or conversion](https://...)
- 📦 Size: Hugging Face `Files and versions` total download size or `TBD`
- ⏱️ Duration: duration from metadata or `TBD`
- ⚖️ License: license or `TBD`
- 📝 Notes: One sentence about embodiment, tasks, scale, or caveats.
```

## Sorting

- Sort datasets by publication year, newest year first.
- Within a year, sort alphabetically by dataset name.
- Keep descriptions factual and short.
