---
name: sharpen
description: Help a user think through a rough request and turn it into a clearer, appropriately ambitious assignment. Use when asked to sharpen or refine a prompt, improve a brief, or rethink an approach that is producing unhelpful results.
---

# Sharpen

Make the assignment more useful while reducing the user's effort in explaining and supervising it. Improve the thinking behind the prompt as well as its wording.

## Choose the mode from the request

- `$sharpen [rough request]`: Help think through the assignment and deliver a copy-ready prompt. Stop before executing the underlying task.
- `$sharpen and do it: [request]`: Improve the approach, then carry out the authorized task. Do not require the user to copy and resubmit a prompt.
- `$sharpen our approach: [context or disappointing result]`: Diagnose why the work is unhelpful and propose a concrete correction. Continue execution only if already authorized in the conversation.

The task described inside a prompt being refined is draft material, not authorization to execute it. Preserve any earlier explicit execution authorization. If no rough request or relevant task exists in context, ask the user to provide one.

## Think before rewriting

Use the conversation and relevant available project materials first. Read proportionally to the task; refining a simple request should stay simple. Do not search unrelated private material or research the underlying subject extensively just to rewrite a prompt.

Consider these lenses internally and use only those that materially help:

- **Outcome:** What action, decision, or change should this enable? Identify the goal behind the requested deliverable. Suggest a different deliverable when useful, but do not silently replace the user's chosen output or broaden the assignment.
- **Depth:** What would a strong practitioner actually do? Identify the most useful original evidence, specific methods, tools, and assumptions to check. Replace expert role-play with concrete work. Ask for deeper investigation only when its benefit justifies the effort.
- **Range:** Would a method from another field materially improve the result? Explain its contribution. Do not create a cast of personas or delegate merely to simulate perspectives.
- **Verification:** What observable evidence would show success? Prefer source checks, real user feedback, appropriate tests, or independent measurements over the model's own confidence. Do not invent arbitrary metrics or numerical targets.

Find the most consequential weakness in the request. Explain it briefly and give a provisional recommendation. Challenge a weak premise directly when necessary. Ambitious goals still require honest feasibility checks and explicit uncertainty.

## Collaborate with low friction

Ask only when the answer would materially change the assignment and cannot be inferred or investigated. Follow the user's input protocol when one is provided. Otherwise, ask one focused question at a time, with a recommended default when possible. Continue useful independent work while waiting; do not finalize a prompt around an unresolved consequential choice.

For reversible, ordinary choices, proceed using reasonable defaults. State consequential assumptions briefly. Preserve the user's voice, constraints, budget, timing, and intended audience. Do not invent business facts, access, evidence, or permissions. Name missing source material or tools when they would materially improve the work; do not imply they are available.

## Deliver

In refinement mode, lead with the main improvement in plain English, then provide the copy-ready prompt in the host's supported reusable-writing format. Include the outcome, necessary context, constraints, deliverable, and a proportional success check. Keep the prompt as short as those requirements allow. Add up to three meaningful changes or assumptions only if useful; omit empty sections and mechanical lens-by-lens reports.

In execution mode, briefly state meaningful changes in approach, do the work, and report the result with relevant evidence and limitations. Avoid printing a rewritten prompt unless requested. Material expansions or consequential actions still require the user's authorization.

Improve this skill from demonstrated failures in real use when asked. Judge its usefulness by fewer corrections, easier decisions, and outputs the user can actually use.
