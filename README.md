# Redshift Data API

这是一个基于 FastAPI + SQLAlchemy 构建的简单 API 项目，用于从 Amazon Redshift 数据库中查询数据并通过 HTTP 接口返回。

---

## 🔧 环境变量配置

请在项目根目录下创建 `.env` 文件，并填写以下变量（`.env.example` 提供了格式参考）：

```env
REDSHIFT_USER=your_user
REDSHIFT_PASS=your_password
REDSHIFT_HOST=your_host
REDSHIFT_PORT=5439
REDSHIFT_DB=your_db
