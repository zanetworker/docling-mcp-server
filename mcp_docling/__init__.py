import argparse
import logging
from .server import mcp

def main():
    """MCP Docling: Convert documents to markdown using Docling."""
    parser = argparse.ArgumentParser(
        description="Convert documents to markdown using Docling."
    )
    parser.add_argument(
        "--timeout", 
        type=int, 
        default=600,  # Increase to 10 minutes
        help="Timeout in seconds for MCP server requests"
    )
    args = parser.parse_args()
    
    # Log the timeout value
    logging.info(f"Starting MCP server with timeout: {args.timeout} seconds")
    
    # Run the MCP server with the specified timeout
    mcp.run(timeout=args.timeout)

if __name__ == "__main__":
    main() 