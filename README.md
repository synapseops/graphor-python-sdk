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
from pathlib import Path

from graphor import Graphor

client = Graphor()  # Uses GRAPHOR_API_KEY env var

# Upload a document; it is parsed in the background
build = client.sources.ingest_file(
    file=Path("document.pdf"),
    method="agentic",  # Options: fast, balanced, accurate, agentic, auto
)

# Check the build
status = client.sources.get_build_status(build.build_id)
print(f"{status.file_name}: {status.status}")

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
build = client.sources.ingest_file(file=Path("report.pdf"))

# Upload from URL
source = client.sources.ingest_url(url="https://example.com/article")

# Upload from GitHub
source = client.sources.ingest_github(url="https://github.com/org/repo")

# Upload from YouTube
source = client.sources.ingest_youtube(url="https://youtube.com/watch?v=...")
```

**Supported formats:** PDF, DOCX, TXT, MD, HTML, CSV, XLSX, PNG, JPG, MP3, MP4, and more.

📖 [Full upload documentation](https://docs.graphorlm.com/sdk/sources/upload)

Large files work the same way: above 30 MiB, `ingest_file` sends the file in chunks that resume after a network error, then returns the same `build_id`. A large upload can take a while, and `timeout` applies to each request rather than to the whole upload.
### ⚙️ Process Documents

Reprocess documents with different OCR/parsing methods:

```python
# Reprocess with high-resolution parsing
source = client.sources.reprocess(
    file_id="<file_id>",
    method="balanced",  # Options: fast, balanced, accurate, agentic, auto
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

### 📁 Organize Sources in Folders

A folder is a `/`-separated path such as `Contracts/2026`; `""` (or `/`) is the top level. Every source carries its `folder`. Names stay unique across the project, whatever the folder.

```python
from pathlib import Path

# Upload into a folder; a folder that does not exist is created
build = client.sources.ingest_file(file=Path("lease.pdf"), folder="Contracts/2026")
client.sources.ingest_url(url="https://example.com/terms", folder="Contracts")

# List a folder and everything below it, only the folder itself, or the top level
sources = client.sources.list(folder="Contracts")
sources = client.sources.list(folder="Contracts", recursive=False)
sources = client.sources.list(folder="/")

# Ask, extract or retrieve within folders (every source at or below each one)
response = client.sources.ask(question="When do the leases end?", folders=["Contracts"])

# Manage folders
client.sources.list_folders()  # every folder, sorted, with `truncated`
client.sources.create_folder(folder="Contracts/2027")  # safe to repeat
client.sources.move(file_ids=["<file_id>"], folder="Contracts/2027")  # "" moves to the top level
client.sources.rename_folder(folder="Contracts/2027", new_folder="Archive/2027")

# Each of these is a separate example
client.sources.remove_folder(folder="Archive")  # its content moves to the folder above
client.sources.create_folder(folder="Drafts")
client.sources.delete_folder(folder="Drafts")  # only an empty folder
```

An empty `folders` list is no folder scope: the call covers what `file_ids` names, or the whole project. A folder that holds no source refuses the call with `400 chat.folder_scope_empty`.

`rename_folder`, `remove_folder` and `delete_folder` are not safe to repeat blindly: after a `503`, a timeout or a lost answer the change may have been saved. They never retry on their own, whatever `max_retries` says; call `list_folders()` before repeating one by hand. Only a `404` whose `code` is `folder.not_found` may mean an earlier call worked.

The API echoes every folder filter or scope it applies. When a call sends one and the answer does not echo it, the API did not apply it (it does not support folders), and the SDK raises `graphor.FolderScopeNotAppliedError` instead of returning a result that may cover more sources than were asked for. The same error is raised when the API does not offer a folder method. The check runs whenever the result is parsed, also through `.with_raw_response` and `.with_streaming_response`, but not on the raw bytes, nor on a `.parse(to=...)` into `httpx.Response`, `str` or `bytes`. A large upload with `folder` stops before sending any byte when the upload session does not confirm the folder, or when the API offers no upload sessions. With `folders`, a failure that `ask` or `extract` stream after the answer started raises the error for its status. A `folders` that is not a list is refused before any request.

## Async Usage

Use `AsyncGraphor` for async/await support:

```python
import asyncio
from graphor import AsyncGraphor

async def main():
    client = AsyncGraphor()
    
    # All methods support await
    build = await client.sources.ingest_file(file=("notes.txt", b"content"))
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

## File uploads

Request parameters that correspond to file uploads can be passed as `bytes`, or a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) instance or a tuple of `(filename, contents, media type)`.

```python
from pathlib import Path
from graphor import Graphor

client = Graphor()

client.sources.ingest_file(
    file=Path("/path/to/file"),
)
```

The async client uses the exact same interface. If you pass a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) instance, the file contents will be read asynchronously automatically.

Files above 30 MiB are uploaded in chunks, so a path or an open file is never read into memory whole. If the upload cannot finish, `ingest_file` raises `graphor.UploadError`; when its `build_id` is set, the file was sent and its build may still complete, so check that build before uploading again.

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
| N/A | `FolderScopeNotAppliedError` (a folder parameter the API did not apply) |

## Configuration

### Retries

Requests are not retried by default (`max_retries=0`). With retries enabled, connection errors, 408, 409, 429 and 5xx responses are retried with a short exponential backoff. Large file uploads retry their own chunks regardless of this setting.

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
client.with_options(timeout=300.0).sources.reprocess(
    file_id="<file_id>",
    method="agentic",
)
```

## Complete Example

```python
from pathlib import Path
from graphor import Graphor

client = Graphor()

# 1. Upload a document, parsed in the background
build = client.sources.ingest_file(file=Path("contract.pdf"), method="balanced")

# 2. Check the build
status = client.sources.get_build_status(build.build_id)
print(f"✅ {status.file_name}: {status.status}")
source = status

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

## MCP Server

Use the Graphor MCP Server to enable AI assistants to interact with this API, allowing them to explore endpoints, make test requests, and use documentation to help integrate this SDK into your application.

[![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=graphor-mcp&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsImdyYXBob3ItbWNwIl0sImVudiI6eyJHUkFQSE9SX0FQSV9LRVkiOiJNeSBBUEkgS2V5In19)

Or manually add it to your MCP client's configuration:

```json
{
  "mcpServers": {
    "graphor_api": {
      "command": "npx",
      "args": ["-y", "graphor-mcp@latest"],
      "env": {
        "GRAPHOR_API_KEY": "grlm_your_api_key_here"
      }
    }
  }
}
```

> Note: You may need to set environment variables in your MCP client.

### Remote MCP Server (Web Apps & Agentic Workflows)

For web-based AI clients (e.g. [Claude.ai](https://claude.ai)) or agentic frameworks (e.g. LangChain, CrewAI) that cannot run local `npx` processes, use the hosted remote MCP server. Authentication is handled via **OAuth** — a browser window will open for you to log in.

```
https://mcp.graphor.workers.dev/sse
```

**Web apps (e.g. Claude.ai)** — in Claude.ai, go to **Settings > Connectors > Add custom connector**, fill in the name and the remote MCP server URL. You will be redirected to log in through the OAuth flow:

```
https://mcp.graphor.workers.dev/sse
```

**Desktop clients (e.g. Claude Desktop)** — use [`mcp-remote`](https://www.npmjs.com/package/mcp-remote) as a local proxy:

```json
{
  "mcpServers": {
    "graphor_api": {
      "command": "npx",
      "args": ["mcp-remote", "https://mcp.graphor.workers.dev/sse"]
    }
  }
}
```

**Agentic workflows (e.g. LangChain)** — connect via SSE transport:

```python
from langchain_mcp_adapters.client import MultiServerMCPClient

async with MultiServerMCPClient(
    {
        "graphor": {
            "url": "https://mcp.graphor.workers.dev/sse",
            "transport": "sse",
        }
    }
) as client:
    tools = client.get_tools()
    # Use tools with your LangChain agent
```

See the [MCP Server README](https://github.com/synapseops/graphor-mcp-server) for more details.

## API Reference

### Sources

| Method | Description | Docs |
|--------|-------------|------|
| `sources.ingest_file()` | Upload a local file, of any size up to the limit | [📖](https://docs.graphorlm.com/sdk/sources/upload#upload-a-file) |
| `sources.ingest_url()` | Upload from web URL | [📖](https://docs.graphorlm.com/sdk/sources/upload#upload-from-url) |
| `sources.ingest_github()` | Upload from GitHub | [📖](https://docs.graphorlm.com/sdk/sources/upload#upload-from-github) |
| `sources.ingest_youtube()` | Upload from YouTube | [📖](https://docs.graphorlm.com/sdk/sources/upload#upload-from-youtube) |
| `sources.reprocess()` | Reprocess with different method | [📖](https://docs.graphorlm.com/sdk/sources/process) |
| `sources.list()` | List all sources | [📖](https://docs.graphorlm.com/sdk/sources/list) |
| `sources.delete()` | Delete a source | [📖](https://docs.graphorlm.com/sdk/sources/delete) |
| `sources.load_elements()` | Get parsed elements | [📖](https://docs.graphorlm.com/sdk/sources/list-elements) |
| `sources.list_folders()` | List every folder | |
| `sources.create_folder()` | Create a folder | |
| `sources.rename_folder()` | Rename or move a folder | |
| `sources.remove_folder()` | Remove a folder, keeping its content | |
| `sources.delete_folder()` | Delete an empty folder | |
| `sources.move()` | Move sources to a folder | |

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
