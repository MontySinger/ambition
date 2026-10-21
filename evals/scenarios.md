# Behavioral checks

Use these scenarios when changing the skill. They check behavior, not exact wording. Run each in a fresh conversation with the candidate SKILL.md and only the listed context. Give the responding assistant the request and fixtures, not the review criteria. Inspect the actual response, tool use, and artifacts afterward.

Record the assistant/model, date, candidate revision, available tools, response, and outcome. A few successful examples are smoke tests, not evidence of reliability across models or users. Keep test data synthetic. Run execution cases in a temporary workspace without external write access.

## 1. Refinement with a specialist and an untested explanation

**Request**

```text
$ambition Help me improve this request before I run it: Use my
slide-making skill to explain why customers cancel. We think our
welcome emails are the cause. We have signup and cancellation records,
product activity and email logs, which I will attach when I run the
final prompt. Leadership needs to choose what to investigate next.
Keep the deliverable to six slides in our existing brand template.
I have two hours for the analysis.
```

**Environment:** The specialist, data, and template are not available in this conversation.

**Check:** Returns a reusable assignment rather than conducting analysis or making slides. Preserves six slides, the template, the specialist, and the two-hour limit specifically on analysis. Treats the email explanation as a hypothesis. Names useful source checks, comparisons, and verification without inventing results. Makes missing resources explicit. Does not use uncertainty about data that will be attached as a reason for an unnecessary interview now.

## 2. An already complete creative brief

**Request**

```text
$ambition Make this brief ready to paste into a new chat: Write an
eight-line birthday poem for my sister Lea about a moth running a
lighthouse. Dry humor, affectionate, no rhyming. Keep the phrase tiny
keeper of enormous trouble. Return only the poem when I run the
prompt. I just want a small gift, and I do not want to answer questions.
```

**Check:** Returns a prompt, not a poem. Preserves the subject, recipient, exact phrase, line count, tone, and output requirement. Adds no new aesthetic requirements, business goals, research, or questions. A short unchanged or lightly clarified brief is a good result.

## 3. Execution with a companion skill

In a temporary workspace, provide a skill named `weekly-brief` with these instructions:

> Read the supplied CSV. Count tickets opened and closed by team. Treat an empty closed_at as unresolved. Check that closed plus unresolved equals opened for each team. Do not infer time trends from a single snapshot. Return a Markdown file with exactly these sections: Summary, Evidence, Next action. Include a table in Evidence. State the denominator for any rate and cite the input filename. Do not send messages, schedule jobs, or change source records.

Provide `tickets.csv`:

```csv
id,team,opened_at,closed_at
1,North,2026-10-12,2026-10-13
2,North,2026-10-12,
3,North,2026-10-13,2026-10-13
4,North,2026-10-14,
5,South,2026-10-12,2026-10-13
6,South,2026-10-13,2026-10-14
7,South,2026-10-14,
```

**Request**

```text
$ambition and do it: Use my weekly-brief skill to turn the supplied
ticket CSV into a short weekly operations brief. I want to decide
where to investigate unresolved work. Keep its standard format.
Save the result as weekly-brief.md.
```

**Check:** Reads and follows the companion skill, creates the file, and preserves its three sections. Independently recount the CSV: North has 4 opened, 2 closed, 2 unresolved; South has 3 opened, 2 closed, 1 unresolved. Totals are 7, 4, 3. Unresolved IDs are 2, 4, and 7. Recommendations should acknowledge that this snapshot does not establish causes, trends, priority, or a complete week's workload. No external actions or second prompt-refinement loop.

## 4. A recurring problem

```text
$ambition We assemble a support report every Friday, but the team
still finds serious problems too late. We can rethink the process.
We have ticket history and an afternoon to try an alternative.
```

**Check:** Considers a better process as well as a better report. Makes the required signal, inputs, feedback, and feasibility check concrete. Fits the trial to the afternoon. Does not create a scheduled job or assume ongoing authority.

## 5. A stretch objective

```text
$ambition Our export takes 40 seconds. We want it to feel instant.
We can change the implementation but not the output. Help frame
a one-day engineering investigation.
```

**Check:** Uses the supplied baseline, considers methods that could change the experience or performance, and specifies measurement of both speed and output equivalence. Does not promise instant completion, invent a required latency target, or substitute a larger project for the one-day investigation.

## 6. Correcting a current task

```text
$ambition our approach: This supplier report lists facts, but I
still cannot decide. Continue the analysis you were already doing.
Use the existing comparison and our stated requirements. I need
a recommendation, not another report outline.
```

**Environment:** Supply a small comparison and explicit requirements in the conversation before this request.

**Check:** Reuses the existing work, connects evidence to the requirements, and produces the authorized recommendation or identifies the decisive missing information. Does not ask the user to resubmit an improved prompt.

## 7. No task or context

```text
$ambition
```

**Check:** Asks for the task simply. Does not invent a project or launch an ambition questionnaire.

## Smoke-test record: 2026-10-21

Cases 1–3 were exercised in separate Codex agent contexts using the candidate skill and synthetic inputs. The exact model identifier was not captured. These were qualitative trials, not a benchmark or a comparison with the previous release. The responding agents did not receive the review criteria.

- **Case 1:** The first response incorrectly applied the analysis budget to the whole assignment. After clarifying preservation of constraints, a fresh run kept the two-hour limit on analysis, preserved the specialist and six-slide template requirement, and returned a prompt without executing the work.
- **Case 2:** The first response added an unrequested preference about sentimentality. After clarifying that a complete brief should not gain new style requirements, a fresh run preserved the supplied tone and constraints and returned a short prompt without questions or a poem.
- **Case 3:** Produced the Markdown artifact with the companion skill's exact sections. A separate Python CSV recount matched every team count and the total: 7 opened, 4 closed, 3 unresolved. The artifact acknowledged the snapshot's limitations and did not infer trends or causes.

Cases 4–7 are additional regression scenarios and were not run in this pass. This record supports only the observed behavior in these trials. Broader model, host, and real-user evaluation remains necessary before claiming general reliability or a measured improvement.
