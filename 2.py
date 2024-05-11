from datetime import datetime, timedelta
today = datetime.now()
du_ruz_pesh = today - timedelta(days=2)
du_ruz_bad = today + timedelta(days=2)
print("Du ruz pesh: ", du_ruz_pesh.strftime("%Y-%m-%d"))
print("Today: ", today.strftime("%Y-%m-%d"))
print("Du ruz bad: ", du_ruz_bad.strftime("%Y-%m-%d"))
