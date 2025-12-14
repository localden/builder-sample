# Introduction to Vibe Coding for Microsoft Foundry Agents

These are the simplest instructions for creating a project and running an AI Agent with Microsoft Foundry. The goal is to get you started as quickly as possible with a minimalist agent, along with baseline instructions to vibe code a suitable web-based frontend.

## Phase 1: Create the Project (Foundry + Azure resources needed)

>[!NOTE]
>All paths start here. This sets up the cloud resources required for the rest of the exercise.

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fpaulyuk%2Fsimple-agent-af%2Fmain%2Finfra%2Fdeploybutton%2Fazuredeploy.json)

1. **Click** the "Deploy to Azure" button above
2. **Sign in** with your Azure credentials
3. **Configure:**
   * **Region:** Select **East US 2** (or your preferred region)
   * **Environment Name:** Enter `vibe-agent-offsite` (or your preferred name)
4. **Deploy:** Click **Review + Create**, then **Create**

>[!IMPORTANT]
>Make sure that you are selecting an Azure subscription you have write access to.

>[!NOTE]
>Provisioning can take 2-3 minutes.

**What gets created:**

* **Resource Group:** `rg-<your-environment-name>` (e.g., `rg-vibe-agent-offsite`)
* **Model Deployment:** Named `chat` using GPT-4.1-mini
* **Azure AI Foundry Project:** Named `simple-agent-<unique-id>`

Go to [Foundry Portal](https://ai.azure.com) and look for your project starting with **simple-agent** (view All Resources if needed). Alternatively, look for the resource group mentioned above to find all the relevant resources.

## Phase 2: Build the Agent

Choose your path - with code focus or the portal

### Path A: The Code (Developer Experience using Agent Framework)

***Best for**: Understanding SDK implementation and running locally.*

#### 1. Gather Your Credentials

Before running code, you need two values from your Azure/Foundry settings:

* **Azure OpenAI Endpoint:** (e.g., `https://<your-resource>.openai.azure.com/`)
* **Deployment Name:** (The name of the model you deployed, e.g., `chat`)

The endpoint we want for Agent Framework is the Azure OpenAI one.

![Selecting the OpenAI endpoint](./media/endpoint.gif)

E.g. a valid endpoint looks like:

```shell
https://agent-ai-servicesou6taoycpkkwc.openai.azure.com/
```

>[!IMPORTANT]
>Make sure that you are **not using** the _New Foundry_ portal to quickly get the Azure OpenAI endpoint.

#### 2. Configure Environment Variables

Copy the block matching your OS into your terminal to set the variables for the current session.

**PowerShell**

```powershell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-foundry-project-id>.openai.azure.com/"
$env:AZURE_OPENAI_DEPLOYMENT_NAME = "chat"
```

**macOS / Linux**

```bash
export AZURE_OPENAI_ENDPOINT="https://<your-foundry-project-id>.openai.azure.com/"
export AZURE_OPENAI_DEPLOYMENT_NAME="chat"
```

#### 3. Run the Agent

**Option 1: Python**

* **Repo:** [https://github.com/paulyuk/simple-agent-af-python](https://github.com/paulyuk/simple-agent-af-python)

1. Clone the repository.
2. Open your terminal to the repo folder.
3. Run the environment variable commands from Step 2.
4. Follow the `README.md` to install dependencies in a virtual environment (`venv`) and run the agent script (`python main.py`).

**Option 2: C# / .NET**

* **Repo:** [https://github.com/paulyuk/simple-agent-af](https://github.com/paulyuk/simple-agent-af)

1. Clone the repository.
2. Open your terminal to the repo folder.
3. Run the environment variable commands from Step 2.
4. Follow the `README.md` to run the app (`dotnet run`).

You will know the agent is running successfully if you can have it answer your questions in the terminal.

### Path B: The Portal UX (No-Code using Agent Service)

***Best for**: Rapid prototyping, testing prompts, and visual verification.*

1. **Enter Agent Builder:** In your new project, look at the left-hand navigation menu and click **Agents**.
2. **Create:** Click **+ Create Agent**.
3. **Setup:**
   * **Name:** Give your agent a name.
   * **Model:** Select `gpt-4.1-mini` from the dropdown. *If no model is listed, click "Connect & deploy" to add one named `gpt-4.1-mini`.*
   * **Instructions:** Type a simple system prompt (e.g., "You are a helpful project management assistant.").
4. **Test:** Use the **Playground** chat window on the right to type a message and verify the response.