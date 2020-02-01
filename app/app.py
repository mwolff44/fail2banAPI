# Copyright 2019 (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from fastapi import FastAPI

from .routers import global
from .routers import jail

def get_app(config: dict):
    app = FastAPI()
    app.include_router(global.router)
    app.include_router(jail.router)

    return app
