import json
import asyncio
from lagent.actions.web_browser import BochaSearch

async def main():
    web_browser = BochaSearch('xxxx', 3)
    search_resp = await web_browser.asearch('拼多多 2024 年的业绩表现和财报')
    print(json.dumps(search_resp, ensure_ascii=False))

if __name__ == '__main__':
    asyncio.run(main())