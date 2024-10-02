# Copyright (c) 2024 AwesomeHelpersInc. All rights reserved.
# This file is part of the EmailerWorker project.

import asyncio
import uuid

from src.core.context import request_id_context

if __name__ == "__main__":
    from src.app.app import AskDocsApp

    ## Set Request ID
    request_id_context.set(str(uuid.uuid4()))

    ## Start Service
    app = AskDocsApp()

    # Run the async start method using asyncio's event loop
    asyncio.run(app.start())
