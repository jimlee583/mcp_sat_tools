def add_core(a: int, b: int) -> int:
    """
    Pure add function used by the MCP tool.

    Keeping the core logic separate from the MCP wrapper
    makes testing and reusability easier.
    """
    return a + b
