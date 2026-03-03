import os
from pathlib import Path

def create_project_structure(base_name="langgraph_project"):
    """Creates a production-ready directory structure for a LangGraph + FastAPI project."""
    
    # Define the directory tree
    directories = [
        ".github/workflows",  # For CI/CD pipelines
        "agent",              # Core LangGraph logic
        "api",                # FastAPI backend
        "config",             # Configuration and environment management
        "tests",              # Unit and integration tests
    ]
    
    # Define the initial files to create inside those directories
    files = {
        # GitHub Actions
        ".github/workflows/ci.yml": "# CI pipeline definition goes here\n",
        
        # Agent Logic
        "agent/__init__.py": "",
        "agent/graph.py": "# Define your LangGraph workflow here\n",
        "agent/nodes.py": "# Define individual node functions here\n",
        "agent/state.py": "# Define your graph's State schema (TypedDict or Pydantic) here\n",
        "agent/tools.py": "# Define custom tools for your agent here\n",
        
        # FastAPI Application
        "api/__init__.py": "",
        "api/main.py": "# FastAPI application instance and middleware\n",
        "api/routes.py": "# API endpoints (e.g., /chat, /health)\n",
        "api/schemas.py": "# Pydantic models for request and response validation\n",
        
        # Configuration
        "config/__init__.py": "",
        "config/settings.py": "# Load environment variables and global settings\n",
        
        # Testing
        "tests/__init__.py": "",
        "tests/test_agent.py": "# Tests for LangGraph logic\n",
        "tests/test_api.py": "# Tests for FastAPI endpoints\n",
        
        # Root level files
        "Dockerfile": "# Docker build instructions\n",
        "docker-compose.yml": "# Multi-container orchestration (e.g., App + Database)\n",
        "environment.yml": "# Mamba/Conda environment dependencies\n",
        ".env.example": "OPENAI_API_KEY=your_key_here\nLANGSMITH_API_KEY=your_key_here\nLANGCHAIN_TRACING_V2=true\nLANGCHAIN_PROJECT=langgraph_prod\n",
        ".gitignore": "__pycache__/\n*.pyc\n.env\n.pytest_cache/\n",
        "README.md": f"# {base_name}\n\nProduction LangGraph Agent.\n",
    }

    print(f"Creating project structure for: {base_name}...")
    
    # Create directories
    for directory in directories:
        dir_path = Path(base_name) / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {dir_path}")

    # Create files
    for file_path, content in files.items():
        full_path = Path(base_name) / file_path
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created file: {full_path}")

    print("\nProject structure generated successfully!")

if __name__ == "__main__":
    create_project_structure("my_ai_agent")