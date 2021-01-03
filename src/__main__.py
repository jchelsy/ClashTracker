from src import app

if __name__ == "__main__":
    TH_level = 10
    clash = app.Control("Jchelsy", TH_level)
    clash.initialize()
    clash.print()
