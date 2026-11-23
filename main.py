import logging
from dotenv import load_dotenv
from brain.gemini import GeminiBrain
from learning.worker import LearningWorker
from memory.sheets import SheetsMemory
load_dotenv()
logging.basicConfig(level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s")
def main():
    brain=GeminiBrain(); memory=SheetsMemory(); worker=LearningWorker(brain,memory)
    print("Tiwari AI Engineer | /learn research | /quit exit")
    while True:
        try:
            q=input("\nYou> ").strip()
            if q.lower() in {"/quit","/exit"}: break
            if q=="/learn": print(worker.run_once()); continue
            if not q: continue
            ans=brain.ask(q,context=memory.recent_context())
            print("\nTiwari> "+ans); memory.save("chat",q,ans)
        except KeyboardInterrupt: break
        except Exception as e: logging.exception(e); print("Error:",e)
if __name__=="__main__": main()
