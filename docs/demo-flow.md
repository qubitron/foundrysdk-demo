## Why you should use AI as a developer

Problem: I don't know where I can use AI, and what it's good at

Slide: Automation of tasks, especially things involving language

Problem: I don't understand the concepts of AI

Slide: models, prompts, agents, tools

## Getting started

Problem: too many options to choose from: models, cloud, dev tools, client libraries

Slide:
 - Microsoft is the best developer platform for building with AI, GitHub, VS Code and Azure all integrated into one streamlined experience
      - Everything you need included in the box with the Foundry resource & SDK: models, agents, observability, search
      - Models from popular providers, just change the model name in code
      - Customize with connectors to existing data, external services
      - Integrations into popular OSS frameworks: LangChain, MCP, A2A
 
Problems: a lot of setup steps and cloud provisioning required I can get coding
   - need to provision cloud services, setup authentication
   - time consuming build out application scaffolding 

Demo:
 - Start from ai.azure.com
 - Create a new project
    - This deploys a gpt-4o model
 - Open in VS Code
    -> show how it works for all 4 programming languages
 - Create an azd template, deploy it, share it with a coworker

Improvements shown:
 - Simplified resource provisioning: 
      - no longer need a hub, combined into the AI Services resource
      - authentication is now simpler, just need access to a single AI Services resource
      - no longer need to be a subscription owner, the azure ai project manager role allows you to grant users access
 - Simplified API
      - agents, models, evaluation all available on the same API endpoint
 - Easier transition to code: Open in VS Code streamlines transition from portal to working code
 - Easier to deploy a web app: azd init privisions an app template that connects to existing resources

## Optimizing models and prompts

Problem: difficult to prepare optimization pipeline to baseline & improve results

Demo:
 - Traces enable you to capture production traffic, user thumbs-up and thumbs-down for ranking (python script to generate dataset from kusto)
 - Evaluation enables you to experiment with prompts & models and compare before/after results
 - Fine-tuning enables you to get better cost/performance out of models (use OpenAI SDK)
 - One more thing: model router?

Improvements shown:
 - Tracing is integrated into the Foundry SDK, simply connect application insights add ```projects.telemetry.enable()```
   - At Build: application Insights connection simplifies authentication
 - Evaluation is now part of the AI Services resource
 - Fine-tuning: not sure what's new here?
 - Model router is new


## Adding context using Agents

Challenge: a lot of manual coding, prompt authoring to add context into your prompts

Slide: showing the steps & sample code to build a custom RAG app
   - docs here: https://learn.microsoft.com/en-us/azure/ai-foundry/tutorials/copilot-sdk-build-rag

Demo:
 - Use SDK code to create a vector store with markdown files uploaded
 - Create an agent with a file search tool for product search, bing search
 - 

Improvements: 
 - Agents service is now GA, with REST API documentation and support in Java & JavaScript
 - Agents is now part of the AI Services resource (same)
 - 

## Orchestrating complex workflows & actions

Challenge: how enable your agents to take action to provide even more value to users?

Demo:
 - Function calling for invoking local program functions, OpenAPI tool for calling APIs
 - Use semantic kernel for MCP servers?

Improvements:
 - automatic function calling
 - Is OpenAPI tool new?
 - MCP server support in semantic kernel

Challenge: need specialized agents for different task, one agent falls over if it has too many tools

Demo:
 - enable agents to call other agents
 - using semantic kernel for complex workflow orchestration


## Visibility into the production application

Problem: managing quality - how do I know it's doing what I want it to do, how do I catch issues?

Demo: start with local testing
 - Local agent evaluations for tool call accuracy, relevance, and intent resolution
   - TODO: groundedness still not available?
 - 

Problem: how do I keep quality high?

Demo: github actions prevents regressions from getting checked in

Problem: how do I know it's behaving well in production?

Demo: continuous evaluation with monitoring dashboards

Improvements:
 - Agent evaluations
 - GitHub actions for agents
 - Continuous evaluation API & monitoring dashboard