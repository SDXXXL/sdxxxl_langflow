> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Trace Claude Code

This guide shows you how to automatically send conversations from the [Claude Code CLI](https://code.claude.com/docs/en/overview) to LangSmith.

Once configured, you can opt-in to sending traces from Claude Code projects to LangSmith. Traces will include user messages, tool calls and assistant responses. As system prompts aren't returned in Claude Code's conversation transcripts, these are not included in the trace.

<div style={{ textAlign: 'center' }}>
  <img className="block dark:hidden" src="https://mintcdn.com/langchain-5e9cc07a/ibZBFaqiLl4UuJmc/langsmith/images/claude-code-trace.png?fit=max&auto=format&n=ibZBFaqiLl4UuJmc&q=85&s=d59e2e68fb03e868ddf5d6d2887c25e6" alt="LangSmith UI showing trace from Claude Code." data-og-width="2478" width="2478" data-og-height="1596" height="1596" data-path="langsmith/images/claude-code-trace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/ibZBFaqiLl4UuJmc/langsmith/images/claude-code-trace.png?w=280&fit=max&auto=format&n=ibZBFaqiLl4UuJmc&q=85&s=d1cec3f7adf1c3cbad885e77918f9017 280w, https://mintcdn.com/langchain-5e9cc07a/ibZBFaqiLl4UuJmc/langsmith/images/claude-code-trace.png?w=560&fit=max&auto=format&n=ibZBFaqiLl4UuJmc&q=85&s=d3fceeffc8c9796cb3d2d2a95d9f9785 560w, https://mintcdn.com/langchain-5e9cc07a/ibZBFaqiLl4UuJmc/langsmith/images/claude-code-trace.png?w=840&fit=max&auto=format&n=ibZBFaqiLl4UuJmc&q=85&s=531f7631f8c70fb5cbb021053bec3d29 840w, https://mintcdn.com/langchain-5e9cc07a/ibZBFaqiLl4UuJmc/langsmith/images/claude-code-trace.png?w=1100&fit=max&auto=format&n=ibZBFaqiLl4UuJmc&q=85&s=37355ed63ffecac752419053857f4f68 1100w, https://mintcdn.com/langchain-5e9cc07a/ibZBFaqiLl4UuJmc/langsmith/images/claude-code-trace.png?w=1650&fit=max&auto=format&n=ibZBFaqiLl4UuJmc&q=85&s=5bb693851b27f81483b25c06e917d582 1650w, https://mintcdn.com/langchain-5e9cc07a/ibZBFaqiLl4UuJmc/langsmith/images/claude-code-trace.png?w=2500&fit=max&auto=format&n=ibZBFaqiLl4UuJmc&q=85&s=a6ad02ca2d3ba75f7a696040a5e8db11 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/langchain-5e9cc07a/ibZBFaqiLl4UuJmc/langsmith/images/claude-code-trace-dark.png?fit=max&auto=format&n=ibZBFaqiLl4UuJmc&q=85&s=81330e8bbd01d5ef740a7b7472e5e173" alt="LangSmith UI showing trace from Claude Code." data-og-width="2480" width="2480" data-og-height="1564" height="1564" data-path="langsmith/images/claude-code-trace-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/ibZBFaqiLl4UuJmc/langsmith/images/claude-code-trace-dark.png?w=280&fit=max&auto=format&n=ibZBFaqiLl4UuJmc&q=85&s=c8d35a77173846ba56d3cf841a5b663a 280w, https://mintcdn.com/langchain-5e9cc07a/ibZBFaqiLl4UuJmc/langsmith/images/claude-code-trace-dark.png?w=560&fit=max&auto=format&n=ibZBFaqiLl4UuJmc&q=85&s=61083b3e1bf841ed1e2df85233410fad 560w, https://mintcdn.com/langchain-5e9cc07a/ibZBFaqiLl4UuJmc/langsmith/images/claude-code-trace-dark.png?w=840&fit=max&auto=format&n=ibZBFaqiLl4UuJmc&q=85&s=a782d8898b2a38c41a7ff5b89a2adaed 840w, https://mintcdn.com/langchain-5e9cc07a/ibZBFaqiLl4UuJmc/langsmith/images/claude-code-trace-dark.png?w=1100&fit=max&auto=format&n=ibZBFaqiLl4UuJmc&q=85&s=e4e089ff508bc5e2bdf89052aa0fde5d 1100w, https://mintcdn.com/langchain-5e9cc07a/ibZBFaqiLl4UuJmc/langsmith/images/claude-code-trace-dark.png?w=1650&fit=max&auto=format&n=ibZBFaqiLl4UuJmc&q=85&s=ea8be6805edcdb5cb3a2047c0dea216b 1650w, https://mintcdn.com/langchain-5e9cc07a/ibZBFaqiLl4UuJmc/langsmith/images/claude-code-trace-dark.png?w=2500&fit=max&auto=format&n=ibZBFaqiLl4UuJmc&q=85&s=a9266da4f4042d694b90474639cb2a29 2500w" />
</div>

## How it works

1. A global "Stop" [hook](https://code.claude.com/docs/en/hooks-guide#get-started-with-claude-code-hooks) is configured to run each time Claude Code responds.
2. The hook reads Claude Code’s generated conversation transcripts.
3. Messages in the transcript are converted into LangSmith runs and sent to your LangSmith project.

<Note> Tracing is opt-in and is enabled per Claude Code project using environment variables. </Note>

## Prerequisites

Before setting up tracing, ensure you have:

* **Claude Code CLI** installed.
* **LangSmith API key** ([get it here](https://smith.langchain.com/settings/apikeys)).
* **Command-line tool** `jq` - JSON processor ([install guide](https://jqlang.github.io/jq/download/))

<Info>
  This guide currently only supports macOS.
</Info>

## 1. Create the hook script

`stop_hook.sh` processes Claude Code's generated conversation transcripts and sends traces to LangSmith. Create the file `~/.claude/hooks/stop_hook.sh` with the following script: [stop\_hook.sh](https://github.com/langchain-ai/tracing-claude-code/blob/main/stop_hook.sh)

Make it executable:

```bash  theme={null}
chmod +x ~/.claude/hooks/stop_hook.sh
```

## 2. Configure the global hook

Set up a global hook in `~/.claude/settings.json` that runs the `stop_hook.sh` script. The global setting enables you to easily trace any Claude Code CLI project.

In `~/.claude/settings.json`, add the `Stop` hook.

```json  theme={null}
{
"hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash ~/.claude/hooks/stop_hook.sh"
          }
        ]
      }
    ]
  }
}
```

## 3. Enable tracing

For each Claude Code project (a Claude Code project is a directory with Claude Code initialized) where you want tracing enabled, create or edit [Claude Code's project settings file](https://code.claude.com/docs/en/settings#:~:text=Project%20settings%20are%20saved%20in%20your%20project%20directory%3A) `.claude/settings.local.json` to include the following environment variables:

* `TRACE_TO_LANGSMITH: "true"` - Enables tracing for this project. Remove or set to `false` to disable tracing.
* `CC_LANGSMITH_API_KEY` - Your LangSmith API key
* `CC_LANGSMITH_PROJECT` - The LangSmith project name where traces are sent
* (optional) `CC_LANGSMITH_DEBUG: "true"` - Enables detailed debug logging. Remove or set to `false` to disable tracing.

```json  theme={null}
{
  "env": {
    "TRACE_TO_LANGSMITH": "true",
    "CC_LANGSMITH_API_KEY": "lsv2_pt_...",
    "CC_LANGSMITH_PROJECT": "project-name",
    "CC_LANGSMITH_DEBUG": "true"

  }
}
```

<Note> Alternatively, to enable tracing to LangSmith for all Claude Code sessions, you can add the above JSON to your [global Claude Code settings.json](https://code.claude.com/docs/en/settings#:~:text=User%20settings%20are%20defined%20in%20~/.claude/settings.json%20and%20apply%20to%20all%20projects.) file. </Note>

## 4. Verify setup

Start a Claude Code session in your configured project. Traces will appear in LangSmith after Claude Code responds.

In LangSmith, you'll see:

* Each message to Claude Code appears as a trace.
* All turns from the same Claude Code session are grouped using a shared `thread_id` and can be viewed in the **Threads** tab of a project.

## Troubleshooting

### No traces appearing in LangSmith

1. **Check the hook is running**:
   ```bash  theme={null}
   tail -f ~/.claude/state/hook.log
   ```
   You should see log entries after each Claude response.

2. **Verify environment variables**:
   * Check that `TRACE_TO_LANGSMITH="true"` in your project's `.claude/settings.local.json`
   * Verify your API key is correct (starts with `lsv2_pt_`)
   * Ensure the project name exists in LangSmith

3. **Enable debug mode** to see detailed API activity:
   ```json  theme={null}
   {
     "env": {
       "CC_LANGSMITH_DEBUG": "true"
     }
   }
   ```
   Then check logs for API calls and HTTP status codes.

### Permission errors

Make sure the hook script is executable:

```bash  theme={null}
chmod +x ~/.claude/hooks/stop_hook.sh
```

### Required commands not found

Verify all required commands are installed:

```bash  theme={null}
which jq curl uuidgen
```

If `jq` is missing:

* **macOS**: `brew install jq`
* **Ubuntu/Debian**: `sudo apt-get install jq`

### Managing log file size

The hook logs all activity to `~/.claude/state/hook.log`. With debug mode enabled, this file can grow large:

```bash  theme={null}
# View log file size
ls -lh ~/.claude/state/hook.log

# Clear logs if needed
> ~/.claude/state/hook.log
```

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-claude-code.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>