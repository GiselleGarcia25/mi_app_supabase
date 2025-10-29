from supabase import create_client, Client

# Aquí pegas tus claves desde Supabase
SUPABASE_URL = "https://mrourfyaunnpgscktcgu.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1yb3VyZnlhdW5ucGdzY2t0Y2d1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjE3NDcwOTQsImV4cCI6MjA3NzMyMzA5NH0.hFSDH1LePrIOWlPkv4Qox54Jkr2umz6PvlzGI_F4YJM"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
