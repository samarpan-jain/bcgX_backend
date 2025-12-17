import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()
if __name__=='__main__':
    uvicorn.run(
        "api.v1.routes:app",
        host=os.getenv("APP_HOST","127.0.0.1"),
        port=int(os.getenv("APP_PORT", 8080)),
        reload=bool(os.getenv("IS_DEBUG", True)),
        log_level="info",
        use_colors=False
    )