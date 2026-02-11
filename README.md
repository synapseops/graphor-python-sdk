# Graphor Python SDK

[![PyPI version](https://img.shields.io/pypi/v/graphor.svg?label=pypi%20(stable))](https://pypi.org/project/graphor/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

The official Python SDK for the [Graphor](https://graphorlm.com) API. Build intelligent document applications with ease.

**Features:**
- 📄 **Document Ingestion** — Upload files, web pages, GitHub repos, and YouTube videos
- 💬 **Document Chat** — Ask questions with conversational memory
- 📊 **Structured Extraction** — Extract data using JSON Schema
- 🔍 **Semantic Search** — Retrieve relevant chunks for custom RAG pipelines
- ⚡ **Async Support** — Full async/await support with `AsyncGraphor`
- 🔒 **Type Safety** — Complete type definitions for all params and responses

## MCP Server

Use the Graphor MCP Server to enable AI assistants to interact with this API, allowing them to explore endpoints, make test requests, and use documentation to help integrate this SDK into your application.

[![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=graphor-mc&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsImdyYXBob3ItbWMiXSwiZW52Ijp7IkdSQVBIT1JfQVBJX0tFWSI6Ik15IEFQSSBLZXkifX0)
[![Install in VS Code](https://img.shields.io/badge/_-Add_to_VS_Code-blue?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PHBhdGggZmlsbD0iI0VFRSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMzAuMjM1IDM5Ljg4NGEyLjQ5MSAyLjQ5MSAwIDAgMS0xLjc4MS0uNzNMMTIuNyAyNC43OGwtMy40NiAyLjYyNC0zLjQwNiAyLjU4MmExLjY2NSAxLjY2NSAwIDAgMS0xLjA4Mi4zMzggMS42NjQgMS42NjQgMCAwIDEtMS4wNDYtLjQzMWwtMi4yLTJhMS42NjYgMS42NjYgMCAwIDEgMC0yLjQ2M0w3LjQ1OCAyMCA0LjY3IDE3LjQ1MyAxLjUwNyAxNC41N2ExLjY2NSAxLjY2NSAwIDAgMSAwLTIuNDYzbDIuMi0yYTEuNjY1IDEuNjY1IDAgMCAxIDIuMTMtLjA5N2w2Ljg2MyA1LjIwOUwyOC40NTIuODQ0YTIuNDg4IDIuNDg4IDAgMCAxIDEuODQxLS43MjljLjM1MS4wMDkuNjk5LjA5MSAxLjAxOS4yNDVsOC4yMzYgMy45NjFhMi41IDIuNSAwIDAgMSAxLjQxNSAyLjI1M3YuMDk5LS4wNDVWMzMuMzd2LS4wNDUuMDk1YTIuNTAxIDIuNTAxIDAgMCAxLTEuNDE2IDIuMjU3bC04LjIzNSAzLjk2MWEyLjQ5MiAyLjQ5MiAwIDAgMS0xLjA3Ny4yNDZabS43MTYtMjguOTQ3LTExLjk0OCA5LjA2MiAxMS45NTIgOS4wNjUtLjAwNC0xOC4xMjdaIi8+PC9zdmc+)](https://vscode.stainless.com/mcp/%7B%22name%22%3A%22graphor-mc%22%2C%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22graphor-mc%22%5D%2C%22env%22%3A%7B%22GRAPHOR_API_KEY%22%3A%22My%20API%20Key%22%7D%7D)

> Note: You may need to set environment variables in your MCP client.

## Documentation

📚 **Full documentation**: [docs.graphorlm.com/sdk/overview](https://docs.graphorlm.com/sdk/overview)

## Installation

```bash
pip install graphor
```

For better async performance with aiohttp:

```bash
pip install graphor[aiohttp]
```

## Quick Start

```python
from graphor import Graphor

client = Graphor()  # Uses GRAPHOR_API_KEY env var

# Upload a document
source = client.sources.upload(file=open("document.pdf", "rb"))
print(f"Uploaded: {source.file_name}")

# Ask questions about your documents
response = client.sources.ask(question="What are the main topics?")
print(f"Answer: {response.answer}")
```

## Authentication

Set your API key as an environment variable (recommended):

```bash
export GRAPHOR_API_KEY="grlm_your_api_key_here"
```

```python
from graphor import Graphor

client = Graphor()  # Automatically uses GRAPHOR_API_KEY
```

Or pass it directly:

```python
client = Graphor(api_key="grlm_your_api_key_here")
```

## Core Features

### 📄 Upload Documents

Upload files, web pages, GitHub repositories, or YouTube videos:

```python
from pathlib import Path
from graphor import Graphor

client = Graphor()

# Upload a local file
source = client.sources.upload(file=Path("report.pdf"))

# Upload from URL
source = client.sources.upload_url(url="https://example.com/article")

# Upload from GitHub
source = client.sources.upload_github(url="https://github.com/org/repo")

# Upload from YouTube
source = client.sources.upload_youtube(url="https://youtube.com/watch?v=...")
```

**Supported formats:** PDF, DOCX, TXT, MD, HTML, CSV, XLSX, PNG, JPG, MP3, MP4, and more.

📖 [Full upload documentation](https://docs.graphorlm.com/sdk/sources/upload)

Certain errors are automatically retried 0 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.
### ⚙️ Process Documents

Reprocess documents with different OCR/parsing methods:

```python
# Reprocess with high-resolution parsing
source = client.sources.parse(
    file_name="document.pdf",
    partition_method="hi_res"  # Options: basic, hi_res, hi_res_ft, mai, graphorlm
)
```

📖 [Full processing documentation](https://docs.graphorlm.com/sdk/sources/process)

### 💬 Chat with Documents

Ask questions about your documents with conversational memory:

```python
# Ask a question
response = client.sources.ask(
    question="What are the key findings?"
)
print(response.answer)

# Follow-up question (maintains context)
follow_up = client.sources.ask(
    question="Can you elaborate on the first point?",
    conversation_id=response.conversation_id
)
print(follow_up.answer)

# Scope to specific documents
response = client.sources.ask(
    question="Compare these two reports",
    file_names=["report-2023.pdf", "report-2024.pdf"]
)
```

📖 [Full chat documentation](https://docs.graphorlm.com/sdk/chat)

### 📊 Extract Structured Data

Extract structured information using JSON Schema:

```python
result = client.sources.extract(
    file_names=["invoice.pdf"],
    user_instruction="Extract invoice details",
    output_schema={
        "type": "object",
        "properties": {
            "invoice_number": {"type": "string"},
            "total_amount": {"type": "number"},
            "line_items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "description": {"type": "string"},
                        "amount": {"type": "number"}
                    }
                }
            }
        }
    }
)

print(result.structured_output)
# {"invoice_number": "INV-001", "total_amount": 1500.00, "line_items": [...]}
```

📖 [Full extraction documentation](https://docs.graphorlm.com/sdk/extract)

### 🔍 Retrieve Chunks (Prebuilt RAG)

Build custom RAG pipelines with semantic search:

```python
# Retrieve relevant chunks
result = client.sources.retrieve_chunks(
    query="What are the payment terms?"
)

for chunk in result.chunks:
    print(f"[{chunk.file_name}, Page {chunk.page_number}]")
    print(f"Score: {chunk.score:.2f}")
    print(chunk.text)
    print("---")

# Use with your preferred LLM
context = "\n".join([c.text for c in result.chunks])
# Pass context to OpenAI, Anthropic, etc.
```

📖 [Full RAG documentation](https://docs.graphorlm.com/sdk/prebuilt-rag)

### 📋 Manage Sources

List, inspect, and delete documents:

```python
# List all sources
sources = client.sources.list()
for source in sources:
    print(f"{source.file_name}: {source.status}")

# Get document elements
elements = client.sources.load_elements(
    file_name="document.pdf",
    page=1,
    page_size=50
)

# Delete a source
result = client.sources.delete(file_name="document.pdf")
```

## Async Usage

Use `AsyncGraphor` for async/await support:

```python
import asyncio
from graphor import AsyncGraphor

async def main():
    client = AsyncGraphor()
    
    # All methods support await
    source = await client.sources.upload(file=b"content")
    response = await client.sources.ask(question="Summarize this document")
    
    print(response.answer)

asyncio.run(main())
```

### With aiohttp (Better Concurrency)

```python
from graphor import AsyncGraphor, DefaultAioHttpClient

async def main():
    async with AsyncGraphor(http_client=DefaultAioHttpClient()) as client:
        sources = await client.sources.list()
        print(f"Found {len(sources)} sources")

asyncio.run(main())
```

## Error Handling

```python
import graphor
from graphor import Graphor

client = Graphor()

try:
    response = client.sources.ask(question="What is this about?")
except graphor.AuthenticationError:
    print("Invalid API key")
except graphor.NotFoundError:
    print("Resource not found")
except graphor.RateLimitError:
    print("Rate limited - back off and retry")
except graphor.APIConnectionError:
    print("Network error")
except graphor.APIStatusError as e:
    print(f"API error: {e.status_code}")
```

| Status Code | Error Type |
|-------------|------------|
| 400 | `BadRequestError` |
| 401 | `AuthenticationError` |
| 403 | `PermissionDeniedError` |
| 404 | `NotFoundError` |
| 422 | `UnprocessableEntityError` |
| 429 | `RateLimitError` |
| ≥500 | `InternalServerError` |
| N/A | `APIConnectionError` |

## Configuration

### Retries

Requests are automatically retried twice with exponential backoff:

```python
# Configure default retries
client = Graphor(max_retries=5)

# Or per-request
client.with_options(max_retries=3).sources.ask(question="...")
```

### Timeouts

Default timeout is 60 seconds:

```python
# Configure default timeout
client = Graphor(timeout=120.0)

# Or per-request
client.with_options(timeout=300.0).sources.parse(
    file_name="large-document.pdf",
    partition_method="graphorlm"
)
```

## Complete Example

```python
from pathlib import Path
from graphor import Graphor

client = Graphor()

# 1. Upload a document
source = client.sources.upload(file=Path("contract.pdf"))
print(f"✅ Uploaded: {source.file_name}")

# 2. Process with advanced parsing
processed = client.sources.parse(
    file_name=source.file_name,
    partition_method="hi_res"
)
print(f"✅ Processed: {processed.status}")

# 3. Ask questions
response = client.sources.ask(
    question="What are the key terms of this contract?",
    file_names=[source.file_name]
)
print(f"📝 Answer: {response.answer}")

# 4. Extract structured data
extracted = client.sources.extract(
    file_names=[source.file_name],
    user_instruction="Extract contract details",
    output_schema={
        "type": "object",
        "properties": {
            "parties": {"type": "array", "items": {"type": "string"}},
            "effective_date": {"type": "string"},
            "termination_date": {"type": "string"},
            "total_value": {"type": "number"}
        }
    }
)
print(f"📊 Extracted: {extracted.structured_output}")

# 5. Build custom RAG
chunks = client.sources.retrieve_chunks(
    query="payment obligations",
    file_names=[source.file_name]
)
print(f"🔍 Found {chunks.total} relevant chunks")
```

## API Reference

### Sources

| Method | Description | Docs |
|--------|-------------|------|
| `sources.upload()` | Upload a local file | [📖](https://docs.graphorlm.com/sdk/sources/upload#upload-a-file) |
| `sources.upload_url()` | Upload from web URL | [📖](https://docs.graphorlm.com/sdk/sources/upload#upload-from-url) |
| `sources.upload_github()` | Upload from GitHub | [📖](https://docs.graphorlm.com/sdk/sources/upload#upload-from-github) |
| `sources.upload_youtube()` | Upload from YouTube | [📖](https://docs.graphorlm.com/sdk/sources/upload#upload-from-youtube) |
| `sources.parse()` | Reprocess with different method | [📖](https://docs.graphorlm.com/sdk/sources/process) |
| `sources.list()` | List all sources | [📖](https://docs.graphorlm.com/sdk/sources/list) |
| `sources.delete()` | Delete a source | [📖](https://docs.graphorlm.com/sdk/sources/delete) |
| `sources.load_elements()` | Get parsed elements | [📖](https://docs.graphorlm.com/sdk/sources/list-elements) |

### Chat & AI

| Method | Description | Docs |
|--------|-------------|------|
| `sources.ask()` | Ask questions about documents | [📖](https://docs.graphorlm.com/sdk/chat) |
| `sources.extract()` | Extract structured data | [📖](https://docs.graphorlm.com/sdk/extract) |
| `sources.retrieve_chunks()` | Retrieve chunks for RAG | [📖](https://docs.graphorlm.com/sdk/prebuilt-rag) |

## Requirements

- Python 3.9+

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](./LICENSE) for details.

## Links

- 📚 [Documentation](https://docs.graphorlm.com/sdk/overview)
- 🐛 [Issue Tracker](https://github.com/synapseops/graphor-python-sdk/issues)
- 📦 [PyPI](https://pypi.org/project/graphor/)
- 🏠 [Graphor](https://graphorlm.com)
