# 📝 Homework Assignment - Week 7-8: Build a "Smart Maintenance Assistant" Agent

**Module:** LangChain, Agents & Advanced RAG  
**Due:** End of Week 8  
**Points:** 100

---

## 🎯 Assignment Overview

Your mission is to build a single, powerful AI agent that acts as a "Smart Maintenance Assistant" for a manufacturing plant. This agent will use LangChain tools to diagnose problems, check inventory, and provide step-by-step guidance based on Standard Operating Procedures (SOPs).

This project will synthesize the key concepts from Week 7-8, including building agents, creating custom tools, and implementing governance.

---

## 🛠️ Core Requirements

### 1. The Agent (40 points) - *Based on Notebook 12*

- **Build a ReAct Agent**: Using `initialize_agent` with `AgentType.ZERO_SHOT_REACT_DESCRIPTION`, create an agent that can reason and use tools to answer maintenance queries.
- **Agent Persona**: The agent's system prompt should define it as a "Manufacturing Maintenance Assistant" for the Pune plant. It must be helpful, concise, and prioritize safety.
- **Verbose Logging**: The agent must be initialized with `verbose=True` to show its reasoning steps.

### 2. Custom Tools (40 points) - *Based on Notebooks 12 & 13*

Create three specific tools that the agent will use. These tools will simulate looking up information in a manufacturing environment.

1.  **`SparePartsInventoryTool`**:
    -   **Input**: A string query (e.g., "bearing for Press 14").
    -   **Functionality**: Simulates checking an inventory database. It should have a hardcoded Python dictionary of parts (e.g., bearings, seals, sensors for "Press 14" and "CNC-03").
    -   **Output**: A string indicating the stock count and location (e.g., "Found 12 units of SKF-22210E in Warehouse B-7").

2.  **`MaintenanceHistoryTool`**:
    -   **Input**: An equipment ID string (e.g., "Press 14").
    -   **Functionality**: Simulates looking up past maintenance events. It should have a hardcoded dictionary of past incidents.
    -   **Output**: A string summarizing the last 2-3 maintenance events for that equipment (e.g., "On 2023-09-30, replaced bearing due to vibration.").

3.  **`StandardProcedureTool`**:
    -   **Input**: A procedure name string (e.g., "bearing replacement").
    -   **Functionality**: Simulates looking up an SOP. It should have a hardcoded dictionary of procedures.
    -   **Output**: A string containing the step-by-step SOP, which **must** include safety warnings (e.g., "SOP-122: 1. SAFETY: Perform lockout/tagout...").

### 3. Governance & Auditing (20 points) - *Based on Notebook 12*

- **Capture Reasoning**: After the agent runs, extract the `intermediate_steps` from the response.
- **Create a Governance Log**: Create a structured JSON log entry for each agent run. This log must contain:
    -   `timestamp`: The time of the request.
    -   `request_id`: A unique ID for the request (e.g., a hash of the question).
    -   `question`: The original user query.
    -   `reasoning_trace`: A formatted list of the agent's `intermediate_steps` (tool, input, output).
    -   `final_answer`: The agent's final response.
    -   `governance_checks`: A dictionary with booleans for `contains_safety_info` and `contains_sop_reference`.
- **Save the Log**: Append the JSON log entry to a file named `agent_runs.jsonl`.

---

## 🚀 Example Scenario

**User Query**: `"Press 14 is failing its vibration test. Do we have bearings in stock and what are the first steps according to the SOP?"`

**Expected Agent Behavior**:

1.  **Thought**: "I need to check the maintenance history for 'Press 14', look up 'bearings' in the inventory, and find the SOP for 'vibration test' or 'bearing replacement'."
2.  **Action**: Calls `MaintenanceHistoryTool` with `equipment='Press 14'`.
3.  **Action**: Calls `SparePartsInventoryTool` with `query='bearing for Press 14'`.
4.  **Action**: Calls `StandardProcedureTool` with `procedure_type='vibration test'`.
5.  **Thought**: "I have all the information. The history shows a past bearing replacement. We have bearings in stock. The SOP gives clear steps."
6.  **Final Answer**: The agent synthesizes the information into a helpful, multi-part answer that includes the stock status and the initial SOP steps, including safety warnings.

---

## 📦 Submission Structure

Your submission should be a single Jupyter Notebook named `homework_week_07_08.ipynb`.

The notebook should be organized with Markdown headings:
1.  **Part 1: Tool Implementation**: Define your three custom tool functions here.
2.  **Part 2: Agent Initialization**: Set up the `tools` list and initialize your ReAct agent.
3.  **Part 3: Agent Execution**: Define the user query and run the agent.
4.  **Part 4: Governance Logging**: Write the code to process the agent's response and create/save the JSON governance log.

---

## ✅ Submission Checklist

- [ ] The notebook is named `homework_week_07_08.ipynb`.
- [ ] All three custom tools are implemented with hardcoded data.
- [ ] The agent is a `ZERO_SHOT_REACT_DESCRIPTION` type and runs with `verbose=True`.
- [ ] The agent successfully uses at least two tools to answer the example query.
- [ ] The governance log is created in the specified JSON format and saved to `agent_runs.jsonl`.
- [ ] The final answer from the agent is helpful and includes safety information from the SOP tool.

---

<div align="center">
Good luck, and build a safe and effective AI assistant! 🤖
</div>