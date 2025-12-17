from fastapi import FastAPI
from api.v1.authRoutes import authRoutes
from api.v1.userRoutes import userRoutes
from core.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

try:
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")
except Exception as e:
    print("Error creating database tables:", e)

app = FastAPI(title="Pricing Optimization Manager API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost:5173"],  # Allow all origins for CORS
    allow_credentials=True,  # Allow cookies, authorization headers, etc.
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers in the request
)

app.include_router(authRoutes, prefix="/api/v1/auth")
app.include_router(userRoutes, prefix="/api/v1/users")