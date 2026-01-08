# Sources

Types:

```python
from graphor.types import (
    PartitionMethod,
    PublicSource,
    SourceListResponse,
    SourceDeleteResponse,
    SourceAskResponse,
    SourceExtractResponse,
    SourceLoadElementsResponse,
    SourceRetrieveChunksResponse,
)
```

Methods:

- <code title="get /sources">client.sources.<a href="./src/graphor/resources/sources.py">list</a>() -> <a href="./src/graphor/types/source_list_response.py">SourceListResponse</a></code>
- <code title="delete /sources/delete">client.sources.<a href="./src/graphor/resources/sources.py">delete</a>(\*\*<a href="src/graphor/types/source_delete_params.py">params</a>) -> <a href="./src/graphor/types/source_delete_response.py">SourceDeleteResponse</a></code>
- <code title="post /sources/ask-sources">client.sources.<a href="./src/graphor/resources/sources.py">ask</a>(\*\*<a href="src/graphor/types/source_ask_params.py">params</a>) -> <a href="./src/graphor/types/source_ask_response.py">SourceAskResponse</a></code>
- <code title="post /sources/run-extraction">client.sources.<a href="./src/graphor/resources/sources.py">extract</a>(\*\*<a href="src/graphor/types/source_extract_params.py">params</a>) -> <a href="./src/graphor/types/source_extract_response.py">SourceExtractResponse</a></code>
- <code title="post /sources/elements">client.sources.<a href="./src/graphor/resources/sources.py">load_elements</a>(\*\*<a href="src/graphor/types/source_load_elements_params.py">params</a>) -> <a href="./src/graphor/types/source_load_elements_response.py">SourceLoadElementsResponse</a></code>
- <code title="post /sources/process">client.sources.<a href="./src/graphor/resources/sources.py">parse</a>(\*\*<a href="src/graphor/types/source_parse_params.py">params</a>) -> <a href="./src/graphor/types/public_source.py">PublicSource</a></code>
- <code title="post /sources/prebuilt-rag">client.sources.<a href="./src/graphor/resources/sources.py">retrieve_chunks</a>(\*\*<a href="src/graphor/types/source_retrieve_chunks_params.py">params</a>) -> <a href="./src/graphor/types/source_retrieve_chunks_response.py">SourceRetrieveChunksResponse</a></code>
- <code title="post /sources/upload">client.sources.<a href="./src/graphor/resources/sources.py">upload</a>(\*\*<a href="src/graphor/types/source_upload_params.py">params</a>) -> <a href="./src/graphor/types/public_source.py">PublicSource</a></code>
- <code title="post /sources/upload-github-source">client.sources.<a href="./src/graphor/resources/sources.py">upload_github</a>(\*\*<a href="src/graphor/types/source_upload_github_params.py">params</a>) -> <a href="./src/graphor/types/public_source.py">PublicSource</a></code>
- <code title="post /sources/upload-url-source">client.sources.<a href="./src/graphor/resources/sources.py">upload_url</a>(\*\*<a href="src/graphor/types/source_upload_url_params.py">params</a>) -> <a href="./src/graphor/types/public_source.py">PublicSource</a></code>
- <code title="post /sources/upload-youtube-source">client.sources.<a href="./src/graphor/resources/sources.py">upload_youtube</a>(\*\*<a href="src/graphor/types/source_upload_youtube_params.py">params</a>) -> <a href="./src/graphor/types/public_source.py">PublicSource</a></code>
