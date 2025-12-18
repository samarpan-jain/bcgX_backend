from fastapi import HTTPException

class APIResponse:
    status_code: int
    message: str
    data: dict|None = None

    @staticmethod
    def generateError(status_code: int, message: str) -> dict:
        response = {
            "message": message,
        }
        raise HTTPException(status_code=status_code, detail=response)
    
    @staticmethod
    def generateSuccess(status_code: int, message: str, data: dict|None = None) -> dict:
        response = {
            "status_code": status_code,
            "message": message,
        }
        if data is not None:
            response["data"] = data
        return response