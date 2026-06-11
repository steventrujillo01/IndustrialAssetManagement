FROM python:3.12-slim

WORKDIR /app

# install uv
RUN pip install uv

# copy dependency files first (cache layer)
COPY pyproject.toml uv.lock requirements.txt ./

# install dependencies (SYSTEM MODE - IMPORTANT)
RUN uv pip install --system -r requirements.txt

# copy source code
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]