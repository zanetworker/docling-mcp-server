# Docling MCP Server

A Model Context Protocol (MCP) server for converting documents to markdown using the Docling library. This server enables Claude and other AI assistants to process and extract content from various document formats.

## Features

- Convert documents from URLs or local files to markdown
- Extract tables from documents
- Convert documents with embedded images
- Support for OCR (Optical Character Recognition)
- Batch processing of multiple documents
- Caching of conversion results for improved performance
- Hardware acceleration support (MPS on macOS)

## Installation

### Prerequisites

- Python 3.10 or higher
- Docling library
- MCP library

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mcp-docling.git
   cd mcp-docling
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the package:
   ```bash
   pip install -e .
   ```

## Usage

### Development Mode

Run the server in development mode:

```bash
mcp dev mcp_docling/server.py
```

### "Production" Mode (as a module)

Run the server as a module:

```bash
python -m mcp_docling
```

### Integration with Claude Desktop

To use this server with Claude Desktop, add the following configuration to your Claude Desktop config file (located at `~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "docling": {
      "command": "/path/to/your/python/environment/bin/python",
      "args": [
        "-m",
        "mcp_docling"
      ],
      "env": {
        "PYTHONPATH": "/path/to/your/project/directory"
      }
    }
  }
}
```

Replace the paths with your actual Python environment and project directory paths.

## Available Tools

### convert_document

Converts a document from a URL or local path to markdown format.

```python
convert_document("https://arxiv.org/pdf/2408.09869")
convert_document("/path/to/document.pdf", enable_ocr=True, ocr_language=["en"])
```

### convert_document_with_images

Converts a document and returns both markdown text and embedded images.

```python
convert_document_with_images("https://arxiv.org/pdf/2408.09869")
```

### extract_tables

Extracts tables from a document and returns them as structured data.

```python
extract_tables("https://arxiv.org/pdf/2408.09869")
```

### convert_batch

Converts multiple documents in batch mode.

```python
convert_batch(["https://arxiv.org/pdf/2408.09869", "/path/to/document.pdf"])
```

### get_system_info

Returns information about the system configuration and acceleration status.

```python
get_system_info()
```

## Testing

You can test the server using the provided test script:

```bash
python test_docling_server.py
```

Make sure to set the required environment variables before running the test:

```bash
export INFERENCE_MODEL="your-model-id"
export LLAMA_STACK_PORT="8080"
```

## Configuration

The server supports various configuration options:

- OCR support with language selection
- Hardware acceleration (MPS on macOS)
- Caching of conversion results
- Batch processing settings

## Troubleshooting

If you encounter issues:

1. Check the logs for error messages
2. Verify that your Python environment has all required dependencies
3. Ensure the PYTHONPATH is correctly set in your configuration
4. For hardware acceleration issues, check that your system supports the configured accelerator

## License

[Your License Here]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
