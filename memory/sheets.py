import os,logging
class SheetsMemory:
    def __init__(self):
        self.sheet=None; sid=os.getenv("GOOGLE_SHEETS_ID"); path=os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE","credentials.json")
        if sid and os.path.isfile(path):
            try:
                import gspread
                self.sheet=gspread.service_account(filename=path).open_by_key(sid).sheet1
                if not self.sheet.get_all_values(): self.sheet.append_row(["timestamp","kind","question","answer"])
            except Exception as e: logging.warning("Sheets init: %s",e)
    def save(self,kind,q,a):
        if self.sheet:
            from datetime import datetime,timezone
            try:self.sheet.append_row([datetime.now(timezone.utc).isoformat(),kind,q,a])
            except Exception as e:logging.warning("Save: %s",e)
    def recent_context(self,limit=8):
        if not self.sheet:return ""
        try:
            rows=self.sheet.get_all_values()[-limit:]
            return "\n\n".join("Q: "+r[2]+"\nA: "+r[3] for r in rows if len(r)>3)
        except Exception:return ""
