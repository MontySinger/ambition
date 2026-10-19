# Sharpen

**Turn a rough request into a stronger assignment.**

Sharpen is an AI agent skill that helps you think through what you actually want, choose better methods, and define how to check the result. It improves the thinking behind a prompt as well as its wording.

Created by Monty Singer. Inspired by Felix Rieseberg’s [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/).

## Use it

Start with a messy request. You do not need a polished brief.

```text
$sharpen Research this company before my meeting tomorrow.
```

Sharpen uses relevant context already available, identifies the most consequential weakness in the request, and returns a prompt you can copy and use. It asks questions only when an answer would materially change the assignment.

| Invocation | What happens |
| --- | --- |
| `$sharpen [rough request]` | Think through the assignment and produce a copy-ready prompt. |
| `$sharpen and do it: [request]` | Improve the approach, then carry out the authorized task. |
| `$sharpen our approach: [context or disappointing result]` | Diagnose why the work is unhelpful and propose a correction. Continue execution only if already authorized. |

A task mentioned inside a prompt being refined stays draft material. Use **“and do it”** when you also want the underlying work carried out.

## What it looks for

- **Outcome:** What decision, action, or change should this enable?
- **Depth:** What evidence, tools, and methods would a strong practitioner actually use?
- **Range:** Would a useful method from another field improve the work?
- **Verification:** What observable evidence would show that the result succeeds?

Only the lenses that help are used. Simple requests should stay simple. Ambition still needs honest feasibility checks, evidence, and respect for your constraints.

## Example

An illustrative request:

```text
$sharpen Research this prospect.
```

A stronger assignment might be:

> Help me decide whether this company is worth pursuing for our consultancy. Use available evidence about its operations to identify a plausible problem we could solve. Separate facts from hypotheses, explain what remains unknown, and recommend the next step. If the evidence is weak, say so.

The improvement is a decision to support, a reason to gather evidence, and a useful stopping point.

## Install in Codex

Clone this repository into a folder named `sharpen` in your local skills directory. For the `~/.codex/skills` layout:

```sh
mkdir -p ~/.codex/skills
git clone https://github.com/MSizzle/sharpen.git ~/.codex/skills/sharpen
```

If `sharpen` is already installed, review or back it up before replacing it. The clone command will refuse to overwrite a nonempty folder.

Start a new Codex session and invoke `$sharpen` followed by your request.

The skill itself is plain Markdown. For another assistant, read [SKILL.md](SKILL.md) and use it as instructions, adapting the invocation to your host. Tool access and execution capabilities depend on that host.

## Files

- [SKILL.md](SKILL.md): the complete skill instructions.
- [agents/openai.yaml](agents/openai.yaml): Codex display name and default prompt.
- [LICENSE](LICENSE): MIT license for this repository’s original material.

## Inspiration and attribution

Felix Rieseberg’s article supplied the starting point: reconsider the outcome, go deeper into professional methods and source material, and draw useful techniques from other fields. Sharpen turns those ideas into a reusable workflow with explicit refinement and execution modes, low-friction questions, and observable checks.

This is an independent implementation by Monty Singer. The article remains Felix’s work and is linked here rather than reproduced. The MIT license does not cover the linked article, and no endorsement is implied.

## Improving the skill

Useful feedback starts with a real failure: the rough request, what went wrong, and what a useful result would have looked like. Remove private information before posting examples in public issues or pull requests.
