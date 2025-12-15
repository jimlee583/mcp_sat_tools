import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main():
    server_url = "http://localhost:8000/mcp"

    print(f"Connecting to MCP server at {server_url} ...")

    # Open MCP connection
    async with streamablehttp_client(server_url) as (read, write, _):
        async with ClientSession(read, write) as session:

            # Handshake
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print("\nTools available from server:")
            for t in tools.tools:
                print(" -", t.name)

            # --- Test tool #1: add ---
            print("\nCalling add(a=3, b=5)...")
            add_result = await session.call_tool("add", {"a": 3, "b": 5})
            print("Add Result:", add_result.structuredContent)

            # --- Test tool #2: compute_power_budget ---
            print("\nCalling compute_power_budget(...) ...")

            pb_result = await session.call_tool(
                "compute_power_budget",
                {
                    "payload_power_w": 5000,
                    "eclipse_fraction": 0.35,
                    "bus_power_margin": 0.30,
                },
            )

            print("Power Budget Result:", pb_result.structuredContent)


if __name__ == "__main__":
    asyncio.run(main())
