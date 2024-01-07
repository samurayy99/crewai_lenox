# crewAI

![Logo of crewAI, tow people rowing on a boat](./crewai_logo.png)

🤖 Cutting-edge framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks.

- [Why CrewAI](#why-crewai)
- [Getting Started](#getting-started)
- [Key Features](#key-features)
- [Examples](#examples)
- [Local Open Source Models](#local-open-source-models)
- [CrewAI x AutoGen x ChatDev](#how-crewai-compares)
- [Contribution](#contribution)
- [License](#license)

## Why CrewAI?

The power of AI collaboration has too much to offer.
CrewAI is designed to enable AI agents to assume roles, share goals, and operate in a cohesive unit - much like a well-oiled crew. Whether you're building a smart assistant platform, an automated customer service ensemble, or a multi-agent research team, CrewAI provides the backbone for sophisticated multi-agent interactions.

- 🤖 [Talk with the Docs](https://chat.openai.com/g/g-qqTuUWsBY-crewai-assistant)
- 📄 [Documentation Wiki](https://github.com/joaomdmoura/CrewAI/wiki)

## Getting Started

To get started with CrewAI, follow these simple steps:

1. **Installation**:

```shell
pip install crewai
```

2. **Setting Up Your Crew**:

```python
import os
from crewai import Agent, Task, Crew, Process

os.environ["OPENAI_API_KEY"] = "Your Key"

# Define your agents with roles and goals
researcher = Agent(
  role='Researcher',
  goal='Discover new insights',
  backstory="You're a world class researcher working on a major data science company",
  verbose=True,
  allow_delegation=False
  # llm=OpenAI(temperature=0.7, model_name="gpt-4"). It uses langchain.chat_models, default is GPT4
)
writer = Agent(
  role='Writer',
  goal='Create engaging content',
  backstory="You're a famous technical writer, specialized on writing data related content",
  verbose=True,
  allow_delegation=False
)

# Create tasks for your agents
task1 = Task(description='Investigate the latest AI trends', agent=researcher)
task2 = Task(description='Write a blog post on AI advancements', agent=writer)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=2, # Crew verbose more will let you know what tasks are being worked on, you can set it to 1 or 2 to different logging levels
  process=Process.sequential # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.
)

# Get your crew to work!
result = crew.kickoff()
```

Currently the only supported process is `Process.sequential`, where one task is executed after the other and the outcome of one is passed as extra content into this next.

## Key Features

- **Role-Based Agent Design**: Customize agents with specific roles, goals, and tools.
- **Autonomous Inter-Agent Delegation**: Agents can autonomously delegate tasks and inquire amongst themselves, enhancing problem-solving efficiency.
- **Flexible Task Management**: Define tasks with customizable tools and assign them to agents dynamically.
- **Processes Driven**: Currently only supports `sequential` task execution but more complex processes like consensual and hierarchical being worked on.

![CrewAI Mind Map](/crewAI-mindmap.png "CrewAI Mind Map")

## Examples
You can test different real life examples of AI crews [in the examples repo](https://github.com/joaomdmoura/crewAI-examples?tab=readme-ov-file)

## Local Open Source Models
crewAI supports integration with local models, thorugh tools such as [Ollama](https://ollama.ai/), for enhanced flexibility and customization. This allows you to utilize your own models, which can be particularly useful for specialized tasks or data privacy concerns.

### Setting Up Ollama
- **Install Ollama**: Ensure that Ollama is properly installed in your environment. Follow the installation guide provided by Ollama for detailed instructions.
- **Configure Ollama**: Set up Ollama to work with your local model. You will probably need to [tweak the model using a Modelfile](https://github.com/jmorganca/ollama/blob/main/docs/modelfile.md). I'd recommend adding `Observation` as a stop word and playing with `top_p` and `temperature`.

### Integrating Ollama with CrewAI
- Instantiate Ollama Model: Create an instance of the Ollama model. You can specify the model and the base URL during instantiation. For example:

```python
from langchain.llms import Ollama
ollama_openhermes = Ollama(model="agent")
# Pass Ollama Model to Agents: When creating your agents within the CrewAI framework, you can pass the Ollama model as an argument to the Agent constructor. For instance:

local_expert = Agent(
  role='Local Expert at this city',
  goal='Provide the BEST insights about the selected city',
  backstory="""A knowledgeable local guide with extensive information
  about the city, it's attractions and customs""",
  tools=[
    SearchTools.search_internet,
    BrowserTools.scrape_and_summarize_website,
  ],
  llm=ollama_openhermes, # Ollama model passed here
  verbose=True
)
```

## How CrewAI Compares

- **Autogen**: While Autogen excels in creating conversational agents capable of working together, it lacks an inherent concept of process. In Autogen, orchestrating agents' interactions requires additional programming, which can become complex and cumbersome as the scale of tasks grows.

- **ChatDev**: ChatDev introduced the idea of processes into the realm of AI agents, but its implementation is quite rigid. Customizations in ChatDev are limited and not geared towards production environments, which can hinder scalability and flexibility in real-world applications.

**CrewAI's Advantage**: CrewAI is built with production in mind. It offers the flexibility of Autogen's conversational agents and the structured process approach of ChatDev, but without the rigidity. CrewAI's processes are designed to be dynamic and adaptable, fitting seamlessly into both development and production workflows.

## Contribution

CrewAI is open-source and we welcome contributions. If you're looking to contribute, please:

- Fork the repository.
- Create a new branch for your feature.
- Add your feature or improvement.
- Send a pull request.
- We appreciate your input!

### Installing Dependencies
```bash
poetry lock
poetry install
```

### Virtual Env
```bash
poetry shell
```

### Pre-commit hooks

```bash
pre-commit install
```

### Running Tests
```bash
poetry run pytest
```

### Packaging
```bash
poetry build
```

### Installing Locally
```bash
pip install dist/*.tar.gz
```

## License
CrewAI is released under the MIT License

CREWAI Documentation:

```
Understanding Agents
In CrewAI, an agent is an autonomous unit programmed to perform tasks, make decisions, and communicate with other agents. Think of an agent as a member of a team, with specific skills and a particular job to do. Agents can have different roles like 'Researcher', 'Writer', or 'Customer Support', each contributing to the overall goal of the crew.

Key Properties of an Agent

Role: Defines the agent's function within the crew. It determines the kind of tasks the agent is best suited for.
Goal: The individual objective that the agent aims to achieve. It guides the agent's decision-making process.
Backstory: Provides context to the agent's role and goal, enriching the interaction and collaboration dynamics.
Tools: A set of capabilities or functions that the agent can use to perform tasks. Tools can be shared or exclusive to specific agents.
Verbose: This allow you to actually see what is going on during the Crew execution.
Allow Delegation: Agents can delegate tasks or questions to one another, ensuring that each task is handled by the most suitable agent.
Agent Lifecycle

Initialization: An agent is created with a defined role, goal, backstory, and set of tools.
Task Assignment: The agent is assigned tasks either directly or through the crew's process management.
Execution: The agent performs the task using its available tools and in accordance with its role and goal.
Collaboration: Throughout the execution, the agent can communicate with other agents to delegate, inquire, or assist.
Creating an Agent

To create an agent, you would typically initialize an instance of the Agent class with the desired properties. Here's a conceptual example:

from crewai import Agent

# Create an agent with a role and a goal
agent = Agent(
  role='Data Analyst',
  goal='Extract actionable insights',
  verbose=True,
  backstory="You'er a data analyst at a large company. I am responsible for analyzing data and providing insights to the business. I am currently working on a project to analyze the performance of our marketing campaigns. I have been asked to provide insights on how to improve the performance of our marketing campaigns."
)
Agent Interaction

Agents can interact with each other using the CrewAI's built-in delegation and communication mechanisms. This allows for dynamic task management and problem-solving within the crew.

Conclusion

Agents are the building blocks of the CrewAI framework. By understanding how to define and interact with agents, you can create sophisticated AI systems that leverage the power of collaborative intelligence.
```

```
Defining Tasks
In the CrewAI framework, tasks are the individual assignments that agents are responsible for completing. They are the fundamental units of work that your AI crew will undertake. Understanding how to define and manage tasks is key to leveraging the full potential of CrewAI.

A task in CrewAI encapsulates all the information needed for an agent to execute it, including a description, the agent assigned to it, and any specific tools required. Tasks are designed to be flexible, allowing for both simple and complex actions depending on your needs.

Properties of a Task

Every task in CrewAI has several properties:

Description: A clear and concise statement of what needs to be done.
Agent: The agent assigned to the task (optional). If no agent is specified, the task can be picked up by any agent based on the process defined.
Tools: A list of tools (optional) that the agent can use to complete the task. These can override the agent's default tools if necessary.
Creating a Task

Creating a task is straightforward. You define what needs to be done and, optionally, who should do it and what tools they should use. Here’s a conceptual guide:

from crewai import Task

# Define a simple task with just a description
simple_task = Task(description='Validate user input data')

# Define a task with a designated agent and specific tools
advanced_task = Task(description='Generate monthly sales report', agent=sales_agent, tools=[reporting_tool])
Task Assignment

Tasks can be assigned to agents in several ways:

Directly, by specifying the agent when creating the task.
Through the Crew's process, which can assign tasks based on agent roles, availability, or other criteria.
Task Execution

Once a task has been defined and assigned, it's ready to be executed. Execution is typically handled by the Crew object, which manages the workflow and ensures that tasks are completed according to the defined process.

Task Collaboration

Tasks in CrewAI can be designed to require collaboration between agents. For example, one agent might gather data while another analyzes it. This collaborative approach can be defined within the task properties and managed by the Crew's process.

Conclusion

Tasks are the driving force behind the actions of agents in CrewAI. By properly defining tasks, you set the stage for your AI agents to work effectively, either independently or as a collaborative unit. In the following sections, we will explore how tasks fit into the larger picture of processes and crew management.
```

```
Managing Processes
Processes are the heart of CrewAI's workflow management, akin to the way a human team organizes its work. In CrewAI, processes define the sequence and manner in which tasks are executed by agents, mirroring the coordination you'd expect in a well-functioning team of people.

A process in CrewAI can be thought of as the game plan for how your AI agents will handle their workload. Just as a project manager assigns tasks to team members based on their skills and the project timeline, CrewAI processes assign tasks to agents to ensure efficient workflow.

Process Implementations

Sequential (Supported): This is the only process currently implemented in CrewAI. It ensures tasks are handled one at a time, in a given order, much like a relay race where one runner passes the baton to the next.
Consensual (WIP): Envisioned for a future update, the consensual process will enable agents to make joint decisions on task execution, similar to a team consensus in a meeting before proceeding.
Hierarchical (WIP): Also in the pipeline, this process will introduce a chain of command to task execution, where some agents may have the authority to prioritize tasks or delegate them, akin to a traditional corporate hierarchy. These additional processes, once implemented, will offer more nuanced and sophisticated ways for agents to interact and complete tasks, much like teams in complex organizational structures.
Defining a Sequential Process

Creating a sequential process in CrewAI is straightforward and reflects the simplicity of coordinating a team's efforts step by step. In this process the outcome of the previous task is sent into the next one as context that I should use to accomplish it's task

from crewai import Process

# Define a sequential process
sequential_process = Process.sequential
The Magic of Sequential Processes

The sequential process is where much of CrewAI's magic happens. It ensures that tasks are approached with the same thoughtful progression that a human team would use, fostering a natural and logical flow of work while passing on task outcome into the next.

Assigning Processes to a Crew

To assign a process to a crew, simply set it during the crew's creation. The process will dictate the crew's approach to task execution.

from crewai import Crew

# Create a crew with a sequential process
crew = Crew(agents=my_agents, tasks=my_tasks, process=sequential_process)
The Role of Processes in Teamwork

The process you choose for your crew is critical. It's what transforms a group of individual agents into a cohesive unit that can tackle complex projects with the precision and harmony you'd find in a team of skilled humans.

Conclusion

Processes bring structure and order to the CrewAI ecosystem, allowing agents to collaborate effectively and accomplish goals systematically. As CrewAI evolves, additional process types will be introduced to enhance the framework's versatility, much like a team that grows and adapts over time.
```

```
Delegation and Collaboration
In CrewAI, collaboration is the cornerstone of agent interaction. Agents are designed to work together by sharing information, requesting assistance, and combining their skills to complete tasks more efficiently.

Information Sharing: Agents can share findings and data amongst themselves to ensure all members are informed and can contribute effectively.
Task Assistance: If an agent encounters a task that requires additional expertise, it can seek the help of another agent with the necessary skill set.
Resource Allocation: Agents can share or allocate resources such as tools or processing power to optimize task execution.
Collaboration is embedded in the DNA of CrewAI, enabling a dynamic and adaptive approach to problem-solving.

Delegation: Dividing to Conquer

Delegation is the process by which an agent assigns a task to another agent, or just ask another agent, it's an intelligent decision-making process that enhances the crew's functionality. By default all agents can delegate work and ask questions, so if you want an agent to work alone make sure to set that option when initializing an Agent, this is useful to prevent deviations if the task is supposed to be straightforward.

Implementing Collaboration and Delegation

When setting up your crew, you'll define the roles and capabilities of each agent. CrewAI's infrastructure takes care of the rest, managing the complex interplay of agents as they work together.

Example Scenario:

Imagine a scenario where you have a researcher agent that gathers data and a writer agent that compiles reports. The writer can autonomously ask question or delegate more in depth research work depending on its needs as it tries to complete its task.

Conclusion

Collaboration and delegation are what transform a collection of AI agents into a unified, intelligent crew. With CrewAI, you have a framework that not only simplifies these interactions but also makes them more effective, paving the way for sophisticated AI systems that can tackle complex, multi-dimensional tasks.
```

```
Agent Tools
A tool in CrewAI is a function or capability that an agent can utilize to perform actions, gather information, or interact with external systems, behind the scenes tools are LangChain Tools. These tools can be as straightforward as a search function or as sophisticated as integrations with other chains or APIs.

Utility: Tools are designed to serve specific purposes, such as searching the web, analyzing data, or generating content.
Integration: Tools can be integrated into agents to extend their capabilities beyond their basic functions.
Customizability: Developers can create custom tools tailored to the specific needs of their agents or use pre-built LangChain ones available in the ecosystem.
Creating your own Tools

You can easily create your own tool using LangChain Tool Custom Tool Creation.

Example:

import json
import requests

from crewai import Agent
from langchain.tools import tool
from unstructured.partition.html import partition_html

class BrowserTools():
  @tool("Scrape website content")
  def scrape_website(website):
    """Useful to scrape a website content"""
    url = f"https://chrome.browserless.io/content?token={config('BROWSERLESS_API_KEY')}"
    payload = json.dumps({"url": website})
    headers = {
      'cache-control': 'no-cache',
      'content-type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    elements = partition_html(text=response.text)
    content = "\n\n".join([str(el) for el in elements])

    # Return only the first 5k characters
    return content[:5000]


# Create an agent and assign the scrapping tool
agent = Agent(
  role='Research Analyst',
  goal='Provide up-to-date market analysis',
  backstory='An expert analyst with a keen eye for market trends.',
  tools=[BrowserTools().scrape_website]
)
Using Existing Tools

Check LangChain Integration for a set of useful existing tools. To assign a tool to an agent, you'd provide it as part of the agent's properties during initialization.

from crewai import Agent
from langchain.agents import Tool
from langchain.utilities import GoogleSerperAPIWrapper

# Initialize SerpAPI tool with your API key
os.environ["OPENAI_API_KEY"] = "Your Key"
os.environ["SERPER_API_KEY"] = "Your Key"

search = GoogleSerperAPIWrapper()

# Create tool to be used by agent
serper_tool = Tool(
  name="Intermediate Answer",
  func=search.run,
  description="useful for when you need to ask with search",
)

# Create an agent and assign the search tool
agent = Agent(
  role='Research Analyst',
  goal='Provide up-to-date market analysis',
  backstory='An expert analyst with a keen eye for market trends.',
  tools=[serper_tool]
)
Tool Interaction

Tools enhance an agent's ability to perform tasks autonomously or in collaboration with other agents. For instance, an agent might use a search tool to gather information, then pass that data to another agent specialized in analysis.

Conclusion

Tools are vital components that expand the functionality of agents within the CrewAI framework. They enable agents to perform a wide range of actions and collaborate effectively with one another. As you build with CrewAI, consider the array of tools you can leverage to empower your agents and how they can be interwoven to create a robust AI ecosystem.
```

```
Customizing Agents
Customizing your AI agents is a cornerstone of creating an effective CrewAI team. Each agent can be tailored to fit the unique needs of your project, allowing for a dynamic and versatile AI workforce.

When you initialize an Agent, you can set various attributes that define its behavior and role within the Crew:

Role: The job title or function of the agent within your crew. This can be anything from 'Analyst' to 'Customer Service Rep'.
Goal: What the agent is aiming to achieve. Goals should be aligned with the agent's role and the overall objectives of the crew.
Backstory: A narrative that provides depth to the agent's character. This could include previous experience, motivations, or anything that adds context to their role.
Tools: The abilities or methods the agent uses to complete tasks. This could be as simple as a 'search' function or as complex as a custom-built analysis tool.
Understanding Tools in CrewAI

Tools in CrewAI are functions that empower agents to interact with the world around them. These can range from generic utilities like a search function to more complex ones like integrating with an external API. The integration with LangChain allows you to utilize a suite of ready-to-use tools such as Google Serper, which enables agents to perform web searches and gather data.

Customizing Agents and Tools

You can customize an agent by passing parameters when creating an instance. Each parameter tweaks how the agent behaves and interacts within the crew.

Customizing an agent's tools is particularly important. Tools define what an agent can do and how it interacts with tasks. For instance, if a task requires data analysis, assigning an agent with data-related tools would be optimal.

When initializing your agents, you can equip them with a set of tools that enable them to perform their roles more effectively:

from crewai import Agent
from langchain.agents import Tool
from langchain.utilities import GoogleSerperAPIWrapper

# Initialize SerpAPI tool with your API key
os.environ["OPENAI_API_KEY"] = "Your Key"
os.environ["SERPER_API_KEY"] = "Your Key"

search = GoogleSerperAPIWrapper()

# Create tool to be used by agent
serper_tool = Tool(
  name="Intermediate Answer",
  func=search.run,
  description="useful for when you need to ask with search",
)

# Create an agent and assign the search tool
agent = Agent(
  role='Research Analyst',
  goal='Provide up-to-date market analysis',
  backstory='An expert analyst with a keen eye for market trends.',
  tools=[serper_tool]
)
Delegation and Autonomy

One of the most powerful aspects of CrewAI agents is their ability to delegate tasks to one another. Each agent by default can delegate work or ask question to anyone in the crew, but you can disable that by setting allow_delegation to false, this is particularly useful for straightforward agents that should execute their tasks in isolation.

agent = Agent(
  role='Content Writer',
  goal='Write the most amazing content related to market trends an business.',
  backstory='An expert writer with many years of experience in market trends, stocks and all business related things.',
  allow_delegation=False
)
Conclusion

Customization is what makes CrewAI powerful. By adjusting the attributes of each agent, you can ensure that your AI team is well-equipped to handle the challenges you set for them. Remember, the more thought you put into your agents' roles, goals, backstories, and tools, the more nuanced and effective their interactions and task execution will be.
```

```
Creating Tasks
A Task in CrewAI is essentially a job or an assignment that an AI agent needs to complete. It's defined by what needs to be done and can include additional information like which agent should do it and what tools they might need.

Task Properties

Description: A clear, concise statement of what the task entails.
Agent: Optionally, you can specify which agent is responsible for the task. If not, the crew's process will determine who takes it on.
Tools: These are the functions or capabilities the agent can utilize to perform the task. They can be anything from simple actions like 'search' to more complex interactions with other agents or APIs.
Integrating Tools with Tasks

In CrewAI, tools are functions from the langchain toolkit that agents can use to interact with the world. These can be generic utilities or specialized functions designed for specific actions. When you assign tools to a task, they empower the agent to perform its duties more effectively.

Example of Creating a Task with Tools

from crewai import Task
from langchain.agents import Tool
from langchain.utilities import GoogleSerperAPIWrapper

# Initialize SerpAPI tool with your API key
os.environ["OPENAI_API_KEY"] = "Your Key"
os.environ["SERPER_API_KEY"] = "Your Key"

search = GoogleSerperAPIWrapper()

# Create tool to be used by agent
serper_tool = Tool(
  name="Intermediate Answer",
  func=search.run,
  description="useful for when you need to ask with search",
)

# Create a task with a description and the search tool
task = Task(
  description='Find and summarize the latest and most relevant news on AI',
  tools=[serper_tool]
)
When the task is executed by an agent, the tools specified in the task will override the agent's default tools. This means that for the duration of this task, the agent will use the search tool provided, even if it has other tools assigned to it.

Tool Override Mechanism

The ability to override an agent's tools with those specified in a task allows for greater flexibility. An agent might generally use a set of standard tools, but for certain tasks, you may want it to use a particular tool that is more suited to the task at hand.

Conclusion

Creating tasks with the right tools is crucial in CrewAI. It ensures that your agents are not only aware of what they need to do but are also equipped with the right functions to do it effectively. This feature underlines the flexibility and power of the CrewAI system, where tasks can be tailored with specific tools to achieve the best outcome.
```

```
Creating a Crew and kick it off
Get a crew working

Assembling a Crew in CrewAI is like casting characters for a play. Each agent you create is a cast member with a unique part to play. When your crew is assembled, you'll give the signal, and they'll spring into action, each performing their role in the grand scheme of your project.

Step 1: Assemble Your Agents

Start by creating your agents, each with its own role and backstory. These backstories add depth to the agents, influencing how they approach their tasks and interact with one another.

from crewai import Agent

# Create a researcher agent
researcher = Agent(
  role='Senior Researcher',
  goal='Discover groundbreaking technologies',
  verbose=True,
  backstory='A curious mind fascinated by cutting-edge innovation and the potential to change the world, you know everything about tech.'
)

# Create a writer agent
writer = Agent(
  role='Writer',
  goal='Craft compelling stories about tech discoveries',
  verbose=True,
  backstory='A creative soul who translates complex tech jargon into engaging narratives for the masses, you write using simple words in a friendly and inviting tone that does not sounds like AI.'
)
Step 2: Define the Tasks

Outline the tasks that your agents need to tackle. These tasks are their missions, the specific objectives they need to achieve.

from crewai import Task

# Task for the researcher
research_task = Task(
  description='Identify the next big trend in AI',
  agent=researcher  # Assigning the task to the researcher
)

# Task for the writer
write_task = Task(
  description='Write an article on AI advancements leveraging the research made.',
  agent=writer  # Assigning the task to the writer
)
Step 3: Form the Crew

Bring your agents together into a crew. This is where you define the process they'll follow to complete their tasks.

from crewai import Crew, Process

# Instantiate your crew
tech_crew = Crew(
  agents=[researcher, writer],
  tasks=[research_task, write_task],
  process=Process.sequential  # Tasks will be executed one after the other
)
Step 4: Kick It Off

With the crew formed and the stage set, it's time to start the show. Kick off the process and watch as your agents collaborate to achieve their goals.

# Begin the task execution
tech_crew.kickoff()
Conclusion

Creating a crew and setting it into motion is a straightforward process in CrewAI. With each agent playing their part and a clear set of tasks, your AI ensemble is ready to take on any challenge. Remember, the richness of their backstories and the clarity of their goals will greatly enhance their performance and the outcomes of their collaboration.
```


