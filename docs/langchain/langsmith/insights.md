> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Discover errors and usage patterns with the Insights Agent

The Insights Agent automatically analyzes your traces to detect usage patterns, common agent behaviors and failure modes — without requiring you to manually review thousands of traces.

Insights uses hierarchical categorization to make sense of your data and highlight actionable trends.

<Note>
  Insights is available for LangSmith Plus and Enterprise [plans](https://www.langchain.com/pricing) and is only available for LangSmith SaaS deployments.
</Note>

## Prerequisites

* An OpenAI API key (generate one [on the OpenAI platform](https://platform.openai.com/account/api-keys)) or an Anthropic API key (generate one [on the Anthropic console](https://console.anthropic.com/settings/keys))
* Permissions to create rules in LangSmith (required to generate new Insights Reports)
* Permissions to view tracing projects LangSmith (required to view existing Insights Reports)

## Generate your first Insights report

<Frame caption="Auto configuration flow for Insights Agent">
  <img src="https://mintcdn.com/langchain-5e9cc07a/rp5c1TvRWS7-YcPd/langsmith/images/insights-autogenerate-config.png?fit=max&auto=format&n=rp5c1TvRWS7-YcPd&q=85&s=1055fe5ac43cdce00c43297e818db6b6" data-og-width="1498" width="1498" data-og-height="1408" height="1408" data-path="langsmith/images/insights-autogenerate-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/rp5c1TvRWS7-YcPd/langsmith/images/insights-autogenerate-config.png?w=280&fit=max&auto=format&n=rp5c1TvRWS7-YcPd&q=85&s=0c83b31a5a183ba5935b39b7b9de711d 280w, https://mintcdn.com/langchain-5e9cc07a/rp5c1TvRWS7-YcPd/langsmith/images/insights-autogenerate-config.png?w=560&fit=max&auto=format&n=rp5c1TvRWS7-YcPd&q=85&s=72217621fca8f07947a9461d75f42913 560w, https://mintcdn.com/langchain-5e9cc07a/rp5c1TvRWS7-YcPd/langsmith/images/insights-autogenerate-config.png?w=840&fit=max&auto=format&n=rp5c1TvRWS7-YcPd&q=85&s=b23c7627f8e62d8bebb7e94a0ec068da 840w, https://mintcdn.com/langchain-5e9cc07a/rp5c1TvRWS7-YcPd/langsmith/images/insights-autogenerate-config.png?w=1100&fit=max&auto=format&n=rp5c1TvRWS7-YcPd&q=85&s=5399d7c632e4bde4b5aefd4d19c8a175 1100w, https://mintcdn.com/langchain-5e9cc07a/rp5c1TvRWS7-YcPd/langsmith/images/insights-autogenerate-config.png?w=1650&fit=max&auto=format&n=rp5c1TvRWS7-YcPd&q=85&s=6be2b9f0c90979149f86e416c7cd4d8c 1650w, https://mintcdn.com/langchain-5e9cc07a/rp5c1TvRWS7-YcPd/langsmith/images/insights-autogenerate-config.png?w=2500&fit=max&auto=format&n=rp5c1TvRWS7-YcPd&q=85&s=adf51929b885117ba87e00be8f54d306 2500w" />
</Frame>

#### From the [LangSmith UI](https://smith.langchain.com)

1. Navigate to **Tracing Projects** in the left-hand menu and select a tracing project.
2. Click **+New** in the top right corner then **New Insights Report** to generate new insights over the project.
3. Enter a name for your job.
4. Click the <Icon icon="key" /> icon in the top right of the job creation pane to set your OpenAI (or Anthropic) API key as a [workspace secret](/langsmith/administration-overview#workspaces). If your workspace already has an OpenAI API key set, you can skip this step.
5. Answer the guided questions to focus your Insights Report on what you want to learn about your agent, then click **Run job**.

<Tip>Toggle to Manual mode to try [prebuilt configs](#using-a-prebuilt-config) for common use cases or [build your own](#building-a-config-from-scratch).</Tip>

This will kick off a background Insights Report. Reports can take up to 30 minutes to complete.

#### From the [LangSmith SDK](https://reference.langchain.com/python/langsmith/observability/sdk/client/#langsmith.client.Client)

You can generate Insights Reports over data stored outside LangSmith using the Python SDK. This allows you to analyze chat histories from your production systems, logs, or other sources.

When you call `generate_insights()`, the SDK will:

1. Upload your chat histories as traces to a new LangSmith project
2. Generate an Insights Report over those uploaded traces
3. Return a link to your results in the LangSmith UI

<CodeGroup>
  ```python Python theme={null}
  import os
  from langsmith import Client

  client = Client()

  chat_histories = [
      [
          {"role": "user", "content": "how are you"},
          {"role": "assistant", "content": "good!"},
      ],
      [
          {"role": "user", "content": "do you like art"},
          {"role": "assistant", "content": "only Tarkovsky"},
      ],
  ]

  report = client.generate_insights(
      chat_histories=chat_histories,
      name="Customer Support Topics - March 2024",
      instructions="What are the main topics and questions users are asking about?",
      openai_api_key=os.environ["OPENAI_API_KEY"],  # optional if already set as workspace secret
  )

  # client.poll_insights(report=report)
  ```
</CodeGroup>

<Note>
  Generating insights over 1,000 threads typically costs \$1.00-\$2.00 with OpenAI models and \$3.00-\$4.00 with current Anthropic models. The cost scales with the number of threads sampled and the size of each thread.
</Note>

## Understand the results

Once your job has completed, you can navigate to the **Insights** tab where you'll see a table of Insights Report. Each Report contains insights generated over a specific sample of traces from the tracing project.

<Frame caption="Insights Reports for a single tracing project">
  <img src="https://mintcdn.com/langchain-5e9cc07a/4-kFQm9_42J5OnwH/langsmith/images/insights-job-results.png?fit=max&auto=format&n=4-kFQm9_42J5OnwH&q=85&s=6068ead08d93b27a31e85dd35bdbca01" data-og-width="2540" width="2540" data-og-height="836" height="836" data-path="langsmith/images/insights-job-results.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/4-kFQm9_42J5OnwH/langsmith/images/insights-job-results.png?w=280&fit=max&auto=format&n=4-kFQm9_42J5OnwH&q=85&s=d89d356e627fe9b79a889f1b08f5b55e 280w, https://mintcdn.com/langchain-5e9cc07a/4-kFQm9_42J5OnwH/langsmith/images/insights-job-results.png?w=560&fit=max&auto=format&n=4-kFQm9_42J5OnwH&q=85&s=1e36efd2e207f240c943918bec0fb692 560w, https://mintcdn.com/langchain-5e9cc07a/4-kFQm9_42J5OnwH/langsmith/images/insights-job-results.png?w=840&fit=max&auto=format&n=4-kFQm9_42J5OnwH&q=85&s=81d1b513785c44c83e19e037ee2bac9c 840w, https://mintcdn.com/langchain-5e9cc07a/4-kFQm9_42J5OnwH/langsmith/images/insights-job-results.png?w=1100&fit=max&auto=format&n=4-kFQm9_42J5OnwH&q=85&s=bd6af403106f833511a03a2f2f58d866 1100w, https://mintcdn.com/langchain-5e9cc07a/4-kFQm9_42J5OnwH/langsmith/images/insights-job-results.png?w=1650&fit=max&auto=format&n=4-kFQm9_42J5OnwH&q=85&s=9de6145f9638aaa949b33cdae33de291 1650w, https://mintcdn.com/langchain-5e9cc07a/4-kFQm9_42J5OnwH/langsmith/images/insights-job-results.png?w=2500&fit=max&auto=format&n=4-kFQm9_42J5OnwH&q=85&s=f062f61dcc789fbc72a6fdf11fb76603 2500w" />
</Frame>

Click into your job to see traces organized into a set of auto-generated categories.

You can drill down through categories and subcategories to view the underlying traces, feedback, and run statistics.

<Frame caption="Common topics of conversations with the https://chat.langchain.com chatbot">
  <img src="https://mintcdn.com/langchain-5e9cc07a/4-kFQm9_42J5OnwH/langsmith/images/insights-nav.gif?s=6a22bfd0d94262b7aa78468a8379ea0f" data-og-width="800" width="800" data-og-height="516" height="516" data-path="langsmith/images/insights-nav.gif" data-optimize="true" data-opv="3" />
</Frame>

### Executive summary

At the top of each report, you'll find an executive summary that surfaces the most important patterns discovered in your traces. This includes:

* Key findings with percentages showing how often each pattern appears.
* Clickable references (e.g., #1, #2, #3) to traces the agent identified as exceptionally relevant to your question.

<Frame caption="Executive summary showing key patterns with trace references">
  <img src="https://mintcdn.com/langchain-5e9cc07a/Of41ZZ4fTt77Vjj5/langsmith/images/insights-summary.png?fit=max&auto=format&n=Of41ZZ4fTt77Vjj5&q=85&s=d565a549c83bad50398fa7a276eae0af" data-og-width="2202" width="2202" data-og-height="706" height="706" data-path="langsmith/images/insights-summary.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/Of41ZZ4fTt77Vjj5/langsmith/images/insights-summary.png?w=280&fit=max&auto=format&n=Of41ZZ4fTt77Vjj5&q=85&s=c3fca1bea9412fb8363361d2702ce08b 280w, https://mintcdn.com/langchain-5e9cc07a/Of41ZZ4fTt77Vjj5/langsmith/images/insights-summary.png?w=560&fit=max&auto=format&n=Of41ZZ4fTt77Vjj5&q=85&s=09f3dc0885400b40203f1d3783fba0c8 560w, https://mintcdn.com/langchain-5e9cc07a/Of41ZZ4fTt77Vjj5/langsmith/images/insights-summary.png?w=840&fit=max&auto=format&n=Of41ZZ4fTt77Vjj5&q=85&s=78eb3bde377ec55798d0117797e1f255 840w, https://mintcdn.com/langchain-5e9cc07a/Of41ZZ4fTt77Vjj5/langsmith/images/insights-summary.png?w=1100&fit=max&auto=format&n=Of41ZZ4fTt77Vjj5&q=85&s=75d04925165d1d6643c5e52ee5fb985b 1100w, https://mintcdn.com/langchain-5e9cc07a/Of41ZZ4fTt77Vjj5/langsmith/images/insights-summary.png?w=1650&fit=max&auto=format&n=Of41ZZ4fTt77Vjj5&q=85&s=c8872251a924aad5385fb0fae3433811 1650w, https://mintcdn.com/langchain-5e9cc07a/Of41ZZ4fTt77Vjj5/langsmith/images/insights-summary.png?w=2500&fit=max&auto=format&n=Of41ZZ4fTt77Vjj5&q=85&s=36cf847b04549cdae06e274d7108d430 2500w" />
</Frame>

### Top-level categories

Your traces are automatically grouped into top-level categories that represent the broadest patterns in your data.

The distribution bars show how frequently each pattern occurs, making it easy to spot behaviors that happen more or less than expected.

Each category has a brief description and displays aggregated metrics over the traces it contains, including:

* Typical trace stats (like error rates, latency, cost)
* Feedback scores from your evaluators
* [Attributes](#attributes) extracted as part of the job

### Subcategories

Clicking on any category shows a breakdown into subcategories, which gives you a more granular understanding of interaction patterns in that category of traces.

In the [Chat Langchain](https://chat.langchain.com) example pictured above, under "Data & Retrieval" there are subcategories like "Vector Stores" and "Data Ingestion".

### Individual traces

You can view the traces assigned to each category or subcategory by clicking through to see the traces table. From there, you can click into any trace to see the full conversation details.

## Configure a job

You can create an Insights Report three ways. Start with the auto-generated flow to spin up a baseline, then iterate with saved or manual configs as you refine.

### Autogenerating a config

1. Open **New Insights** and make sure the **Auto** toggle is active.
2. Answer the natural-language questions about your agent's purpose, what you want to learn, and how traces are structured. Insights will translate your answers into a draft config (job name, summary prompt, attributes, and sampling defaults).
3. Choose a provider, then click **Generate config** to preview or **Run job** to launch immediately.

**Providing useful context**

For best results, write a sentence or two for each prompt that gives the agent the context it needs—what you're trying to learn, which signals or fields matter most, and anything you already know isn't useful. The clearer you are about what your agent does and how its traces are structured, the more the Insights Agent can group examples in a way that's specific, actionable, and aligned with how you reason about your data.

**Describing your traces**

Explain how your data is organized—are these single runs or multi-turn conversations? Which inputs and outputs contain the key information? This helps the Insights Agent generate summary prompts and attributes that focus on what matters. You can also directly specify variables from the [summary prompt](#summary-prompt) section if needed.

### Choose a model provider

You can select either OpenAI or Anthropic models to power the agent. You must have the corresponding [workspace secret](/langsmith/administration-overview#workspaces) set for whichever provider you choose (`OPENAI_API_KEY` or `ANTHROPIC_API_KEY`).

Note that using current Anthropic models costs \~3x as much as using OpenAI models.

### Using a prebuilt config

<Frame caption="Prebuilt configs in Manual mode">
  <img src="https://mintcdn.com/langchain-5e9cc07a/fy0PJHxgSvYe7jF3/langsmith/images/insights-manual-config.png?fit=max&auto=format&n=fy0PJHxgSvYe7jF3&q=85&s=fa979566d61807f4f40c91cf9c6928f4" data-og-width="2220" width="2220" data-og-height="1440" height="1440" data-path="langsmith/images/insights-manual-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/fy0PJHxgSvYe7jF3/langsmith/images/insights-manual-config.png?w=280&fit=max&auto=format&n=fy0PJHxgSvYe7jF3&q=85&s=9497dc72f079e1dcec91d6fa5dfa963f 280w, https://mintcdn.com/langchain-5e9cc07a/fy0PJHxgSvYe7jF3/langsmith/images/insights-manual-config.png?w=560&fit=max&auto=format&n=fy0PJHxgSvYe7jF3&q=85&s=cad05d034c0631cebc422b04bc271f9a 560w, https://mintcdn.com/langchain-5e9cc07a/fy0PJHxgSvYe7jF3/langsmith/images/insights-manual-config.png?w=840&fit=max&auto=format&n=fy0PJHxgSvYe7jF3&q=85&s=8bc66817b550b2b01b52bda398b02405 840w, https://mintcdn.com/langchain-5e9cc07a/fy0PJHxgSvYe7jF3/langsmith/images/insights-manual-config.png?w=1100&fit=max&auto=format&n=fy0PJHxgSvYe7jF3&q=85&s=0852ae47cb4fd9f36d5dd7a9b143db63 1100w, https://mintcdn.com/langchain-5e9cc07a/fy0PJHxgSvYe7jF3/langsmith/images/insights-manual-config.png?w=1650&fit=max&auto=format&n=fy0PJHxgSvYe7jF3&q=85&s=d9abc923c29876e8c4abd3217214be82 1650w, https://mintcdn.com/langchain-5e9cc07a/fy0PJHxgSvYe7jF3/langsmith/images/insights-manual-config.png?w=2500&fit=max&auto=format&n=fy0PJHxgSvYe7jF3&q=85&s=51763ece975ee35a4ff9ac02ae90d251 2500w" />
</Frame>

Use the **Saved configurations** dropdown to load presets for common jobs like **Usage Patterns** or **Error Analysis**. Run them directly for a fast start, or adjust filters, prompts, and providers before saving your customized version. To learn more about what you can customize, read the section below.

### Building a config from scratch

Building your own config helps when you need more control—for example, predefining categories you want your data to be grouped into or targeting traces that match specific feedback scores and filters.

#### Select traces

* **Sample size**: The maximum number of traces to analyze. Currently capped at 1,000
* **Time range**: Traces are sampled from this time range
* **Filters**: Additional trace filters. As you adjust filters, you'll see how many traces match your criteria

#### Categories

By default, top-level categories are automatically generated bottom-up from the underlying traces.

In some instances, you know specific categories you're interested in upfront and want the job to bucket traces into those predefined categories.

The **Categories** section of the config lets you do this by enumerating the names and descriptions of the top-level categories you want to be used.

Subcategories are still auto-generated by the algorithm within the predefined top-level categories.

#### Summary prompt

The first step of the job is to create a brief summary of every trace — it is these summaries that are then categorized.

Extracting the right information in the summary is essential for getting useful categories.

The prompt used to generate these summaries can be edited.

The two things to think about when editing the prompt are:

* Summarization instructions: Any information that isn't in the trace summary won't affect the categories that get generated, so make sure to provide clear instructions on what information is important to extract from each trace.
* Trace content: Use mustache formatting to specify which parts of each trace are passed to the summarizer. Large traces with lots of inputs and outputs can be expensive and noisy. Reducing the prompt to only include the most relevant parts of the trace can improve your results.

The Insights Agent analyzes [threads](https://docs.langchain.com/langsmith/threads) - groups of related traces that represent multi-turn conversations. You must specify what parts of the thread to send to the summarizer using at least one of these template variables:

| Variable | Best for                                                                | Example                                            |
| -------- | ----------------------------------------------------------------------- | -------------------------------------------------- |
| `run.*`  | Access data from the most recent root run (i.e. final turn) in a thread | `{{run.inputs}}` `{{run.outputs}}` `{{run.error}}` |

You can also access nested fields using dot notation. For example, the prompt `"Summarize this: {{run.inputs.foo.bar}}"` will include only the "bar" value within the "foo" value of the last run's inputs.

#### Attributes

Along with a summary, you can define additional categorical, numerical, and boolean attributes to be extracted from each trace.
These attributes will influence the categorization step — traces with similar attribute values will tend to be categorized together.
You can also see aggregations of these attributes per category.

As an example, you might want to extract the attribute `user_satisfied: boolean` from each trace to steer the algorithm towards categories that split up positive and negative user experiences, and to see the average user satisfaction per category.

#### Filter attributes

You can use the `filter_by` parameter on boolean attributes to pre-filter traces before generating insights. When enabled, only traces where the attribute evaluates to `true` are included in the analysis.

This is useful when you want to focus your Insights Report on a specific subset of traces—for example, only analyzing errors, only examining English-language conversations, or only including traces that meet certain quality criteria.

<Frame caption="Using filter attributes to generate Insights only on traces with agent errors">
  <img src="https://mintcdn.com/langchain-5e9cc07a/L4LVgASBXoDKblmJ/langsmith/images/insights-filter-by-attribute.png?fit=max&auto=format&n=L4LVgASBXoDKblmJ&q=85&s=8cb30778befb18af445c3f6db758e631" data-og-width="1244" width="1244" data-og-height="490" height="490" data-path="langsmith/images/insights-filter-by-attribute.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/L4LVgASBXoDKblmJ/langsmith/images/insights-filter-by-attribute.png?w=280&fit=max&auto=format&n=L4LVgASBXoDKblmJ&q=85&s=b2a047279e60e995ce9de7fb44be3fc3 280w, https://mintcdn.com/langchain-5e9cc07a/L4LVgASBXoDKblmJ/langsmith/images/insights-filter-by-attribute.png?w=560&fit=max&auto=format&n=L4LVgASBXoDKblmJ&q=85&s=7fd3e854f73803434bc6490a33c77a1f 560w, https://mintcdn.com/langchain-5e9cc07a/L4LVgASBXoDKblmJ/langsmith/images/insights-filter-by-attribute.png?w=840&fit=max&auto=format&n=L4LVgASBXoDKblmJ&q=85&s=84b9cc1cc25ad8cc98962b584bca3ad1 840w, https://mintcdn.com/langchain-5e9cc07a/L4LVgASBXoDKblmJ/langsmith/images/insights-filter-by-attribute.png?w=1100&fit=max&auto=format&n=L4LVgASBXoDKblmJ&q=85&s=5d091df89be4d677139a21be120448f8 1100w, https://mintcdn.com/langchain-5e9cc07a/L4LVgASBXoDKblmJ/langsmith/images/insights-filter-by-attribute.png?w=1650&fit=max&auto=format&n=L4LVgASBXoDKblmJ&q=85&s=a6d991b404f2da6551c2cc696428e030 1650w, https://mintcdn.com/langchain-5e9cc07a/L4LVgASBXoDKblmJ/langsmith/images/insights-filter-by-attribute.png?w=2500&fit=max&auto=format&n=L4LVgASBXoDKblmJ&q=85&s=8c3cf044ac694ceb4818407c74c96b2e 2500w" />
</Frame>

**How it works:**

* Add `"filter_by": true` to any boolean attribute when creating a config for the Insights Agent
* The LLM evaluates each trace against the attribute description during summarization
* Traces where the attribute is `false` or missing are excluded before insights are generated

## Save your config

You can optionally save configs for future reuse using the 'save as' button.
This is especially useful if you want to compare Insights Reports over time to identify changes in user and agent behavior.

Select from previously saved configs in the dropdown in the top-left corner of the pane when creating a new Insights Report.

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/insights.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>