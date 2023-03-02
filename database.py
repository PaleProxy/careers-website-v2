from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://6dgoi1cfetbd3x27bx9m:pscale_pw_uci6rLbsEdrFRUFWY3Hrw4It1W5mdDNpMXUK7uwpLzz@aws-eu-west-2.connect.psdb.cloud/joviancareers?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
  "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
  }
})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    column_names = result.keys()
    jobs = []
    for row in result.all():
      jobs.append(dict(zip(column_names, row)))
    return jobs