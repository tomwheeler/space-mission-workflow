import random
from temporalio import activity


@activity.defn
async def read_probes() -> dict:
    # Simulate coordinate and temperature readings
    a = random.randint(100, 99999)
    x = random.randint(1000, 9999)
    y = random.randint(1000, 9999)
    temperature = random.uniform(-120, -30)

    result = {
        "altitude": f"{a} kilometers",
        "location": f"X:{x} Y:{y}",
        "temperature": f"{temperature:.1f}°C",
    }

    activity.logger.info(f"Collected measurement: {result}")
    return result
