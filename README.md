# MCP Firebase Server

A skeleton project for building your own Model Context Protocol (MCP) server with Firebase integration, using Claude Desktop as your MCP client.

## Overview

This project provides a foundation for creating custom MCP servers that integrate with Firebase services. It allows you to build tools that Claude Desktop can interact with, enabling powerful automation and data management capabilities through Firebase.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10 or higher**
- **MCP SDK**
- **uv** (Package Manager)

## Installation

### Step 1: Install uv Package Manager

#### macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### Verify Installation

```bash
uv --version
```

### Step 2: Setup Your Project

Initialize and configure your MCP server project:

```bash
# Initialize the project
uv init mcp-server

# Navigate to project directory
cd mcp-server

# Create a virtual environment
uv venv

# Activate the virtual environment
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate     # Windows
```

### Step 3: Install Required Packages

Install all necessary dependencies within the virtual environment:

```bash
uv add "mcp[cli]" firebase_admin
```

### Step 4: Configure Firebase

#### Download Service Account Key

1. Navigate to your [Firebase Console](https://console.firebase.google.com/)
2. Go to **Project Settings**
3. Click on the **Service Accounts** tab
4. Click **Generate new private key**
5. Save the downloaded JSON file to your project's main directory

#### Update Configuration

Open `main.py` and update the Firebase credentials path:

```python
cred = credentials.Certificate("path/to/your/serviceAccountKey.json")
```

Replace the path with the actual location of your service account JSON file.

> ⚠️ **Security Note**: Never commit your service account key to version control. Add it to `.gitignore`.

## Development

### Step 5: Create Your Tools

Write your custom tools in `main.py`:

```python
@mcp.tool()
def your_tool_name(param1: str, param2: int) -> str:
    """
    Detailed description of what this tool does.
    The LLM uses this description for chain-of-thought processing.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter
        
    Returns:
        Description of return value
    """
    # Your implementation here
    pass
```

**Important**: 
- Add the `@mcp.tool()` decorator above each function
- Write detailed descriptions to help the LLM choose appropriate tools
- Include clear parameter and return value documentation

### Step 6: Test Your Tools

Test individual tools before integrating with Claude Desktop:

```bash
mcp dev main.py
```

This opens the **MCP Inspector** in your browser, providing:
- Interactive tool testing interface
- Real-time logs and error messages
- Performance monitoring
- Temporary environment variable configuration

## Integration with Claude Desktop

### Step 7: Install MCP Server

Add your server to Claude Desktop's configuration:

```bash
mcp install main.py
```

This automatically registers your server with Claude Desktop.

### Step 8: Verify Installation

1. **Restart Claude Desktop** application
2. Run test queries to verify your tools are working
3. Check that Claude can successfully call your custom tools

If everything works correctly, congratulations! You've successfully created your MCP server with Firebase integration.

## Usage

Once integrated, you can interact with your Firebase data through natural language queries in Claude Desktop. The MCP server will handle the communication between Claude and your Firebase backend.

## Troubleshooting

- Ensure your virtual environment is activated when running commands
- Verify Firebase credentials are correctly configured
- Check the MCP Inspector logs for detailed error messages
- Restart Claude Desktop after making configuration changes

## Support

For questions or issues, contact:
📧 [abdulraffay2494@gmail.com](mailto:abdulraffay2494@gmail.com)

## Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [Firebase Admin SDK](https://firebase.google.com/docs/admin/setup)
- [Claude Desktop](https://claude.ai/download)

## License

This is a skeleton project intended for customization and extension based on your specific needs.

---

**Happy Building!** 🚀