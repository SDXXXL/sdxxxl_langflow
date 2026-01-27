> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up resource tags

<Check>
  Before diving into this content, it might be helpful to read the following:

  * [Conceptual guide on organizations and workspaces](/langsmith/administration-overview)
</Check>

<Info>
  Resource tags are available for Plus and Enterprise plans.
</Info>

While workspaces help separate trust boundaries and access control, tags help you organize resources within a workspace. Tags are key-value pairs that you can attach to resources.

<Note>
  **Not to be confused with commit tags**: Resource tags are key-value pairs used to organize and filter workspace resources (projects, datasets, prompts, etc.). [Commit tags](/langsmith/manage-prompts#commit-tags) are labels that reference specific versions in a prompt's commit history. While both types of tags can use similar terminology (like `prod` or `staging`), resource tags help you *organize resources* across your workspace, while commit tags control *which version* of a prompt is used in your code.
</Note>

## Create a tag

To create a tag, head to the workspace settings and click on the "Resource Tags" tab. Here, you'll be able to see the existing tag values, grouped by key. Two keys `Application` and `Environment` are created by default; the `Application` key is used to filter resources shown in the UI.

To create a new tag, click on the "New Tag" button. You'll be prompted to enter a key and a value for the tag. Note that you can use an existing key or create a new one.

<img src="https://mintcdn.com/langchain-5e9cc07a/aKRoUGXX6ygp4DlC/langsmith/images/create-tag.png?fit=max&auto=format&n=aKRoUGXX6ygp4DlC&q=85&s=7482c51de04fbfa54731159c9f44c4e7" alt="Create tag" data-og-width="1460" width="1460" data-og-height="1268" height="1268" data-path="langsmith/images/create-tag.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/aKRoUGXX6ygp4DlC/langsmith/images/create-tag.png?w=280&fit=max&auto=format&n=aKRoUGXX6ygp4DlC&q=85&s=5a5a406729553197c361b802663af22f 280w, https://mintcdn.com/langchain-5e9cc07a/aKRoUGXX6ygp4DlC/langsmith/images/create-tag.png?w=560&fit=max&auto=format&n=aKRoUGXX6ygp4DlC&q=85&s=5618e46f4895c858a234a62b2222b5d7 560w, https://mintcdn.com/langchain-5e9cc07a/aKRoUGXX6ygp4DlC/langsmith/images/create-tag.png?w=840&fit=max&auto=format&n=aKRoUGXX6ygp4DlC&q=85&s=0dc3a636385e4c0502d23c50013696d8 840w, https://mintcdn.com/langchain-5e9cc07a/aKRoUGXX6ygp4DlC/langsmith/images/create-tag.png?w=1100&fit=max&auto=format&n=aKRoUGXX6ygp4DlC&q=85&s=a138f20d0755211084e7352a6aa98dbc 1100w, https://mintcdn.com/langchain-5e9cc07a/aKRoUGXX6ygp4DlC/langsmith/images/create-tag.png?w=1650&fit=max&auto=format&n=aKRoUGXX6ygp4DlC&q=85&s=0255e6c9c526c32ea01e46b80dde19c7 1650w, https://mintcdn.com/langchain-5e9cc07a/aKRoUGXX6ygp4DlC/langsmith/images/create-tag.png?w=2500&fit=max&auto=format&n=aKRoUGXX6ygp4DlC&q=85&s=e35a3c90d4bd9584e773e2bd1cb28294 2500w" />

## Assign a tag to a resource

Within the same side panel for creating a new tag, you can also create assign resources to tags. Search for corresponding resources in the "Assign Resources" section and select the resources you want to tag.

<Note>
  You can only tag workspace-scoped resources with resource tags. This includes Tracing Projects, Annotation Queues, Deployments, Experiments, Datasets, and Prompts.
</Note>

To un-assign a tag from a resource, click on the Trash icon next to the tag, both in the tag panel and the resource tag panel.

## Delete a tag

You can delete either a key or a value of a tag from the [workspace settings page](https://smith.langchain.com/settings/workspaces/resource_tags). To delete a key, click on the Trash icon next to the key. To delete a value, click on the Trash icon next to the value.

Note that if you delete a key, all values associated with that key will also be deleted. When you delete a value, you will lose all associations between that value and resources.

<img src="https://mintcdn.com/langchain-5e9cc07a/aKRoUGXX6ygp4DlC/langsmith/images/delete-tag.png?fit=max&auto=format&n=aKRoUGXX6ygp4DlC&q=85&s=545b2cd5178bd4da31db56cde48f9f12" alt="Delete tag" data-og-width="1175" width="1175" data-og-height="1030" height="1030" data-path="langsmith/images/delete-tag.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/aKRoUGXX6ygp4DlC/langsmith/images/delete-tag.png?w=280&fit=max&auto=format&n=aKRoUGXX6ygp4DlC&q=85&s=059964ddd0ec5fffbe63bdf775dbd114 280w, https://mintcdn.com/langchain-5e9cc07a/aKRoUGXX6ygp4DlC/langsmith/images/delete-tag.png?w=560&fit=max&auto=format&n=aKRoUGXX6ygp4DlC&q=85&s=4b2fd607ef48d43555ec30f3689075d9 560w, https://mintcdn.com/langchain-5e9cc07a/aKRoUGXX6ygp4DlC/langsmith/images/delete-tag.png?w=840&fit=max&auto=format&n=aKRoUGXX6ygp4DlC&q=85&s=fe5f0a9b4c6695f9b1041e692bdf1799 840w, https://mintcdn.com/langchain-5e9cc07a/aKRoUGXX6ygp4DlC/langsmith/images/delete-tag.png?w=1100&fit=max&auto=format&n=aKRoUGXX6ygp4DlC&q=85&s=6012f1f83a031d5d84f2921f28f3ae4c 1100w, https://mintcdn.com/langchain-5e9cc07a/aKRoUGXX6ygp4DlC/langsmith/images/delete-tag.png?w=1650&fit=max&auto=format&n=aKRoUGXX6ygp4DlC&q=85&s=485c5e41e66ef679ebed451e291ce3ca 1650w, https://mintcdn.com/langchain-5e9cc07a/aKRoUGXX6ygp4DlC/langsmith/images/delete-tag.png?w=2500&fit=max&auto=format&n=aKRoUGXX6ygp4DlC&q=85&s=c172ee7ff2edc13aaead3fa392de80ef 2500w" />

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/set-up-resource-tags.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>