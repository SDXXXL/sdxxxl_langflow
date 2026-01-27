> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up composite online evaluators

<Tip>
  **Recommended Reading**

  Before diving into this content, it might be helpful to read the following:

  * Running [online evaluations](/langsmith/evaluation-concepts#online-evaluation)
  * [Composite evaluators](/langsmith/composite-evaluators-ui)
</Tip>

Online evaluations provide real-time feedback on your production traces. This is useful to continuously monitor the performance of your application—to identify issues, measure improvements, and ensure consistent quality over time.

**Composite evaluators** are a way to combine multiple evaluator scores into a single [score](/langsmith/evaluation-concepts#evaluator-outputs). This is useful when you want to evaluate multiple aspects of your application and combine the results into a single result.

<Note>When an online evaluator runs on any run within a trace, the trace will be auto-upgraded to [extended data retention](/langsmith/administration-overview#data-retention-auto-upgrades). This upgrade will impact trace pricing, but ensures that traces meeting your evaluation criteria (typically those most valuable for analysis) are preserved for investigation. </Note>

## View online evaluators

Head to the **Tracing Projects** tab and select a tracing project. To view existing online evaluators for that project, click on the **Evaluators** tab.

<img src="https://mintcdn.com/langchain-5e9cc07a/1RIJxfRpkszanJLL/langsmith/images/view-evaluators.png?fit=max&auto=format&n=1RIJxfRpkszanJLL&q=85&s=471b55b0d23b6c54ea5044406f0c55f7" alt="View online evaluators" data-og-width="1350" width="1350" data-og-height="639" height="639" data-path="langsmith/images/view-evaluators.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/1RIJxfRpkszanJLL/langsmith/images/view-evaluators.png?w=280&fit=max&auto=format&n=1RIJxfRpkszanJLL&q=85&s=141082993aba37d45550bfff9da502df 280w, https://mintcdn.com/langchain-5e9cc07a/1RIJxfRpkszanJLL/langsmith/images/view-evaluators.png?w=560&fit=max&auto=format&n=1RIJxfRpkszanJLL&q=85&s=211cc6c5359e00ab23f0cf55bd67fd93 560w, https://mintcdn.com/langchain-5e9cc07a/1RIJxfRpkszanJLL/langsmith/images/view-evaluators.png?w=840&fit=max&auto=format&n=1RIJxfRpkszanJLL&q=85&s=fcdae1f3bce28bfcdd91059e43f9e1be 840w, https://mintcdn.com/langchain-5e9cc07a/1RIJxfRpkszanJLL/langsmith/images/view-evaluators.png?w=1100&fit=max&auto=format&n=1RIJxfRpkszanJLL&q=85&s=93b239efbd10f6ab5013e91b08384df6 1100w, https://mintcdn.com/langchain-5e9cc07a/1RIJxfRpkszanJLL/langsmith/images/view-evaluators.png?w=1650&fit=max&auto=format&n=1RIJxfRpkszanJLL&q=85&s=b6e496bee86cfb221cccde72366f83bb 1650w, https://mintcdn.com/langchain-5e9cc07a/1RIJxfRpkszanJLL/langsmith/images/view-evaluators.png?w=2500&fit=max&auto=format&n=1RIJxfRpkszanJLL&q=85&s=79817ff090124e1ec7b5f25eb2ddd978 2500w" />

## Configure composite online evaluators

You can create composite evaluators on a [tracing project](/langsmith/observability-concepts#projects) for [online evaluations](/langsmith/evaluation-concepts#online-evaluation). With composite evaluators in the UI, you can compute a weighted average or weighted sum of multiple evaluator scores, with configurable weights.

<div style={{ textAlign: 'center' }}>
  <img className="block dark:hidden" src="https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-light.png?fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=b3859ada8b576ebeaf5399ff15359b10" alt="LangSmith UI showing an LLM call trace called ChatOpenAI with a system and human input followed by an AI Output." data-og-width="756" width="756" data-og-height="594" height="594" data-path="langsmith/images/create_composite_evaluator-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-light.png?w=280&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=9bab5ad812328acdd6ffe858f487262b 280w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-light.png?w=560&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=4637a2dc732f945d98b0214023266180 560w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-light.png?w=840&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=c3e7b24dde21ed45f481b7a513ecc256 840w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-light.png?w=1100&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=1310a99e2a8b37d68d78f794b8ce6606 1100w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-light.png?w=1650&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=6beb89dcc6ec734b2ad012bc46c58821 1650w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-light.png?w=2500&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=ba7fd7ba48a3e46d8701b6f64bb68f66 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-dark.png?fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=ac13f4d2d4a5e3b67285284150b7d592" alt="LangSmith UI showing an LLM call trace called ChatOpenAI with a system and human input followed by an AI Output." data-og-width="761" width="761" data-og-height="585" height="585" data-path="langsmith/images/create_composite_evaluator-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-dark.png?w=280&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=bfc19d802f0327a579d90e519441cf9a 280w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-dark.png?w=560&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=23ab26db75e25795c17abf07e487ba5d 560w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-dark.png?w=840&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=7ce9597b62f3e68b2dc1afa5f17f0e8c 840w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-dark.png?w=1100&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=ee7058d60185a820fe23decf003bd2c1 1100w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-dark.png?w=1650&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=cff38ad541c55d6834edfa67f5650818 1650w, https://mintcdn.com/langchain-5e9cc07a/cRRwi1N4-QohYC73/langsmith/images/create_composite_evaluator-dark.png?w=2500&fit=max&auto=format&n=cRRwi1N4-QohYC73&q=85&s=0f85093799a489eff72dae01ed5b6d94 2500w" />
</div>

### 1. Navigate to the tracing project

To start configuring a composite evaluator, navigate to the **Tracing Projects** tab and select a project.

From within a tracing project: **+ New** > **Evaluator** > **Composite score**

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

Composite scores are attached to a run as **feedback**, similarly to feedback from a single evaluator.

**On a tracing project**:

* Composite scores appear as feedback on runs.
* [Filter for runs](/langsmith/filter-traces-in-application) with a composite score, or where the composite score meets a certain threshold.
* [Create a chart](/langsmith/dashboards#custom-dashboards) to visualize trends in the composite score over time.

<Note> If any of the constituent evaluators are not configured on the run, the composite score will not be calculated for that run. </Note>

## Video guide

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/z69cBXTJFZ0?si=GBKQ9_muHR1zllLl" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/online-evaluations-composite.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>