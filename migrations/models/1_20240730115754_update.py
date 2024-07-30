from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "todos" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "title" VARCHAR(100) NOT NULL,
    "done" BOOL NOT NULL  DEFAULT False,
    "created_at" TIMESTAMPTZ   DEFAULT CURRENT_TIMESTAMP
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "todos";"""
