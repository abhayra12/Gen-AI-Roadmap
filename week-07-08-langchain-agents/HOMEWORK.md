# 📝 Homework Assignment - Week 7-8

**Module:** LangChain, Agents & Advanced RAG  
**Due:** End of Week 8  
**Points:** 100

---

## 🎯 Assignment: Multi-Agent Manufacturing Data Analyst

Build an autonomous agent system that analyzes manufacturing data, identifies issues, and recommends actions.

---

## 📊 System Components

### Required Agents
1. **Data Analyst Agent**: Analyzes production data
2. **Quality Inspector Agent**: Identifies defects and patterns
3. **Maintenance Agent**: Predicts equipment failures
4. **Report Generator Agent**: Creates executive summaries

### Required Tools
- Database query tool
- Statistical analysis tool
- Visualization generator
- Report formatter
- Web search (for industry standards)

---

## 📋 Task Breakdown

### Part 1: LangGraph Workflow (30 points)
- Design agent state graph
- Implement conditional routing
- Add error handling
- Implement state persistence

### Part 2: Custom Tools (25 points)
- Create 5+ custom tools
- Implement tool calling
- Add input validation
- Handle tool errors

### Part 3: Agent Implementation (25 points)
- Build 4 specialized agents
- Implement ReAct pattern
- Add memory/context
- Test autonomously

### Part 4: Integration (10 points)
- Connect all agents
- Test end-to-end workflow
- Handle edge cases
- Optimize performance

### Part 5: Demo (10 points)
- Interactive interface
- Show agent reasoning
- Display intermediate steps
- Document usage

---

## 💡 Implementation Example

### LangGraph Workflow
```python
from langgraph.graph import StateGraph, END

class AgentState(TypedDict):
    input: str
    intermediate_steps: List
    final_answer: str

workflow = StateGraph(AgentState)

workflow.add_node("analyzer", data_analyst_agent)
workflow.add_node("inspector", quality_inspector_agent)
workflow.add_node("maintainer", maintenance_agent)
workflow.add_node("reporter", report_generator_agent)

workflow.add_conditional_edges(
    "analyzer",
    route_next_agent,
    {
        "inspect": "inspector",
        "maintain": "maintainer",
        "report": "reporter"
    }
)

workflow.set_entry_point("analyzer")
app = workflow.compile()
```

### Custom Tool
```python
from langchain.tools import BaseTool

class DataAnalysisTool(BaseTool):
    name = "data_analyzer"
    description = "Analyzes manufacturing data for patterns and anomalies"
    
    def _run(self, query: str) -> str:
        # Implement analysis logic
        return analysis_result
```

---

## 🚀 Bonus Challenges (+10 points each)

1. **Human-in-the-Loop**: Pause for approval
2. **Multi-modal**: Process images and text
3. **Streaming**: Real-time agent output
4. **Evaluation**: Auto-evaluate agent performance
5. **Deployment**: Deploy as web service

---

## 📦 Submission Structure

```
homework/week-07-08/
├── README.md
├── multi_agent_system.ipynb
├── requirements.txt
├── src/
│   ├── agents/
│   │   ├── analyst.py
│   │   ├── inspector.py
│   │   ├── maintainer.py
│   │   └── reporter.py
│   ├── tools/
│   │   ├── database_tool.py
│   │   ├── analysis_tool.py
│   │   └── viz_tool.py
│   └── workflow.py
├── app.py
└── reports/
    ├── agent_evaluation.md
    └── demo_scenarios/
```

---

## ✅ Submission Checklist

- [ ] All 4 agents implemented
- [ ] 5+ custom tools working
- [ ] LangGraph workflow functional
- [ ] End-to-end demo ready
- [ ] Code documented
- [ ] README comprehensive
- [ ] Committed to GitHub

---

<div align="center">
Week 7-8 Homework | Multi-Agent System | Build autonomous AI! 🤖
</div>
