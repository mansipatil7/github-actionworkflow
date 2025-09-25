#!/usr/bin/env python3
import os

environment = os.getenv("DOCKER_TAG", "PRODUCTION")

if environment == "dev":
    print("Development Server Running!")
    print("Debug mode: ON")
elif environment == "test":
    print(" Test Environment!")
    print("Running in test mode")
else:
    print("Production Server Running!")
    print("Environment: PRODUCTION")