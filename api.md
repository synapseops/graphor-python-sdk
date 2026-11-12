# Sources

Types:

```python
from graphor.types import (
    Element,
    Method,
    PublicSource,
    SourceListResponse,
    SourceDeleteResponse,
    SourceAskResponse,
    SourceExtractResponse,
    SourceGetBuildStatusResponse,
    SourceGetElementsResponse,
    SourceGetPageScreenshotResponse,
    SourceIndexBuildResponse,
    SourceIngestFileResponse,
    SourceIngestGitHubResponse,
    SourceIngestURLResponse,
    SourceIngestYoutubeResponse,
    SourceReprocessResponse,
    SourceRetrieveChunksResponse,
    Folder,
    SourceListFoldersResponse,
    SourceCreateFolderResponse,
    SourceRenameFolderResponse,
    SourceRemoveFolderResponse,
    SourceDeleteFolderResponse,
    SourceMoveResponse,
)
```

Methods:

- <code title="get /sources">client.sources.<a href="./src/graphor/resources/sources.py">list</a>(\*\*<a href="src/graphor/types/source_list_params.py">params</a>) -> <a href="./src/graphor/types/source_list_response.py">SourceListResponse</a></code>
- <code title="delete /sources/delete">client.sources.<a href="./src/graphor/resources/sources.py">delete</a>(\*\*<a href="src/graphor/types/source_delete_params.py">params</a>) -> <a href="./src/graphor/types/source_delete_response.py">SourceDeleteResponse</a></code>
- <code title="post /sources/ask-sources">client.sources.<a href="./src/graphor/resources/sources.py">ask</a>(\*\*<a href="src/graphor/types/source_ask_params.py">params</a>) -> <a href="./src/graphor/types/source_ask_response.py">SourceAskResponse</a></code>
- <code title="post /sources/run-extraction">client.sources.<a href="./src/graphor/resources/sources.py">extract</a>(\*\*<a href="src/graphor/types/source_extract_params.py">params</a>) -> <a href="./src/graphor/types/source_extract_response.py">SourceExtractResponse</a></code>
- <code title="get /sources/builds/{build_id}">client.sources.<a href="./src/graphor/resources/sources.py">get_build_status</a>(build_id, \*\*<a href="src/graphor/types/source_get_build_status_params.py">params</a>) -> <a href="./src/graphor/types/source_get_build_status_response.py">SourceGetBuildStatusResponse</a></code>
- <code title="get /sources/get-elements">client.sources.<a href="./src/graphor/resources/sources.py">get_elements</a>(\*\*<a href="src/graphor/types/source_get_elements_params.py">params</a>) -> <a href="./src/graphor/types/source_get_elements_response.py">SourceGetElementsResponse</a></code>
- <code title="get /sources/{file_id}/pages/{page_number}/screenshot">client.sources.<a href="./src/graphor/resources/sources.py">get_page_screenshot</a>(page_number, \*, file_id, \*\*<a href="src/graphor/types/source_get_page_screenshot_params.py">params</a>) -> <a href="./src/graphor/types/source_get_page_screenshot_response.py">SourceGetPageScreenshotResponse</a></code>
- <code title="post /sources/index">client.sources.<a href="./src/graphor/resources/sources.py">index_build</a>(\*\*<a href="src/graphor/types/source_index_build_params.py">params</a>) -> <a href="./src/graphor/types/source_index_build_response.py">SourceIndexBuildResponse</a></code>
- <code title="post /sources/ingest-file">client.sources.<a href="./src/graphor/resources/sources.py">ingest_file</a>(\*\*<a href="src/graphor/types/source_ingest_file_params.py">params</a>) -> <a href="./src/graphor/types/source_ingest_file_response.py">SourceIngestFileResponse</a></code>
- <code title="post /sources/ingest-github">client.sources.<a href="./src/graphor/resources/sources.py">ingest_github</a>(\*\*<a href="src/graphor/types/source_ingest_github_params.py">params</a>) -> <a href="./src/graphor/types/source_ingest_github_response.py">SourceIngestGitHubResponse</a></code>
- <code title="post /sources/ingest-url">client.sources.<a href="./src/graphor/resources/sources.py">ingest_url</a>(\*\*<a href="src/graphor/types/source_ingest_url_params.py">params</a>) -> <a href="./src/graphor/types/source_ingest_url_response.py">SourceIngestURLResponse</a></code>
- <code title="post /sources/ingest-youtube">client.sources.<a href="./src/graphor/resources/sources.py">ingest_youtube</a>(\*\*<a href="src/graphor/types/source_ingest_youtube_params.py">params</a>) -> <a href="./src/graphor/types/source_ingest_youtube_response.py">SourceIngestYoutubeResponse</a></code>
- <code title="post /sources/reprocess">client.sources.<a href="./src/graphor/resources/sources.py">reprocess</a>(\*\*<a href="src/graphor/types/source_reprocess_params.py">params</a>) -> <a href="./src/graphor/types/source_reprocess_response.py">SourceReprocessResponse</a></code>
- <code title="post /sources/prebuilt-rag">client.sources.<a href="./src/graphor/resources/sources.py">retrieve_chunks</a>(\*\*<a href="src/graphor/types/source_retrieve_chunks_params.py">params</a>) -> <a href="./src/graphor/types/source_retrieve_chunks_response.py">SourceRetrieveChunksResponse</a></code>
- <code title="get /sources/folders">client.sources.<a href="./src/graphor/resources/sources.py">list_folders</a>() -> <a href="./src/graphor/types/source_list_folders_response.py">SourceListFoldersResponse</a></code>
- <code title="post /sources/create-folder">client.sources.<a href="./src/graphor/resources/sources.py">create_folder</a>(\*\*<a href="src/graphor/types/source_create_folder_params.py">params</a>) -> <a href="./src/graphor/types/source_create_folder_response.py">SourceCreateFolderResponse</a></code>
- <code title="post /sources/rename-folder">client.sources.<a href="./src/graphor/resources/sources.py">rename_folder</a>(\*\*<a href="src/graphor/types/source_rename_folder_params.py">params</a>) -> <a href="./src/graphor/types/source_rename_folder_response.py">SourceRenameFolderResponse</a></code>
- <code title="post /sources/remove-folder">client.sources.<a href="./src/graphor/resources/sources.py">remove_folder</a>(\*\*<a href="src/graphor/types/source_remove_folder_params.py">params</a>) -> <a href="./src/graphor/types/source_remove_folder_response.py">SourceRemoveFolderResponse</a></code>
- <code title="post /sources/delete-folder">client.sources.<a href="./src/graphor/resources/sources.py">delete_folder</a>(\*\*<a href="src/graphor/types/source_delete_folder_params.py">params</a>) -> <a href="./src/graphor/types/source_delete_folder_response.py">SourceDeleteFolderResponse</a></code>
- <code title="post /sources/move-sources">client.sources.<a href="./src/graphor/resources/sources.py">move</a>(\*\*<a href="src/graphor/types/source_move_params.py">params</a>) -> <a href="./src/graphor/types/source_move_response.py">SourceMoveResponse</a></code>
