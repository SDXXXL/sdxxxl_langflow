> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

> Build an agent from a template

In this quickstart, you'll use the pre-defined **Email Assistant** [template](/langsmith/agent-builder-templates) that organizes and manages your inbox for you.

* Select a different template.

<Callout icon="comment" color="#8B5CF6" iconType="regular">
  You'll interact with your agent through chat, just like texting a helpful assistant.
</Callout>

## Before you start

You'll need:

* A LangSmith account ([sign up here](https://smith.langchain.com/agents?skipOnboarding=true)).
* A Gmail account.
* A Google calendar.
* An OpenAI or Anthropic API key (Step 1 will show you how to get one).

## 1. Get your model API key

Your agent needs an API key to connect to an AI model. The AI model is what allows your agent to understand and respond to your requests.

<Tabs>
  <Tab title="OpenAI (ChatGPT)">
    1. Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys).
    2. Click **Create new secret key**.
    3. Give it a name like "Agent Builder".
    4. Copy the key (it starts with `sk-`).
    5. Save it somewhere safe, you'll need it in Step 2.
  </Tab>

  <Tab title="Anthropic (Claude)">
    1. Go to [console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys).
    2. Click **Create Key**.
    3. Give it a name like "Agent Builder".
    4. Copy the key (it starts with `sk-ant-`).
    5. Save it somewhere safe, you'll need it in Step 2.
  </Tab>
</Tabs>

<Warning>
  Both services charge based on usage.
</Warning>

## 2. Add your API key to LangSmith

Now you'll add your API key to LangSmith so your agents can use it:

<Steps>
  <Step title="Open Settings">
    1. Go to [smith.langchain.com](https://smith.langchain.com).
    2. Click the <Icon icon="gear" /> **Settings** icon in the bottom left.
  </Step>

  <Step title="Go to Secrets">
    Click the **Secrets** tab at the top.
  </Step>

  <Step title="Add your key">
    1. Click **Add secret**.
    2. For **Key**, enter:
       * `OPENAI_API_KEY` (if using OpenAI)
       * `ANTHROPIC_API_KEY` (if using Anthropic)
    3. For **Value**, paste the API key you copied in Step 1.
    4. Click **Save secret**.
  </Step>
</Steps>

<Callout type="success" icon="check" color="#10B981" iconType="regular">
  Your agent now has access to an AI model to understand and respond to your requests. Next, you'll create your agent.
</Callout>

## 3. Create your agent

<Steps>
  <Step title="Navigate to Agent Builder">
    1. In the [LangSmith UI](https://smith.langchain.com), click <Icon icon="mouse-pointer" /> **Switch to Agent Builder** at the top of the left-hand navigation.
  </Step>

  <Step title="Choose a template">
    1. Select **Templates** in the left-hand navigation.
    2. Select **Email Assistant** template.
    3. Click **Use this template**.

    <Tip>
      If you don't want to start with a template, you have two other options. From the **+ New Agent** page:

      * **Chat**: Use the chat interface to describe your agent, and it will help you create it step-by-step.
      * **Manually**: Select **Create manually instead** to build your agent without any pre-filled responses on the configuration page.
    </Tip>
  </Step>

  <Step title="Authorize accounts">
    Your agent will ask you to connect your Google accounts:

    1. Click **Connect**.
    2. Sign in with your Google account.
    3. Review permissions and click **Allow**.
    4. You'll be redirected back to LangSmith where your agent will be created.
  </Step>
</Steps>

<Info>
  Your agent only accesses your accounts when working on tasks you give it. You can revoke access anytime in your Google account settings.
</Info>

## 4. View the agent template

<Steps>
  <Step title="View and customize the template">
    At this point, you can review the template instructions for the email assistant. If needed, you can make adjustments to the instructions.

    If you made any changes, click **Save changes**.
  </Step>

  <Step title="Start a test chat">
    1. In the right-hand panel of the configuration page, select the **Test Chat** tab.
    2. Try out the email assistant in the chat interface, for example:

       > *Apply a "Review" label to emails that I receive, which require some kind of review from me*
  </Step>

  <Step title="Agent starts working">
    Your agent will start work and provide a **Continue** option for each step that requires your approval.

    <img className="block dark:hidden" src="https://mintcdn.com/langchain-5e9cc07a/GV0X68p3yf3J2iDU/langsmith/images/agent-builder-response.png?fit=max&auto=format&n=GV0X68p3yf3J2iDU&q=85&s=7a96f9f6c7d7a5e78b0bf5e32b56103b" alt="Test chat output view with response including approvals for Gmail tool." data-og-width="670" width="670" data-og-height="974" height="974" data-path="langsmith/images/agent-builder-response.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/GV0X68p3yf3J2iDU/langsmith/images/agent-builder-response.png?w=280&fit=max&auto=format&n=GV0X68p3yf3J2iDU&q=85&s=c7dfe7157c35a84643fd603cce963afb 280w, https://mintcdn.com/langchain-5e9cc07a/GV0X68p3yf3J2iDU/langsmith/images/agent-builder-response.png?w=560&fit=max&auto=format&n=GV0X68p3yf3J2iDU&q=85&s=3b30e3d0f1eda37380b7dc118f570476 560w, https://mintcdn.com/langchain-5e9cc07a/GV0X68p3yf3J2iDU/langsmith/images/agent-builder-response.png?w=840&fit=max&auto=format&n=GV0X68p3yf3J2iDU&q=85&s=29002b926262477dc2ea2750f3ae4a33 840w, https://mintcdn.com/langchain-5e9cc07a/GV0X68p3yf3J2iDU/langsmith/images/agent-builder-response.png?w=1100&fit=max&auto=format&n=GV0X68p3yf3J2iDU&q=85&s=31d969e81cec3ca0fb4cdf6cf695c72e 1100w, https://mintcdn.com/langchain-5e9cc07a/GV0X68p3yf3J2iDU/langsmith/images/agent-builder-response.png?w=1650&fit=max&auto=format&n=GV0X68p3yf3J2iDU&q=85&s=a76417e0b0ea84a641250f16a146f738 1650w, https://mintcdn.com/langchain-5e9cc07a/GV0X68p3yf3J2iDU/langsmith/images/agent-builder-response.png?w=2500&fit=max&auto=format&n=GV0X68p3yf3J2iDU&q=85&s=d67c6d2823d7ffa89b4a4244f5e59980 2500w" />

    <img className="hidden dark:block" src="https://mintcdn.com/langchain-5e9cc07a/GV0X68p3yf3J2iDU/langsmith/images/agent-builder-response-dark.png?fit=max&auto=format&n=GV0X68p3yf3J2iDU&q=85&s=8c1a454a5437353a03e5a50304309a1b" alt="Test chat output view with response including approvals for Gmail tool." data-og-width="659" width="659" data-og-height="973" height="973" data-path="langsmith/images/agent-builder-response-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/langchain-5e9cc07a/GV0X68p3yf3J2iDU/langsmith/images/agent-builder-response-dark.png?w=280&fit=max&auto=format&n=GV0X68p3yf3J2iDU&q=85&s=5db2ae3cdc3a56be2b0657695f2cf013 280w, https://mintcdn.com/langchain-5e9cc07a/GV0X68p3yf3J2iDU/langsmith/images/agent-builder-response-dark.png?w=560&fit=max&auto=format&n=GV0X68p3yf3J2iDU&q=85&s=46611b324b61f1af2ddd51b410275809 560w, https://mintcdn.com/langchain-5e9cc07a/GV0X68p3yf3J2iDU/langsmith/images/agent-builder-response-dark.png?w=840&fit=max&auto=format&n=GV0X68p3yf3J2iDU&q=85&s=741d60d616be4c478bbfe41ab7012a86 840w, https://mintcdn.com/langchain-5e9cc07a/GV0X68p3yf3J2iDU/langsmith/images/agent-builder-response-dark.png?w=1100&fit=max&auto=format&n=GV0X68p3yf3J2iDU&q=85&s=d2388fc3f4ea6f672ae381fb3a8060ee 1100w, https://mintcdn.com/langchain-5e9cc07a/GV0X68p3yf3J2iDU/langsmith/images/agent-builder-response-dark.png?w=1650&fit=max&auto=format&n=GV0X68p3yf3J2iDU&q=85&s=e9e46cd7dca57cf404108832d06aa351 1650w, https://mintcdn.com/langchain-5e9cc07a/GV0X68p3yf3J2iDU/langsmith/images/agent-builder-response-dark.png?w=2500&fit=max&auto=format&n=GV0X68p3yf3J2iDU&q=85&s=4975c5e042427d6a5b9209debdd9f665 2500w" />

    3. As you test out the agent, you can make edits to the instructions, or add tools that you may need. Click **Save changes** when you're happy with the results.
  </Step>
</Steps>

## Edit your agent

You may want to update your agent's instructions or include more tools. You can directly chat with your agent to ask for updates, or you can:

1. From **My Agents** in the left-hand navigation, select the agent you want to edit.
2. Select <Icon icon="pencil" /> **Edit Agent**.

From the agent's edit page, you can:

* Add tools with **+ Add tool** to connect more apps and services like Slack, GitHub, or Linear.
* Add further helpers with **+ Add sub-agent** to break complex tasks into specialized sub-tasks.
* Request pauses for reviews on existing tools.
* Modify existing tools.
* Explore features that can trigger your agent to start a task.

## Next steps

Now that you've created your first agent, here's what to explore:

<CardGroup cols={2}>
  <Card title="Try more templates" icon="shapes" href="/langsmith/agent-builder-templates">
    Explore pre-built agents for common tasks
  </Card>

  <Card title="Add automation" icon="bolt" href="/langsmith/agent-builder-essentials#triggers">
    Run your agent automatically with triggers (Slack, email, schedules)
  </Card>

  <Card title="Connect more tools" icon="puzzle-piece" href="/langsmith/agent-builder-tools">
    Add Slack, GitHub, Linear, and more
  </Card>

  <Card title="Build complex agents" icon="sitemap" href="/langsmith/agent-builder-essentials#sub-agents">
    Use sub-agents to break down big tasks
  </Card>
</CardGroup>

***

<Callout icon="pen-to-square" iconType="regular">
  [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/agent-builder-quickstart.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
</Callout>

<Tip icon="terminal" iconType="regular">
  [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
</Tip>