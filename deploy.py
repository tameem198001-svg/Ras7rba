"""
deploy.py
Lightweight deployment helper (local). Use `python deploy.py` to run streamlit.
"""
import os
import subprocess

if __name__ == '__main__':
    cmd = os.environ.get('STREAMLIT_CMD', 'streamlit run streamlit_app.py')
    print('Running:', cmd)
    subprocess.run(cmd, shell=True)
