@echo off
set PYTHONPATH=%cd%\src
python -m unittest discover tests

