> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to create a composite evaluator

*Composite evaluators* are a way to combine multiple evaluator scores into a single [score](/langsmith/evaluation-concepts#evaluator-outputs). This is useful when you want to evaluate multiple aspects of your application and combine the results into a single result.

This guide shows you how to define a [composite evaluator](/langsmith/evaluation-concepts#llm-as-judge) using the [LangSmith UI](https://smith.langchain.com).

<Note>
  To create composite evaluators programmatically using the SDK, refer to [How to create a composite evaluator (SDK)](/langsmith/composite-evaluators-sdk).
</Note>

## Create a composite evaluator

You can create composite evaluators on a [tracing project](/langsmith/observability-concepts#projects) (for [online evaluations](/langsmith/evaluation-concepts#online-evaluation)) or a [dataset](/langsmith/evaluation-concepts#datasets) (for [offline evaluations](/langsmith/evaluation-concepts#offline-evaluation)). With composite evaluators in the UI, you can compute a weighted average or weighted sum of multiple evaluator scores, with configurable weights.

<div style={{ textAlign: 'center' }}>
  <img className="block dark:hidden" src="https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-light.png?fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=b3859ada8b576ebeaf5399ff15359b10" alt="LangSmith UI showing an LLM call trace called ChatOpenAI with a system and human input followed by an AI Output." data-og-width="756" width="756" data-og-height="594" height="594" data-path="langsmith/images/create_composite_evaluator-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-light.png?w=280&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=9bab5ad812328acdd6ffe858f487262b 280w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-light.png?w=560&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=4637a2dc732f945d98b0214023266180 560w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-light.png?w=840&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=c3e7b24dde21ed45f481b7a513ecc256 840w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-light.png?w=1100&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=1310a99e2a8b37d68d78f794b8ce6606 1100w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-light.png?w=1650&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=6beb89dcc6ec734b2ad012bc46c58821 1650w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-light.png?w=2500&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=ba7fd7ba48a3e46d8701b6f64bb68f66 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-dark.png?fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=ac13f4d2d4a5e3b67285284150b7d592" alt="LangSmith UI showing an LLM call trace called ChatOpenAI with a system and human input followed by an AI Output." data-og-width="761" width="761" data-og-height="585" height="585" data-path="langsmith/images/create_composite_evaluator-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-dark.png?w=280&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=bfc19d802f0327a579d90e519441cf9a 280w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-dark.png?w=560&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=23ab26db75e25795c17abf07e487ba5d 560w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-dark.png?w=840&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=7ce9597b62f3e68b2dc1afa5f17f0e8c 840w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-dark.png?w=1100&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=ee7058d60185a820fe23decf003bd2c1 1100w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-dark.png?w=1650&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=cff38ad541c55d6834edfa67f5650818 1650w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-dark.png?w=2500&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=0f85093799a489eff72dae01ed5b6d94 2500w" />
</div>

### 1. Navigate to the tracing project or dataset

To start configuring a composite evaluator, navigate to the **Tracing Projects** or **Dataset & Experiments** tab and select a project or dataset.

* From within a tracing project: **+ New** > **Evaluator** > **Composite score**
* From within a dataset: **+ Evaluator** > **Composite score**

### 2. Configure the composite evaluator

1. Name your evaluator.
2. Select an aggregation method, either **Average** or **Sum**.
   * **Average**: ∑(weight\*score) / ∑(weight).
   * **Sum**: ∑(weight\*score).
3. Add the feedback keys you want to include in the composite score.
4. Add the weights for the feedback keys. By default, the weights are equal for each feedback key. Adjust the weights to increase or decrease the importance of specific feedback keys in the final score.
5. Click **Create** to save the evaluator.

<Tip> If you need to adjust the weights for the composite scores, they can be updated after the evaluator is created. The resulting scores will be updated for all runs that have the evaluator configured. </Tip>

### 3. View composite evaluator results

Composite scores are attached to a run as **feedback**, similarly to feedback from a single evaluator. How you can view them depends on where the evaluation was run:

**On a tracing project**:

* Composite scores appear as feedback on runs.
* [Filter for runs](/langsmith/filter-traces-in-application) with a composite score, or where the composite score meets a certain threshold.
* [Create a chart](/langsmith/dashboards#custom-dashboards) to visualize trends in the composite score over time.

**On a dataset**:

* View the composite scores in the experiments tab. You can also filter and sort experiments based on the average composite score of their runs.
* Click into an experiment to view the composite score for each run.

<Note> If any of the constituent evaluators are not configured on the run, the composite score will not be calculated for that run. </Note>

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/composite-evaluators-ui.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>