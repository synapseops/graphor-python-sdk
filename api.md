# Sources

Types:

```python
from graphor.types import (
    PublicSource,
    SourceListResponse,
    SourceDeleteResponse,
    SourceAskResponse,
    SourceExtractResponse,
    SourceRetrieveChunksResponse,
)
```

Methods:

- <code title="get /sources">client.sources.<a href="./src/graphor/resources/sources.py">list</a>(\*\*<a href="src/graphor/types/source_list_params.py">params</a>) -> <a href="./src/graphor/types/source_list_response.py">SourceListResponse</a></code>
- <code title="delete /sources/delete">client.sources.<a href="./src/graphor/resources/sources.py">delete</a>(\*\*<a href="src/graphor/types/source_delete_params.py">params</a>) -> <a href="./src/graphor/types/source_delete_response.py">SourceDeleteResponse</a></code>
- <code title="post /sources/ask-sources">client.sources.<a href="./src/graphor/resources/sources.py">ask</a>(\*\*<a href="src/graphor/types/source_ask_params.py">params</a>) -> <a href="./src/graphor/types/source_ask_response.py">SourceAskResponse</a></code>
- <code title="post /sources/run-extraction">client.sources.<a href="./src/graphor/resources/sources.py">extract</a>(\*\*<a href="src/graphor/types/source_extract_params.py">params</a>) -> <a href="./src/graphor/types/source_extract_response.py">SourceExtractResponse</a></code>
- <code title="post /sources/prebuilt-rag">client.sources.<a href="./src/graphor/resources/sources.py">retrieve_chunks</a>(\*\*<a href="src/graphor/types/source_retrieve_chunks_params.py">params</a>) -> <a href="./src/graphor/types/source_retrieve_chunks_response.py">SourceRetrieveChunksResponse</a></code>
