# AI Agent Research & City Guide

A Python-based project that demonstrates AI agent capabilities using LangChain and Claude AI models for research tasks and city guide generation with structured responses.

## Overview

This project showcases two AI agent implementations:

1. **Research Assistant** (`main.py`) - An AI agent that can answer research questions and return structured summaries
2. **City Guide Generator** (`city_capitals.py`) - An AI agent that provides comprehensive city guides including capitals, famous places, and activities

Both agents leverage Claude AI models through LangChain for intelligent, structured responses using Pydantic models.

## Features

- **AI-Powered Research**: Get concise summaries on any topic using Claude AI
- **Structured Responses**: Responses are automatically validated and formatted using Pydantic models
- **Tool Integration**: City guide agent includes a tool to fetch capital cities
- **Environment Configuration**: Support for API keys via `.env` file
- **Type Safety**: Full Python type hints and Pydantic validation

## Requirements

- Python 3.8+
- Anthropic API key

## Installation

1. **Clone or download the project**

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the project root
   - Add your Anthropic API key:
     ```
     ANTHROPIC_API_KEY=your_api_key_here
     ```

## Dependencies

- **langchain** - Framework for building AI agents
- **langchain-anthropic** - Anthropic/Claude integration
- **langchain-community** - Community tools and utilities
- **pydantic** - Data validation and serialization
- **python-dotenv** - Environment variable management
- **wikipedia** - Wikipedia API integration
- **duckduckgo-search** - Web search capability
- **langchain-openai** - OpenAI integration support

## Usage

### Research Assistant

Run the research assistant to answer questions about any topic:

```bash
python main.py
```

The agent will respond with a structured `ResearchResponse` containing:
- `summary` - A concise answer to the query
- `topic` - The topic being researched

### City Guide Generator

Run the city guide generator to get travel information:

```bash
python city_capitals.py
```

The agent will provide a structured `CityGuide` containing:
- `country` - The country name
- `capital` - The capital city
- `summary` - 1-2 line description
- `famous_places` - 4-6 notable landmarks or attractions
- `things_to_do` - 3-5 recommended activities

## Project Structure

```
AI Agent/
├── main.py                 # Research assistant agent
├── city_capitals.py        # City guide agent
├── requirements.txt        # Python dependencies
├── Readme                  # This file
└── .env                    # Environment variables (not included, create locally)
```

## Configuration

The project uses Claude Sonnet 4.5 by default. To change the model, edit the `llm` initialization:

```python
llm = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0)
```

## Customization

### Add Tools to Agents

To add more tools to the agents, use the `@tool` decorator:

```python
@tool
def my_tool(param: str) -> str:
    """Tool description."""
    return result
```

Then pass it to `create_agent`:

```python
agent = create_agent(
    model=llm,
    tools=[my_tool],
    ...
)
```

### Modify Response Structure

Update the Pydantic models to customize response fields:

```python
class CustomResponse(BaseModel):
    field1: str
    field2: list[str]
```

## Example Outputs

### Research Assistant
```
Java is a popular, object-oriented programming language that enables developers to write once and run anywhere...
```

### City Guide
```
London (UK) — The capital of England and gateway to the United Kingdom.
Famous places: Big Ben; Tower of London; Westminster Abbey; Buckingham Palace; Tower Bridge; St. Paul's Cathedral
Things to do: Visit museums; Explore markets; Watch West End shows; Ride the London Eye; Walk along the Thames
```

## Troubleshooting

- **API Key Error**: Ensure your `.env` file is in the project root and contains `ANTHROPIC_API_KEY`
- **Import Errors**: Run `pip install -r requirements.txt` to install all dependencies
- **Connection Issues**: Check your internet connection and Anthropic API status

## License

This project is provided as-is for educational and research purposes.

## Support

For issues or questions, refer to:
- [LangChain Documentation](https://python.langchain.com/)
- [Anthropic API Documentation](https://docs.anthropic.com/)
