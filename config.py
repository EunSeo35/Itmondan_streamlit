# config.py

import streamlit as st
import os

def get_db_config():
    if "database" in st.secrets:
        return st.secrets["database"]
    else:
        # 로컬에서 테스트용 설정 (예: secrets.toml 없을 때)
        return {
            "host": os.getenv("DB_HOST", "localhost"),
            "port": int(os.getenv("DB_PORT", 3306)),
            "user": os.getenv("DB_USER", "root"),
            "password": os.getenv("DB_PASSWORD", "1234"),
            "database": os.getenv("DB_NAME", "mydb")
        }

DB_CONFIG = get_db_config()
