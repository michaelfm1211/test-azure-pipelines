from multiprocessing import Process
import pytest


def test_run():
    server = Process(target="gunicorn app:app")
    server.start()
    server.terminate()

