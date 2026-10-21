---
name: ambition
description: Turn a rough request into a more useful assignment by reconsidering its outcome, choosing concrete methods and evidence, and defining how to check the result. Use when asked to improve a prompt or brief, make an approach more ambitious, or rethink work that is not helping. Can prepare a prompt or improve and execute an authorized task with other available skills.
---

# Ambition

Help the user discover a worthwhile improvement to what they are asking for, then make it practical to pursue. Success means more useful work with less supervision. More words, tools, deliverables, or agents are not success by themselves.

Inspired by Felix Rieseberg's [article on ambition with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/). The workflow below is self-contained; reading the article is not required during use.

## 1. Choose the mode

| Request | Response |
| --- | --- |
| `$ambition [request]` | Improve the assignment and return a prompt to copy. Stop before doing the underlying work. |
| `$ambition and do it: [request]` | Improve the approach, then complete the authorized work. |
| `$ambition our approach: [context]` | Diagnose what is making the work unhelpful and recommend a correction. Continue work when already authorized. |

Recognize equivalent natural-language instructions. A task quoted for refinement is draft material, not permission to execute it. Preserve earlier explicit execution authorization. If the user supplies no task, use a clear task already in the conversation; otherwise ask what they want help with.

## 2. Find the useful opportunity

Start from relevant conversation and project context. Identify the intended outcome, chosen deliverable, constraints, and available inputs. Preserve constraints exactly, including which activity a time or cost limit applies to. Respect the user's voice, audience, and explicit boundaries. Label optional suggestions as optional; do not convert them into requirements. Inspect enough context to improve the assignment; do not perform the whole research task during refinement.

Consider the following directions internally, then select those that change the work for the better. Do not force every direction into every request.

- **Altitude: reconsider the task.** Identify the result the deliverable should enable. When the proposed artifact is only a means to that result, consider whether a different approach would help more. For recurring problems, consider a repeatable process with an observable trigger, necessary access, feedback, and a stopping or escalation condition. Present a meaningful change of scope as an option with its benefit and cost; do not silently adopt it or set up recurring activity. In creative work, the artifact, experience, or act of making it may be the goal. Preserve that intent.
- **Depth: improve the actual method.** Identify the primary material to examine, the concrete work a strong practitioner would do with it, and an assumption worth testing. Replace expert-sounding instructions with an operation: inspect records, reproduce a result, compare alternatives, measure a bottleneck, or run an appropriate experiment. When justified by the task, look for an overlooked explanation or a useful finding beyond the initial hypothesis. Specify how it could be checked before treating it as a discovery.
- **Range: borrow a useful technique.** Describe the job as actions people need to perform, then consider whether another discipline offers a method that helps. State the technique, its input, its contribution, and how it fits the assignment. A list of expert personas is not a method. Use additional agents only when authorized and when distinct work or independent critique earns the coordination cost.
- **Speed: preserve the efficient option.** Sometimes the useful improvement is simply doing an already clear task well and quickly. Keep a strong request intact. Do not manufacture a strategy exercise for a small edit.

Do not stop at cosmetic rewriting when a more valuable approach is apparent. For open-ended or constrained improvement tasks, consider a stretch objective that could change the method. Tie it to the user's outcome and a baseline or feasibility experiment. Treat it as a target to investigate, not a promised result; do not invent numerical targets, ignore physical limits, or turn uncertainty into confidence through repetition.

## 3. Make the assignment executable

Turn the selected improvement into an assignment containing only the detail needed to act:

- **Outcome and constraints:** What should the user be able to decide, experience, or do, and what must be preserved?
- **Inputs and method:** What available material will be used, what concrete steps matter, and what assumption will be examined?
- **Deliverable:** What usable result should be returned, in the requested format?
- **Check:** What evidence, test, measurement, or audience response could establish usefulness or correctness?

Match the check to the claim. Use a baseline for an improvement claim and separate evaluation data for a predictive claim when available. If the available evidence cannot support causation or generalization, narrow the conclusion. For subjective work, use the user's brief, preferences, and audience feedback rather than inventing an objective score. Another model's approval is critique, not independent proof.

Name unavailable inputs or capabilities when they matter. Offer a useful bounded alternative, with its limits. Do not claim access, run results, approvals, or evidence that does not exist. Respect the user's time and cost limits; stop when the agreed deliverable and check are complete. If they cannot be completed, report the specific gap and the smallest useful next step.

### Work with the user's skills

Ambition shapes the assignment; relevant specialist skills supply the execution workflow.

- Preserve explicitly requested skills, templates, and output formats. Use available skill descriptions to identify a relevant specialist, and read its instructions when needed to shape or execute the handoff. Avoid loading an entire skill library.
- Carry the outcome, inputs, constraints, deliverable, and check into that skill's workflow. Let it govern domain methods and artifact production within the user's instructions. Do not replace its required workflow with a generic Ambition checklist.
- In refinement mode, include the requested specialist skill in the copy-ready prompt without invoking it to execute. In execution mode, use it to do the work. Do not send the user through another prompt-refinement loop.
- If a named skill is unavailable, say so and describe the capability needed. Use a permitted equivalent only when it preserves the user's requirements; never pretend to have invoked the missing skill.

### Resolve only consequential uncertainty

Investigate what context can answer. For ordinary reversible choices, use sensible defaults. Ask only when an unresolved choice would materially alter the outcome, scope, or execution. Explain the tradeoff and recommend an option. Follow the user's input protocol if one exists; otherwise ask a focused question or a small related set. Do not make the user select among all the ambition directions or fill out a questionnaire.

## 4. Respond in the chosen mode

**Refine:** Briefly explain the most useful change, then provide one self-contained, copy-ready prompt. Use a plain text code block unless the host offers a better reusable format. Include relevant context so the prompt works in a new conversation; reference required files and identify any still needed. Prefer the few changes that matter over predesigning every execution step. Omit unused headings and reasoning checklists. If the request is already strong, say so and return it with only necessary edits. Do not add stylistic preferences or extra requirements just to justify a rewrite.

**Do it:** Briefly explain a meaningful change in approach, apply the relevant skills, and complete the authorized work. Report the result, the check actually performed, and any material limitation. Do not print a rewritten prompt unless requested. A material expansion still needs the user's agreement.

**Correct course:** Identify the mismatch between the current work and its intended use, then propose the smallest change likely to resolve it. Preserve useful work. If execution is already authorized, apply the correction and check whether it helped.
