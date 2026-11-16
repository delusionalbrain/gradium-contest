import asyncio
import gradium
import os
from dotenv import load_dotenv
load_dotenv()
async def main():
    client = gradium.client.GradiumClient(api_key=os.getenv("GRADIUM_API_KEY"))

    result = await client.tts(
        setup={"voice_id": "Bla6SbVMczYnOhfK", "output_format": "wav"},
        text="Ms. Gupta was here tryna be non-chalant as fuck. What do you think about her approach to Article 321a/c. What about the formula she concocted in it H2SO4 on 24/04/2026"
    )

    with open("test1.wav", "wb") as f:
        f.write(result.raw_data)

if __name__ == "__main__":
    asyncio.run(main())