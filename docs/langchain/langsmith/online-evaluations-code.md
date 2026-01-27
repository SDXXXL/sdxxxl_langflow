> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up online code evaluators

<Tip>
  **Recommended Reading**

  Before diving into this content, it might be helpful to read the following:

  * Running [online evaluations](/langsmith/evaluation-concepts#online-evaluations)
</Tip>

Online evaluations provide real-time feedback on your production traces. This is useful to continuously monitor the performance of your application—to identify issues, measure improvements, and ensure consistent quality over time.

Code evaluators allow you to write an evaluator in Python or JavaScript directly in LangSmith. Often used for validating structure or statistical properties of your data.

<Note>When an online evaluator runs on any run within a trace, the trace will be auto-upgraded to [extended data retention](/langsmith/administration-overview#data-retention-auto-upgrades). This upgrade will impact trace pricing, but ensures that traces meeting your evaluation criteria (typically those most valuable for analysis) are preserved for investigation. </Note>

## View online evaluators

Head to the **Tracing Projects** tab and select a tracing project. To view existing online evaluators for that project, click on the **Evaluators** tab.

<img src="https://mintcdn.com/langchain-5e9cc07a/1RIJxfRpkszanJLL/langsmith/images/view-evaluators.png?fit=max&auto=format&n=1RIJxfRpkszanJLL&q=85&s=471b55b0d23b6c54ea5044406f0c55f7" alt="View online evaluators" data-og-width="1350" width="1350" data-og-height="639" height="639" data-path="langsmith/images/view-evaluators.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/1RIJxfRpkszanJLL/langsmith/images/view-evaluators.png?w=280&fit=max&auto=format&n=1RIJxfRpkszanJLL&q=85&s=141082993aba37d45550bfff9da502df 280w, https://mintcdn.com/langchain-5e9cc07a/1RIJxfRpkszanJLL/langsmith/images/view-evaluators.png?w=560&fit=max&auto=format&n=1RIJxfRpkszanJLL&q=85&s=211cc6c5359e00ab23f0cf55bd67fd93 560w, https://mintcdn.com/langchain-5e9cc07a/1RIJxfRpkszanJLL/langsmith/images/view-evaluators.png?w=840&fit=max&auto=format&n=1RIJxfRpkszanJLL&q=85&s=fcdae1f3bce28bfcdd91059e43f9e1be 840w, https://mintcdn.com/langchain-5e9cc07a/1RIJxfRpkszanJLL/langsmith/images/view-evaluators.png?w=1100&fit=max&auto=format&n=1RIJxfRpkszanJLL&q=85&s=93b239efbd10f6ab5013e91b08384df6 1100w, https://mintcdn.com/langchain-5e9cc07a/1RIJxfRpkszanJLL/langsmith/images/view-evaluators.png?w=1650&fit=max&auto=format&n=1RIJxfRpkszanJLL&q=85&s=b6e496bee86cfb221cccde72366f83bb 1650w, https://mintcdn.com/langchain-5e9cc07a/1RIJxfRpkszanJLL/langsmith/images/view-evaluators.png?w=2500&fit=max&auto=format&n=1RIJxfRpkszanJLL&q=85&s=79817ff090124e1ec7b5f25eb2ddd978 2500w" />

## Configure online evaluators

#### 1. Navigate to online evaluators

Head to the **Tracing Projects** tab and select a tracing project. Click on **+ New** in the top right corner of the tracing project page, then click on **New Evaluator**. Select **code** evaluator.

#### 2. Name your evaluator

#### 3. Create a filter

For example, you may want to apply specific evaluators based on:

* Runs where a [user left feedback](/langsmith/attach-user-feedback) indicating the response was unsatisfactory.
* Runs that invoke a specific tool call. See [filtering for tool calls](/langsmith/filter-traces-in-application#example-filtering-for-tool-calls) for more information.
* Runs that match a particular piece of metadata (e.g. if you log traces with a `plan_type` and only want to run evaluations on traces from your enterprise customers). See [adding metadata to your traces](/langsmith/add-metadata-tags) for more information.

Filters on evaluators work the same way as when you're filtering traces in a project. For more information on filters, you can refer to [this guide](./filter-traces-in-application).

<Tip>
  It's often helpful to inspect runs as you're creating a filter for your evaluator. With the evaluator configuration panel open, you can inspect runs and apply filters to them. Any filters you apply to the runs table will automatically be reflected in filters on your evaluator.
</Tip>

#### 4. (Optional) Configure a sampling rate

Configure a sampling rate to control the percentage of filtered runs that trigger the automation action. For example, to control costs, you may want to set a filter to only apply the evaluator to 10% of traces. In order to do this, you would set the sampling rate to 0.1.

#### 5. (Optional) Apply rule to past runs

Apply rule to past runs by toggling the **Apply to past runs** and entering a "Backfill from" date. This is only possible upon rule creation. Note: the backfill is processed as a background job, so you will not see the results immediately.

In order to track progress of the backfill, you can view logs for your evaluator by heading to the **Evaluators** tab within a tracing project and clicking the Logs button for the evaluator you created. Online evaluator logs are similar to [automation rule logs](./rules#view-logs-for-your-automations).

* Add an evaluator name
* Optionally filter runs that you would like to apply your evaluator on or configure a sampling rate.
* Select **Apply Evaluator**

## Write your evaluation function

<Note>
  **Code evaluators restrictions.**

  **Allowed Libraries**: You can import all standard library functions, as well as the following public packages:

  ```
  numpy (v2.2.2): "numpy"
  pandas (v1.5.2): "pandas"
  jsonschema (v4.21.1): "jsonschema"
  scipy (v1.14.1): "scipy"
  sklearn (v1.26.4): "scikit-learn"
  ```

  **Network Access**: You cannot access the internet from a code evaluator.
</Note>

Code evaluators must be written inline. We recommend testing locally before setting up your code evaluator in LangSmith.

In the UI, you will see a panel that lets you write your code inline, with some starter code:

<img src="https://mintcdn.com/langchain-5e9cc07a/4kN8yiLrZX_amfFn/langsmith/images/online-eval-custom-code.png?fit=max&auto=format&n=4kN8yiLrZX_amfFn&q=85&s=cf7b75691edb3afaa10652a79813e581" alt="Code evaluator panel in LangSmith showing the inline code editor" data-og-width="2910" width="2910" data-og-height="902" height="902" data-path="langsmith/images/online-eval-custom-code.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/4kN8yiLrZX_amfFn/langsmith/images/online-eval-custom-code.png?w=280&fit=max&auto=format&n=4kN8yiLrZX_amfFn&q=85&s=acf6e6f3be5751c93a7287971fb18907 280w, https://mintcdn.com/langchain-5e9cc07a/4kN8yiLrZX_amfFn/langsmith/images/online-eval-custom-code.png?w=560&fit=max&auto=format&n=4kN8yiLrZX_amfFn&q=85&s=5df847b9d1f8171120853834d5d12f38 560w, https://mintcdn.com/langchain-5e9cc07a/4kN8yiLrZX_amfFn/langsmith/images/online-eval-custom-code.png?w=840&fit=max&auto=format&n=4kN8yiLrZX_amfFn&q=85&s=17d028d3e0709087a8be7e31343f0ab0 840w, https://mintcdn.com/langchain-5e9cc07a/4kN8yiLrZX_amfFn/langsmith/images/online-eval-custom-code.png?w=1100&fit=max&auto=format&n=4kN8yiLrZX_amfFn&q=85&s=668fd653028ebe056fed1e3963d3dc8e 1100w, https://mintcdn.com/langchain-5e9cc07a/4kN8yiLrZX_amfFn/langsmith/images/online-eval-custom-code.png?w=1650&fit=max&auto=format&n=4kN8yiLrZX_amfFn&q=85&s=62465285a785c577d0b0537c5ad307ca 1650w, https://mintcdn.com/langchain-5e9cc07a/4kN8yiLrZX_amfFn/langsmith/images/online-eval-custom-code.png?w=2500&fit=max&auto=format&n=4kN8yiLrZX_amfFn&q=85&s=7c342ba749987066e8ae05129e6a4fb7 2500w" />

Code evaluators take in one argument:

* A `Run` ([reference](/langsmith/run-data-format)). This represents the sampled run to evaluate.

They return a single value:

* Feedback(s) Dictionary: A dictionary whose keys are the type of feedback you want to return, and values are the score you will give for that feedback key. For example, `{"correctness": 1, "silliness": 0}` would create two types of feedback on the run, one saying it is correct, and the other saying it is not silly.

In the below screenshot, you can see an example of a simple function that validates that each run in the experiment has a known json field:

<CodeGroup>
  ```python Python theme={null}
  import json

  def perform_eval(run):
    output_to_validate = run['outputs']
    is_valid_json = 0

    # assert you can serialize/deserialize as json
    try:
      json.loads(json.dumps(output_to_validate))
    except Exception as e:
      return { "formatted": False }

    # assert output facts exist
    if "facts" not in output_to_validate:
      return { "formatted": False }

    # assert required fields exist
    if "years_mentioned" not in output_to_validate["facts"]:
      return { "formatted": False }

    return {"formatted": True}
  ```

  ```javascript JavaScript theme={null}
  function perform_eval(run) {
      const outputToValidate = run.outputs;

      // Assert you can serialize/deserialize as json
      try {
          JSON.stringify(outputToValidate);
          JSON.parse(JSON.stringify(outputToValidate));
      } catch (e) {
          return { "formatted": false };
      }

      // Assert output facts exist
      if (!("facts" in outputToValidate)) {
          return { "formatted": false };
      }

      // Assert required fields exist
      if (!outputToValidate["facts"].hasOwnProperty("years_mentioned")) {
          return { "formatted": false };
      }

      return { "formatted": true };
  }
  ```
</CodeGroup>

## Test and save your evaluation function

Before saving, you can test your evaluator function on a recent run by clicking **Test Code** to make sure that your code executes properly.

Once you **Save**, your online evaluator will run over newly sampled runs (or backfilled ones too if you chose the backfill option).

If you prefer a video tutorial, check out the [Online Evaluations video](https://academy.langchain.com/pages/intro-to-langsmith-preview) from the Introduction to LangSmith Course.

## Video guide

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/z69cBXTJFZ0?si=GBKQ9_muHR1zllLl" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/online-evaluations-code.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>