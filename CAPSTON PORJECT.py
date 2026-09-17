#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('writefile', 'crud.py', 'from fastapi import FastAPI\nfrom pydantic import BaseModel\nfrom sqlalchemy import create_engine, Integer,Column,String, Boolean\nfrom sqlalchemy.orm import declarative_base, sessionmaker\n\napp =FastAPI()\nDATABASE_URL = "sqlite:///./todo.db"\nengine= create_engine (DATABASE_URL,connect_args+{"check_some_threads":False}\nBase=declarative_base()\nsessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)\nclass TaskDB(Base):\n    __tablename__ ="task"\n    id=column(Integer,primary_key=True)\n    title=column(String)\n    is_done=column(Boolean, default=False)\nBase.metadata.creat_all(bind=engine)\nclass Task(BaseModel)\n    id:int\n    title:str\n    is_done:bool=False\n\n@app.post ("/tasks")\ndef creat_task(task:Task):\n    db =sessionlocal()\n    new_task=TaskDB(id=task.id,title=task.titel,is_done=task.is_done\n    db.add(new_task)\n    db.commit()\n    db.refrash(new_task)\n    db.close()\n\n@app.get("/tasks")\ndef get_task():\n    db=sessionlocal()\n    tasks=db.query(TaskDB).all()\n    db.close()\n    return tasks\n\n\n\n\n\n\n')


# In[ ]:




