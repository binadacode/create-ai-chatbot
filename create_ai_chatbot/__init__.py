"""
create-ai-chatbot: Scaffold a full-stack AI chatbot project.

Usage:
    create-ai-chatbot [PROJECT_DIR]

Interactive prompts let you choose backend, frontend, LLM provider, and theme.
"""

__version__ = "0.1.0"

import argparse
import sys
from pathlib import Path

try:
    from cookiecutter.main import cookiecutter
except ImportError:
    print("ERROR: cookiecutter is required. Install with: pip install cookiecutter")
    sys.exit(1)


def get_template_dir():
    """Return the path to the cookiecutter template directory."""
    return Path(__file__).parent / "template"


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a full-stack AI chatbot project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
Examples:
  create-ai-chatbot                    # Interactive mode
  create-ai-chatbot my-chatbot         # Create in ./my-chatbot
  create-ai-chatbot --no-input         # Use all defaults
        """,
    )
    parser.add_argument(
        "output_dir",
        nargs="?",
        default=".",
        help="Output directory (default: current directory)",
    )
    parser.add_argument(
        "--no-input",
        action="store_true",
        help="Use default values for all prompts",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0",
    )

    args = parser.parse_args()

    template_dir = get_template_dir()

    if not (template_dir / "cookiecutter.json").exists():
        print(f"ERROR: No cookiecutter.json found in {template_dir}", file=sys.stderr)
        sys.exit(1)

    print("=" * 50)
    print("  create-ai-chatbot")
    print("  Full-stack AI chatbot scaffolding tool")
    print("=" * 50)
    print()

    try:
        result = cookiecutter(
            str(template_dir),
            output_dir=args.output_dir,
            no_input=args.no_input,
        )
        print()
        print(f"Project created in: {result}")
        print()
        print("Next steps:")
        print(f"  cd {result}")
        print("  # Backend:")
        print("  cd backend && cp .env.example .env && pip install -r requirements.txt")
        print("  python -m uvicorn main:app --reload")
        print("  # Frontend (in another terminal):")
        print("  cd frontend && npm install && npm run dev")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
