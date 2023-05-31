@echo off
call %UserProfile%\Anaconda3\Scripts\activate.bat
conda activate falcon_env
python run.py
pause